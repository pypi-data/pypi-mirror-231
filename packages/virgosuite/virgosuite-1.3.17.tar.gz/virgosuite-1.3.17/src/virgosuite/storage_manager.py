# TODO: choose a license

"""
    The choice was to use Dask and Xarray as a backend for managing data. 
    The user will be free to load, save, operate and convert from/to any supported
    format.
    Supported formats will be SFDB09, ZARR, HDF5, ZIP(?)
"""

# NUMPY
import numpy
from numpy.typing import NDArray, ArrayLike

# DASK
import dask.array
import dask.dataframe
from dask.delayed import delayed

# ASTROPY
import astropy.time

# POLARS
import polars

# PANDAS
import pandas

# XARRAY
import xarray

# STANDARD MODULES
from typing import TextIO

from fnmatch import fnmatch
import dataclasses
from itertools import groupby
import mmap
import os

from time import time

import warnings

from .global_settings import storage_settings

# =============================================================================
# *****************************************************************************
# =============================================================================


@dataclasses.dataclass
class TimeIndependentHeader:
    # voglio dividere gli argomenti unici da quelli time-dependant
    # inserisco anche termini di consistency
    # vedere study_of_header.ipynb per la distinzione tra indipendenti e dipendenti
    # time_independant_args
    count: list[numpy.float64]
    detector: list[numpy.int32]
    fft_lenght: list[numpy.float64]
    starting_fft_sample_index: list[numpy.int32]
    unilateral_number_of_samples: list[numpy.int32]
    reduction_factor: list[numpy.int32]
    fft_interlaced: list[numpy.int32]
    scaling_factor: list[numpy.float32]
    window_type: list[numpy.int32]
    normalization_factor: list[numpy.float32]
    window_normalization: list[numpy.float32]
    starting_fft_frequency: list[numpy.float64]
    subsampling_time: list[numpy.float64]
    frequency_resolution: list[numpy.float64]
    sat_howmany: list[numpy.float64]
    spare_1: list[numpy.float64]
    spare_2: list[numpy.float64]
    spare_3: list[numpy.float64]
    spare_5: list[numpy.float32]
    spare_6: list[numpy.float32]
    lenght_of_averaged_time_spectrum: list[numpy.int32]
    scientific_segment: list[numpy.int32]
    spare_9: list[numpy.int32]

    detector_name: str = dataclasses.field(init=False)
    window_normalization_name: str = dataclasses.field(init=False)
    fft_interlaced_name: str = dataclasses.field(init=False)
    samples_per_hertz: numpy.int32 = dataclasses.field(init=False)

    def __post_init__(self):
        # Creating human-readable attributes
        self.detector_name = storage_settings.DETECTOR[self.detector]
        self.window_normalization_name = storage_settings.WINDOW_NAME[self.window_type]
        self.fft_interlaced_name = storage_settings.INTERLACED_METHOD[
            self.fft_interlaced
        ]

        # DOCUMENT THIS: THIS NEEDS A DEEP EXPLANATION
        sampling_rate = 1 / self.subsampling_time
        nyquist = sampling_rate / 2
        coherence_time = 1 / self.frequency_resolution
        self.samples_per_hertz = int(((coherence_time * sampling_rate) / 2) / nyquist)

        # Consistency check
        assert coherence_time == self.fft_lenght, f"Coherence time is inconsistent"
        assert (
            int(coherence_time * sampling_rate / 2) == self.unilateral_number_of_samples
        ), f"Number of samples is inconsistent"

    @property
    def attributes(self):
        self.time_ind_args.extend(
            [
                "detector_name",
                "window_normalization_name",
                "fft_interlaced_name",
                "samples_per_hertz",
            ]
        )
        return {key: getattr(self, key) for key in self.time_ind_args}


# =============================================================================
# *****************************************************************************
# =============================================================================


def memmap_to_array(filename, dtype):
    assert os.path.exists(filename)
    assert os.stat(filename).st_size != 0  # Check if file is not empty

    with open(filename, "r") as file:
        # `mmap` duplicates the file descriptor
        # `0` means map the full file
        # RECUPERARE URL
        memory_mapping = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

    # coerce to NumPy array of expected type and shape
    memory_mapped_array = numpy.asarray(memory_mapping).view(dtype)

    return memory_mapped_array


