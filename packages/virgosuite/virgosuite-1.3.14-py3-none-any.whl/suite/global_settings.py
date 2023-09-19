# global variables
import numpy

class storage_settings:
    """
    User settings for SFDB09 management

    Contains a collection of global settings to use the function of :py:mod:`storage_manager`.
    """
    # All SFDB files have the same structure, so here we set a global variable for
    # the reading
    
    #: list[str]: list of all elements of an header in an SFDB09, in the *exact* order they are stored in the file.
    HEADER_ELEMENTS = [
        ("count", "float64"),
        ("detector", "int32"),
        ("gps_seconds", "int32"),
        ("gps_nanoseconds", "int32"),
        ("fft_lenght", "float64"),
        ("starting_fft_sample_index", "int32"),
        ("unilateral_number_of_samples", "int32"),
        ("reduction_factor", "int32"),
        ("fft_interlaced", "int32"),  # typ
        ("number_of_flags", "float32"),
        ("scaling_factor", "float32"), # einstein
        ("mjd_time", "float64"),
        ("fft_index", "int32"),
        ("window_type", "int32"),  # wink
        ("normalization_factor", "float32"), # normd
        ("window_normalization", "float32"), # normw
        ("starting_fft_frequency", "float64"),
        ("subsampling_time", "float64"),
        ("frequency_resolution", "float64"),
        ("position_x", "float64"),
        ("position_y", "float64"),
        ("position_z", "float64"),
        ("velocity_x", "float64"),
        ("velocity_y", "float64"),
        ("velocity_z", "float64"),
        ("number_of_zeros", "int32"),
        ("sat_howmany", "float64"),
        ("spare_1", "float64"),
        ("spare_2", "float64"),
        ("spare_3", "float64"),
        ("percentage_of_zeros", "float32"), # spare 4
        ("spare_5", "float32"),
        ("spare_6", "float32"),
        ("lenght_of_averaged_time_spectrum", "int32"),
        ("scientific_segment", "int32"),
        ("spare_9", "int32"),
        # fft_data, periodogram and ARSpectrum have variable lengths
    ]

    #: obj: numpy dtype for the SFDB09 header.
    HEADER_DTYPE = numpy.dtype(HEADER_ELEMENTS)

    
    #: list[str]: List of header elements that are expected to be time independant.
    TIME_INDEPENDANT_ATTRIBUTES = [
        "count",
        "detector",
        "fft_lenght",
        "starting_fft_sample_index",
        "unilateral_number_of_samples",
        "reduction_factor",
        "fft_interlaced",
        "scaling_factor",
        "window_type",
        "normalization_factor",
        "window_normalization",
        "starting_fft_frequency",
        "subsampling_time",
        "frequency_resolution",
        "sat_howmany",
        "spare_1",
        "spare_2",
        "spare_3",
        "spare_5",
        "spare_6",
        "lenght_of_averaged_time_spectrum",
        "scientific_segment",
        "spare_9",
    ]


    #: list[str]: List of header elements that are expected to be time dependant.
    TIME_DEPENDANT_ATTRIBUTES = [
        "position_x",
        "position_y",
        "position_z",
        "velocity_x",
        "velocity_y",
        "velocity_z",
        "gps_seconds",
        "gps_nanoseconds",
        "number_of_flags",
        "mjd_time",
        "fft_index",
        "number_of_zeros",
        "percentage_of_zeros",
    ]

    #: dict[int, str]: Used to extract human readable information, from header.
    DETECTOR = {0: "Nautilus", 1: "Virgo", 2: "Ligo Hanford", 3: "Ligo Livingston"}

    #: dict[int, str]: Used to extract human readable information, from header.
    WINDOW_NAME = {
        0: "No Window",
        1: "Hanning",
        2: "Hamming",
        3: "Maria A. Papa",
        4: "Blackmann flatcos",
        5: "Flat top cosine edge",
    }

    #: dict[int, str]: Used to extract human readable information, from header.
    INTERLACED_METHOD = {1: "Half interlaced", 2: "Not interlaced"}
