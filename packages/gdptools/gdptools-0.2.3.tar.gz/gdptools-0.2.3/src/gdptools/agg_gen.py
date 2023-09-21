"""Calculate aggregation methods."""
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

import geopandas as gpd
import numpy as np
import numpy.typing as npt
import pandas as pd
import xarray as xr

from gdptools.agg.agg_data_writers import CSVWriter
from gdptools.agg.agg_data_writers import JSONWriter
from gdptools.agg.agg_data_writers import NetCDFWriter
from gdptools.agg.agg_data_writers import ParquetWriter
from gdptools.agg.agg_engines import DaskAgg
from gdptools.agg.agg_engines import DaskInterp
from gdptools.agg.agg_engines import ParallelAgg
from gdptools.agg.agg_engines import ParallelInterp
from gdptools.agg.agg_engines import SerialAgg
from gdptools.agg.agg_engines import SerialInterp
from gdptools.agg.agg_engines import STAT_TYPES
from gdptools.agg.stats_methods import Count
from gdptools.agg.stats_methods import MACount
from gdptools.agg.stats_methods import MAMax
from gdptools.agg.stats_methods import MAMin
from gdptools.agg.stats_methods import MAWeightedMean
from gdptools.agg.stats_methods import MAWeightedMedian
from gdptools.agg.stats_methods import MAWeightedStd
from gdptools.agg.stats_methods import Max
from gdptools.agg.stats_methods import Min
from gdptools.agg.stats_methods import WeightedMean
from gdptools.agg.stats_methods import WeightedMedian
from gdptools.agg.stats_methods import WeightedStd
from gdptools.data.agg_gen_data import AggData
from gdptools.data.user_data import ODAPCatData
from gdptools.data.user_data import UserCatData
from gdptools.data.user_data import UserData

# write a docstring for STATSMETHODS below

STATSMETHODS = Literal[
    "masked_mean",
    "mean",
    "masked_std",
    "std",
    "masked_median",
    "median",
    "masked_count",
    "count",
    "masked_min",
    "min",
    "masked_max",
    "max",
]
""" List of available aggregation methods.

    Masked methods below account for missing values in the gridded data standard methods
        do not. If there is a missing value in the gridded data then the standard
        methods will return a nan for that polygon.

    Args:
        masked_mean: masked mean of the data.
        mean: mean of the data.

        masked_std: masked standard deviation of the data.
        std: standard deviation of the data.

        masked_median: masked median of the data.
        median: median of the data.

        masked_count: masked count of the data.
        count: count of the data.

        masked_min: masked minimum of the data.
        min: minimum of the data.

        masked_max: masked maximum of the data.
        max: maximum of the data.

    Raises:
        TypeError: If supplied attribute is not one of STATSMETHODS.

    Returns:
        _type_: str
"""

AGGENGINES = Literal["serial", "parallel", "dask"]
""" List of aggregation methods.


Args:
    serial: performes weighted-area aggregation by iterating through polygons.
    parallel: performes weighted-area aggregation by number of jobs.
    dask: performs weighted-area aggregation in the presence of a dask client, the
        number of jobs should be specified.

Raises:
    TypeError: If supplied attribute is not one of AGGENGINES.

Returns:
    _type_: str
"""

AGGWRITERS = Literal["none", "csv", "parquet", "netcdf", "json"]
""" List of available writers applied to the aggregation.

Args:
    none: Output not written to a file.
    csv: Output data in csv format.
    parquet: Output data to parquet.gzip file.
    netcdf: Output data in netcdf format.
    json: Output data as json.

Raises:
    TypeError: If supplied attribute is not one of AGGWRITERS.

Returns:
    _type_: str
"""

WRITER_TYPES = Union[
    Type[None],
    Type[CSVWriter],
    Type[ParquetWriter],
    Type[NetCDFWriter],
    Type[JSONWriter],
]

AGG_ENGINE_TYPES = Union[Type[SerialAgg], Type[ParallelAgg], Type[DaskAgg]]