def load_specific_data(
    file_name_list: list[str], sfdb_dtype: numpy.dtype, data_name: str
):
    collection_of_extracted_data = {}

    for i, file_name in enumerate(file_name_list):
        memmaped_arr = memmap_to_array(file_name, sfdb_dtype)[data_name]
        delayed_arr = dask.array.from_array(memmaped_arr, asarray=False, name=False)
        collection_of_extracted_data[i] = delayed_arr

    extracted_data_list = dask.array.concatenate(
        [file for file in collection_of_extracted_data.values()], axis=0
    )
    return extracted_data_list


# =============================================================================


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def create_file_name_list(
    path: str | list[str], file_type: str = "SFDB09", verbose: int = 0
):
    file_name_list = []
    if isinstance(path, str) and os.path.isdir(path):
        if verbose > 0:
            print(f"\nLooking for .SFDB09 files inside {path}")
        for path, subdirs, files in os.walk(path):
            for name in files:
                if fnmatch(name, "*." + file_type):
                    file_name_list.append(os.path.join(path, name))

    elif isinstance(path, str) and os.path.isfile(path):
        if verbose > 0:
            print(f"\nLooking for {path}")
        file_name_list = [path]
    elif isinstance(path, list):
        file_name_list = path
    else:
        raise ImportError(f"Given path is not a file nor a folder")

    assert len(file_name_list) > 0, f"Given path does not contain any SFDB09 file"
    for file_name in file_name_list:
        assert os.path.exists(file_name), f"{file_name} does not exist"
        assert os.path.isfile(file_name), f"{file_name} is not a file"

    if verbose > 0:
        print(f"{len(file_name_list)} file(s) found")

    return file_name_list


def load_first_headers(file_name_list: list[str], dtype: numpy.dtype):
    header_list = []
    for file_name in file_name_list:
        with open(file_name) as file:
            sfdb_scan = numpy.fromfile(file, dtype=dtype, count=1).copy()
        header_list.append(sfdb_scan)

    first_header_database = numpy.concatenate(header_list, axis=0)

    # the list of first headers should be very lightweight, 1 chunck should be enough
    return first_header_database


# =============================================================================
#                             EXTRACTING FUNCTIONS
# =============================================================================


def extract_periodogram_shape(
    lenght_of_averaged_time_spectrum: numpy.int32, reduction_factor: numpy.int32
):
    # DOCUMENT THIS!
    if lenght_of_averaged_time_spectrum > 0:
        return lenght_of_averaged_time_spectrum
    else:
        return reduction_factor


def extract_arSpectrum_shape(
    lenght_of_averaged_time_spectrum: numpy.int32,
    unilateral_number_of_samples: numpy.int32,
    reduction_factor: numpy.int32,
):
    # DOCUMENT THIS!
    if lenght_of_averaged_time_spectrum > 0:
        return lenght_of_averaged_time_spectrum
    else:
        return int(unilateral_number_of_samples / reduction_factor)


def exctract_human_readable_time(_gps_time):
    gps_time = astropy.time.Time(
        _gps_time,
        format="gps",
        scale="utc",
    )

    iso_time_values = polars.Series("time", gps_time.iso)
    datetimes = iso_time_values.str.to_datetime()
    return datetimes


def parse_sfdb_file_name(file_name: str, separator: str = "_"):
    return file_name.split(separator)


def extract_date_from_file_name(files: str | tuple[str]):
    out_time_list = []
    if isinstance(files, str):
        files = [files]

    elif (not isinstance(files, list)) and (not isinstance(files, str)):
        raise ValueError(f"Input is not string nor list of strings")

    for i, file_name in enumerate(files):
        parsed_file_name = parse_sfdb_file_name(file_name)
        custom_fmt_date_time = parsed_file_name[-2]
        # date_time = astropy.time.Time.strptime(custom_fmt_date_time, "%Y%m%d")
        date_time = pandas.to_datetime(custom_fmt_date_time)
        out_time_list.append(date_time)

    return out_time_list


