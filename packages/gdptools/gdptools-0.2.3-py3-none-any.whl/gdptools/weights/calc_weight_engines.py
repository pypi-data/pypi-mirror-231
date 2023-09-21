# sourcery skip: inline-immediately-returned-variable
"""Abstract Base Class for Template behavior pattern for calculating weights."""
import logging
import os
import time
from abc import ABC
from abc import abstractmethod
from collections.abc import Generator
from typing import Any
from typing import List
from typing import Literal
from typing import Tuple
from typing import Union

import dask.bag as db
import dask_geopandas as dgpd
import geopandas as gpd
import numpy as np
import numpy.typing as npt
import pandas as pd
from joblib import delayed
from joblib import Parallel
from joblib import parallel_backend
from shapely import area
from shapely import intersection

from gdptools.utils import _check_feature_crs
from gdptools.utils import _check_grid_cell_crs
from gdptools.utils import _check_source_poly_idx
from gdptools.utils import _check_target_poly_idx
from gdptools.utils import _get_crs
from gdptools.utils import _reproject_for_weight_calc

logger = logging.getLogger(__name__)

SOURCE_TYPES = Literal["grid", "poly"]


class CalcWeightEngine(ABC):
    """Abstract Base Class (ABC) implementing the template behavioral pattern.

    Abstract Base Class for calculating weights.  There are several weight generation
    methods implemented and they all share a common workflow with different methods
    for calculating the weights.  This ABC defines the calc_weights() workflow, with
    an @abstractmethod for get_weight_components() where new methods can be plugged
    in for weight generation.

    These methods create a table, that describes the intersection between each source polygon and each target polygon.
    In the case of grid-to-poly weight generation, a source polygon represents the cell of a grid, each cell is
    identified by it's i,j index (row, column).  In the case of poly-to-poly intersections the indexes are simply the
    index of the source and the index of the target.  The weights are the fraction area of the source polygon to the
    total area of the target polygon.

    The result is a table that can be used for area-weighted interpolation of the source to the target.

    Note: For grid-to-poly weight generation the use of these classes is controlled by the WeightGen class and for
        poly-to-poly weight generation, these classes are controlled by the WeightGenP2P class, thus most users will
        not use these classes directly.
    """

    def calc_weights(
        self,
        target_poly: gpd.GeoDataFrame,
        target_poly_idx: str,
        source_poly: gpd.GeoDataFrame,
        source_poly_idx: List[str],
        source_type: SOURCE_TYPES,
        wght_gen_crs: Any,
        filename: str = "",
        intersections: bool = False,
        jobs: int = -1,
        verbose: bool = False,
    ) -> Union[Tuple[pd.DataFrame, gpd.GeoDataFrame], pd.DataFrame]:
        """Template method for calculating weights.

        Args:
            target_poly (gpd.GeoDataFrame): GeoDataFrame containing the target polygons for weight calculation.
            target_poly_idx (str): Column name in the target_poly GeoDataFrame containing unique identifiers for each
                target polygon.
            source_poly (gpd.GeoDataFrame): GeoDataFrame containing the source polygons used in weight calculation.
            source_poly_idx (List[str]): List of column names in the source_poly GeoDataFrame containing unique
                identifiers for each source polygon.
            source_type (SOURCE_TYPES): Type of the source polygons, possibly indicating their use or attributes.
            wght_gen_crs (Any): Coordinate reference system used when generating weights.
            filename (str): Optional filename to save results. If not provided, results won't be saved.
            intersections (bool): Whether to calculate intersections between the target and source polygons.
                Defaults to False.
            jobs (int): Number of parallel jobs to run. If set to -1, all available cores will be used. Defaults to -1.
            verbose (bool): If set to True, prints detailed information during execution. Defaults to False.


        Returns:
            Union[pd.DataFrame, Optional[gpd.GeoDataFrame]]: Union[pd.DataFrame, Optional[gpd.GeoDataFrame]]: Either a
                DataFrame or, based on certain conditions, a GeoDataFrame containing the calculated weights.
        """
        self.target_poly = target_poly.reset_index()
        self.target_poly_idx = target_poly_idx
        self.source_poly = source_poly.reset_index()
        self.source_poly_idx = source_poly_idx
        self.source_type = source_type
        self.wght_gen_crs = wght_gen_crs
        self.filename = filename
        self.intersections = intersections

        if jobs == -1:
            self.jobs = int(os.cpu_count() / 2)  # type: ignore
            logger.info(" ParallelWghtGenEngine getting jobs from os.cpu_count()")
        else:
            self.jobs = jobs
        logger.info(f"  ParallelWghtGenEngine using {self.jobs} jobs")
        self.verbose = verbose
        _check_target_poly_idx(self.target_poly, self.target_poly_idx)
        _check_source_poly_idx(self.source_poly, self.source_poly_idx)
        _check_feature_crs(poly=self.target_poly)
        _check_grid_cell_crs(grid_cells=self.source_poly)
        self.grid_out_crs = _get_crs(self.wght_gen_crs)
        self.target_poly, self.source_poly = _reproject_for_weight_calc(
            target_poly=self.target_poly,
            source_poly=self.source_poly,
            wght_gen_crs=self.grid_out_crs,
        )
        if self.intersections:
            print(f"Intersections = {self.intersections}")
            if self.source_type == "grid":
                (
                    self.plist,
                    self.ilist,
                    self.jlist,
                    self.wghtlist,
                    self.calc_intersect,
                ) = self.get_weight_components_and_intesections()
            elif self.source_type == "poly":
                (
                    self.plist,
                    self.splist,
                    self.wghtlist,
                    self.calc_intersect,
                ) = self.get_weight_components_and_intesections()
        elif self.source_type == "grid":
            (
                self.plist,
                self.ilist,
                self.jlist,
                self.wghtlist,
            ) = self.get_weight_components()
        elif self.source_type == "poly":
            (
                self.plist,
                self.splist,
                self.wghtlist,
            ) = self.get_weight_components()
        self.wght_df = self.create_wght_df()
        if self.filename:
            self.wght_df.to_csv(self.filename)
        if self.intersections:
            return self.wght_df, self.calc_intersect
        else:
            return self.wght_df
        # return (  # type: ignore
        #     self.wght_df, self.calc_intersect
        #     if self.intersections
        #     else self.wght_df
        # )

    @abstractmethod
    def get_weight_components(
        self,
    ) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
        """Abstract method for calculating weights.

        Classes that inherit this method will override this method for
        weight-generation.

        if self.source_type == "grid"
        Returned tuples in order:
            1) plist:  list of target poly ids.
            2) ilist i-index of grid_cells.
            3) jlist j-index of grid_cells.
            4) wghtslist weight values of i,j index of grid_cells.

        if self.source_type == "poly"
        Returned tuples in order:
            1) plist: list of target poly ids.
            2) splist: list of source poly ids.
            3) wghtslist weight values of source polygons.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float]],
                Tuple[List[object], List[object], List[float]]
            ]
        """
        pass

    @abstractmethod
    def get_weight_components_and_intesections(
        self,
    ) -> Union[
        Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
        Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
    ]:
        """Abstract method for calculating weights.

        Classes that inherit this method will override this method for \
            weight-generation.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float],
                    gpd.GeoDataFrame],
                Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist:  list of target poly ids.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.
                5) GeoDataFrame of intersection geometries.

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of target poly ids.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
                4) GeoDataFrame of intersection geometries.
        """
        pass

    def create_wght_df(self) -> pd.DataFrame:
        """Create dataframe from weight components."""
        if self.source_type == "grid":
            wght_df = pd.DataFrame(
                {
                    self.target_poly_idx: self.plist,
                    "i": self.ilist,
                    "j": self.jlist,
                    "wght": self.wghtlist,
                }
            )
            wght_df = wght_df.astype({"i": int, "j": int, "wght": float, self.target_poly_idx: str})
        elif self.source_type == "poly":
            wght_df = pd.DataFrame(
                {
                    self.target_poly_idx: self.plist,
                    self.source_poly_idx[0]: self.splist,
                    "wght": self.wghtlist,
                }
            )
            wght_df = wght_df.astype({"wght": float, self.target_poly_idx: str, self.source_poly_idx[0]: str})
        return wght_df