class AggGen:
    """Class for aggregating grid-to-polygons."""

    def __init__(
        self,
        user_data: UserData,
        stat_method: STATSMETHODS,
        agg_engine: AGGENGINES,
        agg_writer: AGGWRITERS,
        weights: Union[str, pd.DataFrame],
        out_path: Optional[Union[str, None]] = None,
        file_prefix: Optional[Union[str, None]] = None,
        append_date: Optional[bool] = False,
        jobs: Optional[int] = -1,
    ) -> None:
        """__init__ Initalize AggGen.

        AggGen is a class for aggregating gridded datasets to polygons using area-
        weighted statistics.  The class is initialized with a user_data object, a
        stat_method, an agg_engine, an agg_writer, and a weights object. Once the class
        is initialized the user can call the :meth:`AggGen.calculate_agg` method to
        perform the aggregation over the period defined in the user-data parameter.

        The user_data object is  one of the catalog data object:(:class:`ODAPCatData`,
        :class:`ClimateCatData`) or a :class:`UserCatData` object which requires some
        additional information that would otherwise be provided by the catalog data
        objects, such as the name of the coordinates and projection.

        The stat_method is one of the :data:`STATSMETHODS` which are either masked or
        standard methods.  If one contributing grid cell that is being interpolated to a
        polygon is missing then that statistic will return a missing value. Using the
        masked statistic will eturn the value of all the non-missing cells.

        The agg_engine is one of the :data:`AGGENGINES`.

        The  agg_writer is one of the :data:`AGGWRITERS`.

        The weights object is either a path to a csv file containing weights or a pandas
        dataframe containing weights.

        The out_path, file_prefix, and append date are optional parameters for for
        writting the weights to a csv file.

        The jobs parameter is optional, and used for both the parallel and dask engines.
        If the jobs parameter is not specified then half the number of processors on the
        machine will be used.

        Args:
            user_data (UserData): One of :class:`UserCatData`, :class:`ODAPCatData`,
                :class:`ClimateCatData`
            stat_method (STATSMETHODS): One of :data:`STATSMETHODS`.
            agg_engine (AGGENGINES): One of :data:`AGGENGINES`.
            agg_writer (AGGWRITERS): One of :data:`AGGWRITERS`.
            weights (Union[str, pd.DataFrame]): Either a path to a csv file containing
                weights or a pandas dataframe containing weights.
            out_path (Optional[Union[str, None]], optional): Optional path to output
                file as a string or None. Defaults to None.
            file_prefix (Optional[Union[str, None]], optional): Optional string as
                prefix to fine name or None if not generating outputfile. Defaults to
                None.
            append_date (Optional[bool], optional): Optional, True will append
                processing date to file name. Defaults to False.
            jobs (Optional[int], optional): Optional, number of processors used in
                parallel or dask methods (dask uses dask bag). If set to default value
                (-1) jobs is defined as the number of processors available/2.
                In this case, because the data needs to be distributed amoung processors
                choosing half the processors available is a reasonable choice. Defaults
                to -1.
        """
        self._user_data = user_data
        self._stat_method = stat_method
        self._agg_engine = agg_engine
        self._agg_writer = agg_writer
        self._weights = weights
        self._out_path = out_path
        self._file_prefix = file_prefix
        self._append_date = append_date
        self._jobs: int = jobs
        self._agg_data: Dict[str, AggData]
        self._set_stats_method()
        self._set_agg_engine()
        self._set_writer()

    def _set_writer(self):
        if self._agg_writer != "none" and ((self._out_path is None) or (self._file_prefix is None)):
            raise ValueError(
                f"If agg_writer not none, then out_path: {self._out_path}"
                f" and file_prefix: {self._file_prefix} must be set."
            )
        self.__writer: WRITER_TYPES

        if self._agg_writer == "none":
            self.__writer = None
        else:
            writers = {
                "csv": CSVWriter,
                "parquet": ParquetWriter,
                "netcdf": NetCDFWriter,
                "json": JSONWriter,
            }
            try:
                self.__writer = writers[self._agg_writer]
            except Exception as exc:
                raise TypeError(f"agg_writer: {self._agg_writer} not in {AGGWRITERS}") from exc

    def _set_agg_engine(self):
        self.agg: AGG_ENGINE_TYPES

        engines = {"serial": SerialAgg, "parallel": ParallelAgg, "dask": DaskAgg}
        try:
            self.agg = engines[self._agg_engine]
        except Exception as exc:
            raise TypeError(f"agg_engine: {self._agg_engine} not in {AGGENGINES}") from exc

    def _set_stats_method(self):
        self._stat: STAT_TYPES

        methods = {
            "masked_mean": MAWeightedMean,
            "masked_std": MAWeightedStd,
            "masked_median": MAWeightedMedian,
            "masked_count": MACount,
            "masked_min": MAMin,
            "masked_max": MAMax,
            "mean": WeightedMean,
            "std": WeightedStd,
            "median": WeightedMedian,
            "count": Count,
            "min": Min,
            "max": Max,
        }
        try:
            self._stat = methods[self._stat_method]
        except Exception as exc:
            raise TypeError(f"stat_method: {self._stat_method} not in {STATSMETHODS}") from exc

    def calculate_agg(
        self,
    ) -> Tuple[gpd.GeoDataFrame, xr.Dataset]:
        """Calculate aggregations.

        Returns:
            Tuple[gpd.GeoDataFrame, xr.Dataset]: _description_
        """
        self._agg_data, new_gdf, agg_vals = self.agg().calc_agg_from_dictmeta(
            user_data=self._user_data,
            weights=self._weights,
            stat=self._stat,
            jobs=self._jobs,
        )
        if self._agg_writer != "none":
            self.__writer().save_file(
                agg_data=self._agg_data,
                feature=new_gdf,
                vals=agg_vals,
                p_out=self._out_path,
                file_prefix=self._file_prefix,
                append_date=self._append_date,
            )

        return new_gdf, self._gen_xarray_return(feature=new_gdf, vals=agg_vals)

    @property
    def agg_data(self) -> dict[str, AggData]:
        """Return agg_data."""
        return self._agg_data

    def _gen_xarray_return(
        self,
        feature: gpd.GeoDataFrame,
        vals: List[npt.NDArray[Union[np.int_, np.double]]],
    ) -> xr.Dataset:
        """Generate xarray return."""
        dataset = []
        for idx, (_key, value) in enumerate(self._agg_data.items()):
            gdf = feature
            gdf_idx = value.id_feature
            # param_values = list(self.agg_data[idx].param_dict.values())[idx]
            param_values = value.cat_param
            t_coord = param_values.T_name
            v_units = param_values.units
            v_varname = param_values.varname
            v_long_name = param_values.long_name
            time = value.da.coords[t_coord].values
            # locs = gdf.index.values
            locs = gdf[gdf_idx].values

            dsn = xr.Dataset(
                data_vars={
                    v_varname: (
                        ["time", gdf_idx],
                        vals[idx],
                        dict(
                            units=v_units,
                            long_name=v_long_name,
                            coordinates="time",
                        ),
                    ),
                },
                coords={
                    "time": time,
                    gdf_idx: ([gdf_idx], locs, {"feature_id": gdf_idx}),
                },
            )
            dataset.append(dsn)
        if len(dataset) > 1:
            ds = xr.merge(dataset)
        else:
            ds = dsn
        fdate = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        ds.attrs = {
            "Conventions": "CF-1.8",
            "featureType": "timeSeries",
            "history": (
                f"{fdate} Original filec created  by gdptools package: "
                "https://code.usgs.gov/wma/nhgf/toolsteam/gdptools \n"
            ),
        }
        return ds