def select_files_in_time_range(path, start_time, end_time):
    file_list = create_file_name_list(
        path,
    )
    starting_time_of_provided_files = extract_date_from_file_name(file_list)

    # converting to numpy array for clearer coding
    time_in_files_name = numpy.array(starting_time_of_provided_files)

    # Selecting files within the provided time interval
    start_time = pandas.to_datetime(start_time)
    end_time = pandas.to_datetime(end_time)

    # In case start and and time are reversed, they will be switched. A warning will be raised
    if start_time > end_time:
        tmp = end_time
        end_time = start_time
        start_time = tmp
        warnings.warn("Starting and ending time have been switched out!")
    mask = numpy.logical_and(
        time_in_files_name > start_time, time_in_files_name < end_time
    )
    parsed_file_list = numpy.array(file_list)[mask].tolist()

    assert len(parsed_file_list) > 0, f"No data in given interval"

    return parsed_file_list


# =============================================================================


def scan_sfdb09(
    file_name: str | list[str],
    verbose: int = 0,
    start_time: str = "2000-01-01",
    end_time: str = "2200-01-01",
) -> list:
    # DOCUMENT THIS

    # This does consistency checks and select subset of files in time intervall
    file_list = select_files_in_time_range(file_name, start_time, end_time)

    # FILE LIST IS NOT TIME-ORDERED

    # Checking if datasets of different shapes were loaded
    # In case process is aborted
    if verbose > 2:
        print("Opening first header to check consistency...")
    first_headers_arr = load_first_headers(file_list, storage_settings.HEADER_DTYPE)
    first_headers_database = polars.DataFrame(first_headers_arr)
    ti_first_headers_db = first_headers_database[
        storage_settings.TIME_INDEPENDANT_ATTRIBUTES
    ]

    for attribute in storage_settings.TIME_INDEPENDANT_ATTRIBUTES:
        assert all_equal(ti_first_headers_db[attribute]), f"{attribute} is not unique"

    ti_first_headers = TimeIndependentHeader(
        **ti_first_headers_db[0].to_struct("ind_header_attributes")[0]
    )

    # REODERING FILE LIST
    time_ord_idx = numpy.argsort(
        first_headers_database["gps_seconds"]
        + first_headers_database["gps_nanoseconds"] * 1e9
    )
    time_ordered_file_list = numpy.array(file_list)[time_ord_idx]

    periodogram_shape = extract_periodogram_shape(
        ti_first_headers.lenght_of_averaged_time_spectrum,
        ti_first_headers.reduction_factor,
    )
    ar_spectrum_shape = extract_arSpectrum_shape(
        ti_first_headers.lenght_of_averaged_time_spectrum,
        ti_first_headers.unilateral_number_of_samples,
        ti_first_headers.reduction_factor,
    )
    spectrum_shape = ti_first_headers.unilateral_number_of_samples

    # Creating a custom dtype to read sfdb files
    sfdb_dtype = numpy.dtype(
        [
            ("header", storage_settings.HEADER_ELEMENTS),
            ("periodogram", "float32", periodogram_shape),
            ("ar_spectrum", "float32", ar_spectrum_shape),
            ("fft_spectrum", "complex64", spectrum_shape),
        ]
    )

    header_database = load_specific_data(
        time_ordered_file_list,
        sfdb_dtype,
        "header",
    )
    periodogram_database = load_specific_data(
        time_ordered_file_list,
        sfdb_dtype,
        "periodogram",
    )
    ar_spectrum_database = load_specific_data(
        time_ordered_file_list,
        sfdb_dtype,
        "ar_spectrum",
    )
    fft_spectrum_database = load_specific_data(
        time_ordered_file_list,
        sfdb_dtype,
        "fft_spectrum",
    )

    # ============================ HEADER =====================================
    # We want the header to be immediately computed, so that the resulting dataset
    # has all the useful informations.

    header_pia = polars.DataFrame(header_database.compute())
    independent_attributes = header_pia[storage_settings.TIME_INDEPENDANT_ATTRIBUTES]
    time_independent_header = TimeIndependentHeader(
        **independent_attributes[0].to_struct("header")[0]
    )

    # Other objects can be lazy
    # ======================= REGRESSIVE STUFF ================================

    periodogram_frequency_index = dask.array.arange(
        0, periodogram_database.shape[1], 1, dtype="int32"
    )
    periodogram_frequencies = (
        periodogram_frequency_index
        * time_independent_header.frequency_resolution
        * time_independent_header.reduction_factor
    )

    # ============================= SPECTRUM ==================================
    # Extracting frequency information from sfdb
    spectrum_frequency_index = dask.array.arange(
        0, fft_spectrum_database.shape[1], 1, dtype="int32"
    )
    spectrum_frequencies = (
        time_independent_header.frequency_resolution * spectrum_frequency_index
    )

    time_chunk_size = 512  # TODO: depends on tfft, * tfft / 86400 days
    frequency_chunk_size = 8 * time_independent_header.samples_per_hertz  # ~10Hz
    rechunked_spectrum = fft_spectrum_database.rechunk(
        (time_chunk_size, frequency_chunk_size)
    )

    rechunked_periodogram = periodogram_database.rechunk("auto")
    rechunked_ar_spectrum = ar_spectrum_database.rechunk("auto")

    normalized_rechunked_spectrum = (
        rechunked_spectrum * time_independent_header.scaling_factor
    )
    normalized_rechunked_periodogram = (
        rechunked_periodogram * time_independent_header.scaling_factor
    )
    normalized_rechunked_ar_spectrum = (
        rechunked_ar_spectrum * time_independent_header.scaling_factor
    )

    # Extracting human readable time from header
    gps_time = header_pia["gps_seconds"] + header_pia["gps_nanoseconds"] * 1e-9
    datetimes = exctract_human_readable_time(gps_time)

    time_independant_attributes = dataclasses.asdict(time_independent_header)
    ti_attributes_df = polars.DataFrame(time_independant_attributes)

    # Saving to Xarray and Datasets
    coordinates_names = ["frequency", "time"]
    spectrum_coords = [spectrum_frequencies, datetimes]
    regressive_coords = [periodogram_frequencies, datetimes]
    spectrum = xarray.DataArray(
        data=normalized_rechunked_spectrum.transpose(),
        dims=coordinates_names,
        coords=spectrum_coords,
    )
    periodogram = xarray.DataArray(
        data=normalized_rechunked_periodogram.transpose(),
        dims=coordinates_names,
        coords=regressive_coords,
    )
    ar_spectrum = xarray.DataArray(
        data=normalized_rechunked_ar_spectrum.transpose(),
        dims=coordinates_names,
        coords=regressive_coords,
    )
    # Building the dataset
    # TODO: DOVE LI PIJO I BUCHI?
    fft_data = xarray.Dataset(
        data_vars={
            "spectrum": spectrum.astype("complex64").where(spectrum != 0),
        },
    )
    regressive_data = xarray.Dataset(
        data_vars={
            "periodogram": periodogram.where(periodogram != 0),
            "ar_spectrum": ar_spectrum.where(ar_spectrum != 0),
        },
    )

    # Time dependant attributes
    td_attributes_df = header_pia[storage_settings.TIME_DEPENDANT_ATTRIBUTES]
    timed_td_attributes_df = td_attributes_df.with_columns(
        polars.Series("time", datetimes)
    )

    td_attributes_dset = (
        timed_td_attributes_df.to_pandas().set_index(["time"]).to_xarray()
    )

    return (
        fft_data,
        regressive_data,
        td_attributes_dset,
        ti_attributes_df,
    )