class SerialWghtGenEngine(CalcWeightEngine):
    """Method to generate grid-to-polygon weight.

    This class is **based on and adapted** from methods provided in the Tobler package. See
        area_tables_binning() method.

    Args:
        CalcWeightEngine (ABC): Abstract Base Class (ABC) employing the Template behavior
            pattern.  The abstractmethod get weight components provides a method to plug-
            in new weight generation methods.
    """

    def get_weight_components(
        self,
    ) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float]],
                Tuple[List[object], List[object], List[float]]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist:  list of target poly ids.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of target poly ids.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            (
                plist,
                ilist,
                jlist,
                wghtslist,
            ) = self.area_tables_binning(
                source_df=self.source_poly,
                target_df=self.target_poly,
                source_type=self.source_type,
            )
        elif self.source_type == "poly":
            (
                plist,
                splist,
                wghtslist,
            ) = self.area_tables_binning(
                source_df=self.source_poly,
                target_df=self.target_poly,
                source_type=self.source_type,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")
        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist
        elif self.source_type == "poly":
            return plist, splist, wghtslist

    def get_weight_components_and_intesections(
        self,
    ) -> Union[
        Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
        Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
    ]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float],
                    gpd.GeoDataFrame],
                Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.
                5) gdf - GeoDataFrame of intersection geometries

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
                4) gdf - GeoDataFrame of intersection geometries
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            (
                plist,
                ilist,
                jlist,
                wghtslist,
                gdf,
            ) = self.area_tables_binning_and_intersections(
                source_df=self.source_poly,
                target_df=self.target_poly,
                source_type=self.source_type,
            )
        elif self.source_type == "poly":
            (
                plist,
                splist,
                wghtslist,
                gdf,
            ) = self.area_tables_binning_and_intersections(
                source_df=self.source_poly,
                target_df=self.target_poly,
                source_type=self.source_type,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")
        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist, gdf
        elif self.source_type == "poly":
            return plist, splist, wghtslist, gdf

    def area_tables_binning(
        self: "SerialWghtGenEngine",
        source_df: gpd.GeoDataFrame,
        target_df: gpd.GeoDataFrame,
        source_type: SOURCE_TYPES,
    ) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
        """Construct intersection tables.

        Construct area allocation and source-target correspondence tables using
        a parallel spatial indexing approach. This method and its associated functions
        are **based on and adapted** from the Tobbler package:

        Args:
            source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and
                polygons
            target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries
            source_type(SOURCE_TYPES): "grid" or "poly" determines output format.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float]],
                Tuple[List[object], List[object], List[float]]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.
                5) gdf - GeoDataFrame of intersection geometries

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
                4) gdf - GeoDataFrame of intersection geometries
        """
        # Buffer polygons with self-intersections
        print("Validating polygons")
        tstrt = time.perf_counter()
        print("     - validating source polygons")
        df1 = _make_valid(source_df)
        print("     - validating target polygons")
        df2 = _make_valid(target_df)
        tend = time.perf_counter()
        print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

        tstrt = time.perf_counter()
        ids_tgt, ids_src = df1.sindex.query(df2.geometry, predicate="intersects")

        areas = (
            df1.geometry.values[ids_src].intersection(df2.geometry.values[ids_tgt]).area
            / df2.geometry.values[ids_tgt].area
        )
        tend = time.perf_counter()
        print(f"Intersections finished in {tend - tstrt:0.4f} seconds")

        if source_type == "grid":
            return (
                df2[self.target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
                df1.i_index.iloc[ids_src].values.astype(int).tolist(),
                df1.j_index.iloc[ids_src].values.astype(int).tolist(),
                areas.astype(float).tolist(),
            )
        else:
            return (
                df2[self.target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
                df1[self.source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
                areas.astype(float).tolist(),
            )

    def area_tables_binning_and_intersections(
        self: "SerialWghtGenEngine",
        source_df: gpd.GeoDataFrame,
        target_df: gpd.GeoDataFrame,
        source_type: SOURCE_TYPES,
    ) -> Union[
        Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
        Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
    ]:
        """Construct intersection tables.

        Construct area allocation and source-target correspondence tables using
        a parallel spatial indexing approach. This method and its associated functions
        are **based on and adapted** from the Tobbler package:

        Args:
            source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and
                polygons
            target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries
            source_type (SOURCE_TYPES): "grid" or "poly"

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float],
                    gpd.GeoDataFrame],
                Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.
                5) gdf - GeoDataFrame of intersection geometries

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of poly_idx strings.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
                4) gdf - GeoDataFrame of intersection geometries
        """
        # Buffer polygons with self-intersections
        print("Validating polygons")
        tstrt = time.perf_counter()
        print("     - validating source polygons")
        df1 = _make_valid(source_df)
        print("     - validating target polygons")
        df2 = _make_valid(target_df)
        tend = time.perf_counter()
        print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

        tstrt = time.perf_counter()
        ids_tgt, ids_src = df1.sindex.query(df2.geometry, predicate="intersects")
        f_intersect = df1.geometry.values[ids_src].intersection(df2.geometry.values[ids_tgt])
        weights = f_intersect.area / df2.geometry.values[ids_tgt].area
        gdf_inter = df2.iloc[ids_tgt]
        # gdf_inter.set_geometry(f_intersect, inplace=True)
        gdf_inter = gdf_inter.iloc[:].set_geometry(f_intersect)
        gdf_inter["weights"] = weights.astype(float)
        tend = time.perf_counter()
        print(f"Intersections finished in {tend - tstrt:0.4f} seconds")

        if source_type == "grid":
            return (
                df2[self.target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
                df1.i_index.iloc[ids_src].values.astype(int).tolist(),
                df1.j_index.iloc[ids_src].values.astype(int).tolist(),
                weights.astype(float).tolist(),
                gdf_inter,
            )
        elif source_type == "poly":
            return (
                df2[self.target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
                df1[self.source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
                weights.astype(float).tolist(),
                gdf_inter,
            )


class ParallelWghtGenEngine(CalcWeightEngine):
    """Method to generate grid-to-polygon weight using multi-processing.

    This class is based on adapted from methods provided in the Tobler package. See
        _area_tables_binning_parallel() method.

    Args:
        CalcWeightEngine (ABC): Abstract Base Class (ABC) employing the Template behavior
            pattern.  The abstractmethod get weight components provides a method to plug-
            in new weight generation methods.
    """

    def get_weight_components(
        self,
    ) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float]],
                Tuple[List[object], List[object], List[float]]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist: list of target poly ids.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of target poly ids.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            plist, ilist, jlist, wghtslist = _area_tables_binning_parallel(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        elif self.source_type == "poly":
            plist, splist, wghtslist = _area_tables_binning_parallel(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")
        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist
        elif self.source_type == "poly":
            return plist, splist, wghtslist

    def get_weight_components_and_intesections(
        self,
    ) -> Union[
        Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
        Tuple[List[object], list[object], List[float], gpd.GeoDataFrame],
    ]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float],
                    gpd.GeoDataFrame],
                Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
            ]

            if self.source_type == "grid"
            Returned tuples in order:
                1) plist:  list of target poly ids.
                2) ilist i-index of grid_cells.
                3) jlist j-index of grid_cells.
                4) wghtslist weight values of i,j index of grid_cells.
                5) GeoDataFrame of intersection geometries.

            if self.source_type == "poly"
            Returned tuples in order:
                1) plist: list of target poly ids.
                2) splist: list of source poly ids.
                3) wghtslist weight values of source polygons.
                4) GeoDataFrame of intersection geometries.
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            (
                plist,
                ilist,
                jlist,
                wghtslist,
                gdf,
            ) = _area_tables_binning_parallel_and_intersections(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        elif self.source_type == "poly":
            (
                plist,
                splist,
                wghtslist,
                gdf,
            ) = _area_tables_binning_parallel_and_intersections(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")

        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist, gdf
        elif self.source_type == "poly":
            return plist, splist, wghtslist, gdf


def _area_tables_binning_parallel_and_intersections(
    source_df: gpd.GeoDataFrame,
    source_poly_idx: str,
    source_type: SOURCE_TYPES,
    target_df: gpd.GeoDataFrame,
    target_poly_idx: str,
    n_jobs: int = -1,
) -> Union[
    Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
    Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
]:
    """Construct intersection tables using a parallel spatial indexing approach.

    This method and its associated functions are adapted from the Tobler package.
    For licensing details, please refer to the Tobler's BSD 3-Clause License.

    Args:
        source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and polygons.
        source_poly_idx (str): Column name representing the unique ID of source polygons.
        source_type (SOURCE_TYPES): Specifies the type of source, either "grid" or "poly".
        target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries.
        target_poly_idx (str): Column name representing the unique ID of target polygons.
        n_jobs (int): Number of processes for parallel execution. If -1, uses all available CPUs. default = -1.

    Returns:
        Union[
            Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
            Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
        ]:
            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.
    """
    if n_jobs == -1:
        n_jobs = int(os.cpu_count() / 2)  # type: ignore
        logger.info(" ParallelWghtGenEngine getting jobs from os.cpu_count()")
    logger.info(f"  ParallelWghtGenEngine using {n_jobs} jobs")

    # Buffer polygons with self-intersections
    print("Validating polygons")
    tstrt = time.perf_counter()
    print("     - validating source polygons")
    df1 = _make_valid(source_df)
    print("     - validating target polygons")
    df2 = _make_valid(target_df)
    tend = time.perf_counter()
    print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

    # Chunk the largest, ship the smallest in full
    to_chunk, df_full = _get_chunks_for_parallel(df1, df2)

    # Spatial index query: Reindex on positional IDs
    to_workers = _chunk_dfs(
        gpd.GeoSeries(to_chunk.geometry.values, crs=to_chunk.crs),
        gpd.GeoSeries(df_full.geometry.values, crs=df_full.crs),
        n_jobs,
    )

    worker_out = _get_ids_for_parallel(n_jobs, to_workers)
    ids_src, ids_tgt = np.concatenate(worker_out).T

    # Intersection + area calculation
    chunks_to_intersection = _chunk_polys(np.vstack([ids_src, ids_tgt]).T, df1.geometry, df2.geometry, n_jobs)
    worker_out = _get_areas_and_intersections_for_parallel(n_jobs, chunks_to_intersection)
    areas = np.concatenate([item[0] for item in worker_out])
    inter_geom = np.concatenate([item[1] for item in worker_out])

    print("Processing intersections for output.")
    inter_sect = df2.iloc[ids_tgt, :].set_geometry(inter_geom)
    weights = areas.astype(float) / df2.geometry[ids_tgt].area
    inter_sect["weights"] = weights

    if source_type == "grid":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1.i_index.iloc[ids_src].values.astype(int).tolist(),
            df1.j_index.iloc[ids_src].values.astype(int).tolist(),
            weights.tolist(),
            inter_sect,
        )
    elif source_type == "poly":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1[source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
            weights.tolist(),
            inter_sect,
        )


def _get_areas_and_intersections_for_parallel(
    n_jobs: int,
    chunks_to_intersection: Generator[Tuple[npt.ArrayLike, npt.ArrayLike], Any, Any],
) -> Any:
    """Get poly-to-poly intersections."""
    with parallel_backend("loky", inner_max_num_threads=1):
        worker_out = Parallel(n_jobs=n_jobs)(
            delayed(_intersect_area_on_chunk)(*chunk_pair) for chunk_pair in chunks_to_intersection
        )
    return worker_out


def _get_areas_for_parallel(
    n_jobs: int,
    chunks_to_intersection: Generator[Tuple[npt.ArrayLike, npt.ArrayLike], Any, Any],
) -> Any:
    """Get poly-to-poly intersections."""
    with parallel_backend("loky", inner_max_num_threads=1):
        worker_out = Parallel(n_jobs=n_jobs)(
            delayed(_area_on_chunk)(*chunk_pair) for chunk_pair in chunks_to_intersection
        )
    return worker_out


def _get_ids_for_parallel(n_jobs: int, to_workers: Generator[Tuple[gpd.GeoSeries, gpd.GeoSeries], Any, Any]) -> Any:
    """Get poly-to-poly intersection ids."""
    with parallel_backend("loky", inner_max_num_threads=1):
        worker_out = Parallel(n_jobs=n_jobs)(delayed(_index_n_query)(*chunk_pair) for chunk_pair in to_workers)
    return worker_out


def _get_chunks_for_parallel(df1: gpd.GeoDataFrame, df2: gpd.GeoDataFrame) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Chunk dataframes."""
    to_chunk = df1
    df_full = df2
    return to_chunk, df_full


def _area_tables_binning_parallel(
    source_df: gpd.GeoDataFrame,
    source_poly_idx: str,
    source_type: SOURCE_TYPES,
    target_df: gpd.GeoDataFrame,
    target_poly_idx: str,
    n_jobs: int = -1,
) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
    """Construct intersection tables using a parallel spatial indexing approach.

    This method and its associated functions are adapted from the Tobler package.
    For licensing details, please refer to the Tobler's BSD 3-Clause License.

    Args:
        source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and polygons.
        source_poly_idx (str): Column name representing the unique ID of source polygons.
        source_type (SOURCE_TYPES): Specifies the type of source, either "grid" or "poly".
        target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries. default = -1.
        target_poly_idx (str): Column name representing the unique ID of target polygons.
        n_jobs (int): Number of processes for parallel execution. If -1, uses all available CPUs.

    Returns:
        Union[
            Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
            Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
        ]:
            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.
    """
    if n_jobs == -1:
        n_jobs = int(os.cpu_count() / 2)  # type: ignore
        logger.info(" ParallelWghtGenEngine getting jobs from os.cpu_count()")
    logger.info(f"  ParallelWghtGenEngine using {n_jobs} jobs")

    # Buffer polygons with self-intersections
    print("Validating polygons")
    tstrt = time.perf_counter()
    print("     - validating source polygons")
    df1 = _make_valid(source_df)
    print("     - validating target polygons")
    df2 = _make_valid(target_df)
    tend = time.perf_counter()
    print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

    # Chunk the largest, ship the smallest in full
    to_chunk, df_full = _get_chunks_for_parallel(df1, df2)

    # Spatial index query: Reindex on positional IDs
    to_workers = _chunk_dfs(
        gpd.GeoSeries(to_chunk.geometry.values, crs=to_chunk.crs),
        gpd.GeoSeries(df_full.geometry.values, crs=df_full.crs),
        n_jobs,
    )

    worker_out = _get_ids_for_parallel(n_jobs, to_workers)
    ids_src, ids_tgt = np.concatenate(worker_out).T

    # Intersection + area calculation
    chunks_to_intersection = _chunk_polys(np.vstack([ids_src, ids_tgt]).T, df1.geometry, df2.geometry, n_jobs)
    worker_out = _get_areas_for_parallel(n_jobs, chunks_to_intersection)
    areas = np.concatenate(worker_out)

    if source_type == "grid":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1.i_index.iloc[ids_src].values.astype(int).tolist(),
            df1.j_index.iloc[ids_src].values.astype(int).tolist(),
            (areas.astype(float) / df2.geometry[ids_tgt].area).tolist(),
        )
    elif source_type == "poly":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1[source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
            (areas.astype(float) / df2.geometry[ids_tgt].area).tolist(),
        )


class DaskWghtGenEngine(CalcWeightEngine):
    """Method to generate grid-to-polygon weight.

    This class is based on methods provided in the Tobbler package. See
        area_tables_bining_parallel() method.

    Args:
        CalcWeightEngine (ABC): Abstract Base Class (ABC) employing the Template behavior
            pattern.  The abstractmethod get weight components povides a method to plug-
            in new weight generation methods.
    """

    def get_weight_components(
        self,
    ) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float]],
                Tuple[List[object], List[object], List[float]]
            ]

            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            plist, ilist, jlist, wghtslist = _area_tables_binning_for_dask(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        elif self.source_type == "poly":
            plist, splist, wghtslist = _area_tables_binning_for_dask(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")

        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist
        elif self.source_type == "poly":
            return plist, splist, wghtslist

    def get_weight_components_and_intesections(
        self,
    ) -> Union[
        Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
        Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
    ]:
        """Template method from CalcWeightEngine class for generating weight components.

        Returns:
            Union[
                Tuple[List[object], List[int], List[int], List[float],
                    gpd.GeoDataFrame],
                Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
            ]

            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.
        """
        tsrt = time.perf_counter()
        if self.source_type == "grid":
            (
                plist,
                ilist,
                jlist,
                wghtslist,
                gdf,
            ) = _area_tables_binning_and_intersections_for_dask(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        elif self.source_type == "poly":
            (
                plist,
                splist,
                wghtslist,
                gdf,
            ) = _area_tables_binning_and_intersections_for_dask(
                source_df=self.source_poly,
                source_poly_idx=self.source_poly_idx,
                source_type=self.source_type,
                target_df=self.target_poly,
                target_poly_idx=self.target_poly_idx,
                n_jobs=self.jobs,
            )
        tend = time.perf_counter()
        print(f"Weight gen finished in {tend-tsrt:0.4f} seconds")

        if self.source_type == "grid":
            return plist, ilist, jlist, wghtslist, gdf
        elif self.source_type == "poly":
            return plist, splist, wghtslist, gdf


def _area_tables_binning_and_intersections_for_dask(
    source_df: gpd.GeoDataFrame,
    source_poly_idx: str,
    source_type: SOURCE_TYPES,
    target_df: gpd.GeoDataFrame,
    target_poly_idx: str,
    n_jobs: int = -1,
) -> Union[
    Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
    Tuple[List[object], List[object], List[float], gpd.GeoDataFrame],
]:
    """Construct intersection tables using a parallel spatial indexing approach.

    This method and its associated functions are adapted from the Tobler package.
    For licensing details, please refer to the Tobler's BSD 3-Clause License.

    Args:
        source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and polygons.
        source_poly_idx (str): Column name representing the unique ID of source polygons.
        source_type (SOURCE_TYPES): Specifies the type of source, either "grid" or "poly".
        target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries.
        target_poly_idx (str): Column name representing the unique ID of target polygons.
        n_jobs (int): Number of processes for parallel execution.
                                  If -1, uses all available CPUs. default=-1

    Returns:
        Union[
            Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
            Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
        ]:
            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.

    Raises:
        ValueError: If n_jobs == -1. Dask generator requires the Optional jobs parameter to be set.
    """
    if n_jobs == -1:
        raise ValueError(" ")

    # Buffer polygons with self-intersections
    print("Validating polygons")
    tstrt = time.perf_counter()
    print("     - validating source polygons")
    df1 = _make_valid(source_df)
    print("     - validating target polygons")
    df2 = _make_valid(target_df)
    tend = time.perf_counter()
    print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

    # Chunk the largest, ship the smallest in full
    sdf, tdf = _get_chunks_for_dask(n_jobs, df1, df2)
    sdf.calculate_spatial_partitions()

    id_chunks = _ids_for_dask_generator(sdf=sdf, tdf=tdf)
    worker_out = _get_ids_for_dask(id_chunks)
    ids_src, ids_tgt = np.concatenate(worker_out).T

    # Intersection + area calculation
    chunks_to_intersection = _chunk_polys_dask(np.vstack([ids_src, ids_tgt]).T, df1.geometry, df2.geometry, n_jobs)

    worker_out = _get_areas_and_intersections_for_dask(n_jobs, chunks_to_intersection)
    areas = np.concatenate([item[0] for item in worker_out])
    inter_geom = np.concatenate([item[1] for item in worker_out])

    print("Processing intersections for output.")
    inter_sect = df2.iloc[ids_tgt, :].set_geometry(inter_geom)
    weights = areas.astype(float) / df2.geometry[ids_tgt].area
    inter_sect["weights"] = weights

    if source_type == "grid":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1.i_index.iloc[ids_src].values.astype(int).tolist(),
            df1.j_index.iloc[ids_src].values.astype(int).tolist(),
            weights.tolist(),
            inter_sect,
        )
    elif source_type == "poly":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1[source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
            weights.tolist(),
            inter_sect,
        )


def _ids_for_dask_generator(
    sdf: dgpd.GeoDataFrame, tdf: dgpd.GeoDataFrame
) -> Generator[Tuple[gpd.GeoSeries, gpd.GeoSeries], Any, Any]:
    for part in tdf.partitions:
        target_chunk = part.compute()
        bnds = target_chunk.total_bounds
        source_chunk = sdf.cx[bnds[0] : bnds[1], bnds[2] : bnds[3]].compute()
        yield (
            gpd.GeoSeries(
                source_chunk.geometry.values,
                index=source_chunk.index,
                crs=source_chunk.crs,
            ),
            gpd.GeoSeries(
                target_chunk.geometry.values,
                index=target_chunk.index,
                crs=target_chunk.crs,
            ),
        )


def _get_areas_and_intersections_for_dask(
    jobs: int,
    chunks_to_intersection: Generator[Tuple[gpd.GeoSeries, gpd.GeoSeries], Any, Any],
) -> Any:
    """Get poly-to-poly intersections."""
    b = db.from_sequence(chunks_to_intersection, npartitions=jobs)  # type: ignore
    b = b.map(_intersect_area_on_chunk_dask)
    return b.compute()


def _get_areas_for_dask(
    jobs: int,
    chunks_to_intersection: Generator[Tuple[npt.ArrayLike, npt.ArrayLike], Any, Any],
) -> Any:
    """Get poly-to-poly intersections."""
    b = db.from_sequence(chunks_to_intersection, npartitions=jobs)  # type: ignore
    b = b.map(_area_on_chunk_dask)
    return b.compute()


def _get_ids_for_dask(to_workers: Generator[Tuple[gpd.GeoSeries, gpd.GeoSeries], Any, Any]) -> Any:
    """Get poly-to-poly intersection ids."""
    b = db.from_sequence(to_workers)  # type: ignore
    result = b.map(_index_n_query_dask)
    return result.compute()


def _area_tables_binning_for_dask(
    source_df: gpd.GeoDataFrame,
    source_poly_idx: str,
    source_type: SOURCE_TYPES,
    target_df: gpd.GeoDataFrame,
    target_poly_idx: str,
    n_jobs: int = -1,
) -> Union[Tuple[List[object], List[int], List[int], List[float]], Tuple[List[object], List[object], List[float]]]:
    """Construct intersection tables using a parallel spatial indexing approach.

    This method and its associated functions are adapted from the Tobler package.
    For licensing details, please refer to the Tobler's BSD 3-Clause License.

    Args:
        source_df (gpd.GeoDataFrame): GeoDataFrame containing input data and polygons.
        source_poly_idx (str): Column name representing the unique ID of source polygons.
        source_type (SOURCE_TYPES): Specifies the type of source, either "grid" or "poly".
        target_df (gpd.GeoDataFrame): GeoDataFrame defining the output geometries.
        target_poly_idx (str): Column name representing the unique ID of target polygons.
        n_jobs (int): Number of processes for parallel execution.
                                  If -1, uses all available CPUs, default=-1

    Returns:
        Union[
            Tuple[List[object], List[int], List[int], List[float], gpd.GeoDataFrame],
            Tuple[List[object], List[object], List[float], gpd.GeoDataFrame]
        ]:
            - If source_type is "grid", the tuple contains:
                1. plist: List of target polygon IDs.
                2. ilist: i-index of grid cells.
                3. jlist: j-index of grid cells.
                4. wghtslist: Weight values for i,j index of grid cells.
                5. GeoDataFrame of intersection geometries.

            - If source_type is "poly", the tuple contains:
                1. plist: List of target polygon IDs.
                2. splist: List of source polygon IDs.
                3. wghtslist: Weight values of source polygons.
                4. GeoDataFrame of intersection geometries.

    Raises:
        ValueError: If n_jobs == -1. Dask generator requires the Optional jobs parameter to be set.
    """
    if n_jobs == -1:
        raise ValueError(" Dask generator requires the Optional jobs parameter to be set")

    # Buffer polygons with self-intersections
    print("Validating polygons")
    tstrt = time.perf_counter()
    print("     - validating source polygons")
    df1 = _make_valid(source_df)
    print("     - validating target polygons")
    df2 = _make_valid(target_df)
    tend = time.perf_counter()
    print(f"Validate polygons finished in {tend - tstrt:0.4f} seconds")

    # Chunk the largest, ship the smallest in full
    sdf, tdf = _get_chunks_for_dask(n_jobs, df1, df2)
    sdf.calculate_spatial_partitions()

    id_chunks = _ids_for_dask_generator(sdf=sdf, tdf=tdf)
    worker_out = _get_ids_for_dask(id_chunks)
    ids_src, ids_tgt = np.concatenate(worker_out).T

    # Intersection + area calculation
    chunks_to_intersection = _chunk_polys_dask(np.vstack([ids_src, ids_tgt]).T, df1.geometry, df2.geometry, n_jobs)

    worker_out = _get_areas_for_dask(n_jobs, chunks_to_intersection)
    areas = np.concatenate(worker_out)
    if source_type == "grid":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1.i_index.iloc[ids_src].values.astype(int).tolist(),
            df1.j_index.iloc[ids_src].values.astype(int).tolist(),
            (areas.astype(float) / df2.geometry[ids_tgt].area).tolist(),
        )
    elif source_type == "poly":
        return (
            df2[target_poly_idx].iloc[ids_tgt].values.astype(object).tolist(),
            df1[source_poly_idx[0]].iloc[ids_src].values.astype(object).tolist(),
            (areas.astype(float) / df2.geometry[ids_tgt].area).tolist(),
        )


def _get_chunks_for_dask(
    jobs: int, source_df: gpd.GeoDataFrame, target_df: gpd.GeoDataFrame
) -> Tuple[dgpd.GeoDataFrame, dgpd.GeoDataFrame]:
    """Chunk dataframes."""
    return (
        dgpd.from_geopandas(source_df, npartitions=jobs),
        dgpd.from_geopandas(target_df, npartitions=jobs),
    )


def _chunk_dfs(
    geoms_to_chunk: gpd.GeoSeries, geoms_full: gpd.GeoSeries, n_jobs: int
) -> Generator[Tuple[gpd.GeoSeries, gpd.GeoSeries], Any, Any]:
    """Chunk dataframes for parallel processing."""
    chunk_size = geoms_to_chunk.shape[0] // n_jobs + 1
    for i in range(n_jobs):
        start = i * chunk_size
        yield geoms_to_chunk.iloc[start : start + chunk_size], geoms_full


def _index_n_query(geoms1: gpd.GeoSeries, geoms2: gpd.GeoSeries) -> npt.ArrayLike:
    """Get geom ids for parallel processing."""
    # Pick largest for STRTree, query the smallest

    # Build tree + query
    qry_polyids, tree_polyids = geoms1.sindex.query(geoms2, predicate="intersects")
    # Remap IDs to global
    large_global_ids = geoms1.iloc[tree_polyids].index.values
    small_global_ids = geoms2.iloc[qry_polyids].index.values

    return np.array([large_global_ids, small_global_ids]).T


def _index_n_query_dask(bag: Tuple[gpd.GeoSeries, gpd.GeoSeries]) -> npt.ArrayLike:
    """Get geom ids for parallel processing."""
    # Build tree + query
    source_df = bag[0]
    target_df = bag[1]
    qry_polyids, tree_polyids = source_df.sindex.query(target_df, predicate="intersects")
    # Remap IDs to global
    large_global_ids = source_df.iloc[tree_polyids].index.values
    small_global_ids = target_df.iloc[qry_polyids].index.values

    return np.array([large_global_ids, small_global_ids]).T


def _chunk_polys(
    id_pairs: npt.NDArray[np.int_],
    geoms_left: gpd.GeoSeries,
    geoms_right: gpd.GeoSeries,
    n_jobs: int,
) -> Generator[Tuple[npt.ArrayLike, npt.ArrayLike], Any, Any]:
    """Chunk polys for parallel processing."""
    chunk_size = id_pairs.shape[0] // n_jobs + 1
    for i in range(n_jobs):
        start = i * chunk_size
        chunk1 = np.asarray(geoms_left.values[id_pairs[start : start + chunk_size, 0]])
        chunk2 = np.asarray(geoms_right.values[id_pairs[start : start + chunk_size, 1]])
        yield chunk1, chunk2


def _chunk_polys_dask(
    id_pairs: npt.NDArray[np.int_],
    geoms_left: gpd.GeoSeries,
    geoms_right: gpd.GeoSeries,
    n_jobs: int,
) -> Generator[Tuple[npt.ArrayLike, npt.ArrayLike], Any, Any]:
    """Chunk polys for parallel processing."""
    chunk_size = id_pairs.shape[0] // n_jobs + 1
    for i in range(n_jobs):
        start = i * chunk_size
        chunk1 = np.asarray(geoms_left.values[id_pairs[start : start + chunk_size, 0]])
        chunk2 = np.asarray(geoms_right.values[id_pairs[start : start + chunk_size, 1]])
        yield (chunk1, chunk2)


def _intersect_area_on_chunk(geoms1: npt.ArrayLike, geoms2: npt.ArrayLike) -> Tuple[gpd.GeoSeries, gpd.GeoSeries]:
    """Get intersection areas."""
    f_intersect = intersection(geoms1, geoms2)
    return area(f_intersect), f_intersect


def _area_on_chunk(geoms1: gpd.GeoSeries, geoms2: gpd.GeoSeries) -> gpd.GeoSeries:
    """Get intersection areas."""
    return area(intersection(geoms1, geoms2))


def _area_on_chunk_dask(dask_bag: Tuple[npt.ArrayLike, npt.ArrayLike]) -> gpd.GeoSeries:
    """Get intersection areas."""
    geoms1 = dask_bag[0]
    geoms2 = dask_bag[1]
    return area(intersection(geoms1, geoms2))


def _intersect_area_on_chunk_dask(dask_bag: Tuple[npt.ArrayLike, npt.ArrayLike]) -> gpd.GeoSeries:
    """Get intersection areas."""
    geoms1 = dask_bag[0]
    geoms2 = dask_bag[1]
    f_intersect = intersection(geoms1, geoms2)
    return area(f_intersect), f_intersect


def _make_valid(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Convert invalid geometries in a GeoDataFrame to valid ones.

    This function checks for invalid geometries in the provided GeoDataFrame.
    For invalid geometries, it uses the buffer trick (buffering by a distance of 0)
    to attempt to convert them into valid geometries. This approach is based on
    the method in Shapely and has been adapted for this specific use case.

    Note: It's recommended to use this function with caution, as the buffer trick
    might not always produce the desired results for all types of invalid geometries.

    Adapted from Shapely:
    Copyright (c) 2007, Sean C. Gillies. 2019, Casper van der Wel. 2007-2022,
    Shapely Contributors. All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    Args:
        df (gpd.GeoDataFrame): A GeoDataFrame containing the geometries to be validated.

    Returns:
        gpd.GeoDataFrame: A GeoDataFrame with invalid geometries made valid. If no
                          invalid geometries are found, the original GeoDataFrame
                          is returned unchanged.
    """
    polys = ["Polygon", "MultiPolygon"]
    if df.geom_type.isin(polys).all():
        mask = ~df.geometry.is_valid
        print(f"     - fixing {len(mask[mask == True])} invalid polygons.")
        col = df._geometry_column_name
        df.loc[mask, col] = df.loc[mask, col].buffer(0)
    return df