class InterpGen:
    """Class for calculating grid statistics for a polyline geometry."""

    def __init__(
        self,
        user_data: Union[ODAPCatData, UserCatData],
        *,
        pt_spacing: Union[float, int, None] = 50,
        stat: str = "all",
        interp_method: str = "linear",
        mask_data: Union[bool, None] = False,
        output_file: Union[str, None] = None,
        calc_crs: Any = 6931,
        method: str = "Serial",
        jobs: Optional[int] = -1,
    ) -> None:
        """Initiate InterpGen Class.

        Args:
            user_data (ODAPCatData or UserCatData): Data Class for input data
            pt_spacing (float): Optional; Numerical value in meters for the spacing of the
                interpolated sample points (default is 50)
            stat (str): Optional; A string indicating which statistics to calculate during
                the query. Options: 'all', 'mean', 'median', 'std', 'max', 'min'
                (default is 'all')
            interp_method (str): Optional; String indicating the xarray interpolation method.
                Default method in 'linear'. Options: "linear", "nearest", "zero", "slinear",
                "quadratic", "cubic", "polynomial".
            mask_data (bool or None): Optional; When True, nodata values are removed from
                statistical calculations.
            output_file (str or None): Optional; When a file path is specified, a CSV of
                the statistics will be written to that file path. Must end with .csv
                file ending.
            calc_crs (Any): Optional; OGC WKT string, Proj.4 string or int EPSG code.
                Determines which projection is used for the area weighted calculations
                of the line buffer geometry. (default is 6933)
            method (str): Optional; Indicates which methodology to preform the query (currently,
                only the Serial method is available, default is 'Serial')
            jobs (Optional[int], optional): Optional, number of processors used in
                parallel or dask methods (dask uses dask bag). If set to default value
                (-1) jobs is defined as the number of processors available/2.
                In this case, because the data needs to be distributed amoung processors
                choosing half the processors available is a reasonable choice. Defaults
                to -1.
        """
        self._user_data = user_data
        self._line = user_data.f_feature
        self._pt_spacing = pt_spacing
        self._stat = stat
        self._interp_method = interp_method
        self._mask_data = mask_data
        self._output_file = output_file
        self._calc_crs = calc_crs
        self._method = method
        self._jobs = jobs

    def calc_interp(
        self,
    ) -> Union[Tuple[pd.DataFrame, gpd.GeoDataFrame], pd.DataFrame]:  # noqa: DAR401
        """calc_interp Run the interpolation and stat calculations.

        _extended_summary_

        Returns:
            _type_: _description_
        """
        if self._method == "Serial":
            self._interp_data, stats, pts = SerialInterp().run(
                user_data=self._user_data,
                pt_spacing=self._pt_spacing,
                stat=self._stat,
                interp_method=self._interp_method,
                calc_crs=self._calc_crs,
                mask_data=self._mask_data,
                output_file=self._output_file,
            )
            return stats, pts

        if self._method == "Parallel":
            self._interp_data, stats, pts = ParallelInterp().run(
                user_data=self._user_data,
                pt_spacing=self._pt_spacing,
                stat=self._stat,
                interp_method=self._interp_method,
                calc_crs=self._calc_crs,
                mask_data=self._mask_data,
                output_file=self._output_file,
            )
            return stats, pts

        if self._method == "Dask":
            self._interp_data, stats, pts = DaskInterp().run(
                user_data=self._user_data,
                pt_spacing=self._pt_spacing,
                stat=self._stat,
                interp_method=self._interp_method,
                calc_crs=self._calc_crs,
                mask_data=self._mask_data,
                output_file=self._output_file,
            )
            return stats, pts