def load_sfdb09(
    path: str | list[str],
    start_freq: float = -1,
    end_freq: float = 1e10,
    start_time: str = "2000-01-01",
    end_time: str = "2200-01-01",
    memory_warning_limit: float = 8,
    memory_limit: float = 16,
    verbose: int = 0,
):
    """
    Loads SFDB data to memory

    Returns data extracted from a collection of SFDB files.
    Due to the large size of this files, it checks for the size of the returns
    before starting the computation. Memory limits can be setted using ``memory_limit``
    and ``memory_warning_limit``.
    It is possible to specify the range of times to be analyzed. In that case
    only a subset of `path` is accessed. This can be very useful in case you want
    to extract data from a database, without having to manually select files.
    To load data :func:`load_sfdb09` will call `suite.storage_manager.scan_sfdb09`.

    Parameters
    ----------
    path : str or list[str]
        Path or list of paths to the files to be loaded. Provided paths
        will be checked for consistency.
    start_freq : float, optional
        Lower frequency limit. Defaults to -1.
    end_freq : float, optional
        Upper frequency limit. Defaults to 1e10.
    start_time : str, optional
        Starting time of analysis. File names in ``path`` will be checked.
        Only those with starting time > `start time` will be opened.
        Defaults to "2000-01-01".
    end_time : str, optional
        Ending time of analysis. File names in ``path`` will be checked.
        Only those with starting time < `start time` will be opened.
        Defaults to "2200-01-01".
    memory_warning_limit : float
        Sets the memory limit (in GB) over wich a warning message is displayed.
        Defaults to 8.
    memory_limit : float
        Sets the memory limit (in GB) over wich an Exeption is raised.
        Defaults to 16.
    verbose : int
        Verbose level. Defaults to 0.

    Returns
    -------
    fft : ndarray[complex64]
        The complex fft data from the SFDB files.
    periodogram : ndarray[float64]
        Periodogram.
    ar_spectrum : ndarray[float64]
        Autoregressive spectrum.
    td_attributes : ndarray[float64]
        Time dependant attributes. For more information about attributes see below.
    ti_attributes : ndarray[float64]
        Time independant attributes. For more information about attributes see below.
    time_axis : ndarray[float64]
        Time axis computed by :func:`suite.storage_manager.scan_sfdb09`.
    frequency_axis : ndarray[float64]
        Frequency axis computed by :func:`suite.storage_manager.scan_sfdb09`.

    See Also
    --------

    Notes
    -----

    Examples
    --------



    """
    # DOCUMENT THIS
    # Beware: this function loads data to memory. Until further notice
    # this function will simply prompt a warning message if data to load exceed
    # 8 GB, and an error if data exceeds 16 GB of memory.
    #
    # This function will call scan_sfdb09 and there will be file checking.
    # But since in most applications, the file list given as input is much larger
    # than the time interval, a first consistency check will be run. This will allow
    # to select only those files that contain desired data, skipping the others.
    #
    # Consistency checks on provided paths are automatically done by the following
    # function.
    parsed_file_list = select_files_in_time_range(path, start_time, end_time)

    (
        fft_data,
        regressive_data,
        td_attributes,
        ti_attributes,
    ) = scan_sfdb09(parsed_file_list, verbose=verbose)

    sliced_fft_data = fft_data["spectrum"].loc[
        dict(time=slice(start_time, end_time), frequency=slice(start_freq, end_freq))
    ]
    sliced_regressive_data = regressive_data.loc[
        dict(time=slice(start_time, end_time), frequency=slice(start_freq, end_freq))
    ]
    sliced_td_attributes = td_attributes.loc[
        dict(
            time=slice(start_time, end_time),
        )
    ]

    total_size_of_variables = (
        sliced_fft_data.nbytes + sliced_regressive_data.nbytes
    ) / 1e9
    if total_size_of_variables > memory_warning_limit:
        warnings.warn(f"You're variables are quite big, try using scan_sfdb09() first")
        if total_size_of_variables > memory_limit:
            raise Exception("You are exceeding memory limit, try using scan_sfdb09()")

    fft = sliced_fft_data.values
    periodogram = sliced_regressive_data["periodogram"].values
    ar_spectrum = sliced_regressive_data["ar_spectrum"].values
    td_attributes = sliced_td_attributes.to_pandas()
    time_axis = sliced_fft_data.time.values
    frequency_axis = sliced_fft_data.frequency.values

    return (
        fft,
        periodogram,
        ar_spectrum,
        td_attributes,
        ti_attributes,
        time_axis,
        frequency_axis,
    )


def scan_database() -> dask.array:
    ...


def load_database():
    return scan_database.compute()


def convert_database():
    ...


def slice_database():
    ...
