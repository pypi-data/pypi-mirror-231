from typing import Literal

NAME_F: Literal["frequency"] = "frequency"
NAME_D: Literal["direction"] = "direction"
NAME_T: Literal["time"] = "time"
NAME_E: Literal["variance_density"] = "variance_density"
NAME_a1: Literal["a1"] = "a1"
NAME_b1: Literal["b1"] = "b1"
NAME_a2: Literal["a2"] = "a2"
NAME_b2: Literal["b2"] = "b2"
NAME_LAT: Literal["latitude"] = "latitude"
NAME_LON: Literal["longitude"] = "longitude"
NAME_DEPTH: Literal["depth"] = "depth"
NAMES_2D = (NAME_F, NAME_D, NAME_T, NAME_E, NAME_LAT, NAME_LON, NAME_DEPTH)
NAMES_1D = (
    NAME_F,
    NAME_T,
    NAME_E,
    NAME_LAT,
    NAME_LON,
    NAME_a1,
    NAME_b1,
    NAME_a2,
    NAME_b2,
    NAME_DEPTH,
)
SPECTRAL_VARS = (NAME_E, NAME_a1, NAME_b1, NAME_a2, NAME_b2)
SPECTRAL_MOMENTS = (NAME_a1, NAME_b1, NAME_a2, NAME_b2)
SPECTRAL_DIMS = (NAME_F, NAME_D)
SPACE_TIME_DIMS = (NAME_T, NAME_LON, NAME_LAT)