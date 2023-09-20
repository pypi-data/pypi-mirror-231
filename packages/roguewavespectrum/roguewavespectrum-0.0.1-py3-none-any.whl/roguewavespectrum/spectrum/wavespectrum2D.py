import numpy
from typing import TypeVar
from xarray import (
    Dataset,
    DataArray,
)
from .wavespectrum import WaveSpectrum
from roguewavespectrum.physical_constants import PhysicsOptions
_T = TypeVar("_T")

from .variable_names import (
    NAME_D,
    NAME_E,
    NAME_F,
    SPECTRAL_VARS,
)


class FrequencyDirectionSpectrum(WaveSpectrum):
    standard_name = "sea_surface_wave_variance_spectral_density"
    units = "m2 Hz-1 deg-1"
    def __init__(self, dataset: Dataset, physics_options:PhysicsOptions=None,**kwargs):
        super(FrequencyDirectionSpectrum, self).__init__(dataset, physics_options=physics_options,**kwargs)
        for name in [NAME_F, NAME_D, NAME_E]:
            if name not in dataset and name not in dataset.coords:
                raise ValueError(
                    f"Required variable/coordinate {name} is"
                    f" not specified in the dataset"
                )

    def __len__(self):
        return int(numpy.prod(self.variance_density.shape[:-2]))

    @property
    def direction_step(self) -> DataArray:
        """
        Calculate the step size between the direction bins. Because the direction bins are circular, we use a modular
        difference estimate.
        :return:
        """
        return DataArray(
            data=(numpy.diff(self.direction.values, append=self.direction[0]) + 180) % 360 - 180,
            coords={NAME_D: self.direction.values},
            dims=[NAME_D]
        )

    @property
    def radian_direction(self) -> DataArray:
        data_array = self.dataset[NAME_D] * numpy.pi / 180
        data_array.name = "radian_direction"
        return data_array

    def _directionally_integrate(self, data_array: DataArray) -> DataArray:
        return (data_array * self.direction_step).sum(NAME_D, skipna=True)

    @property
    def e(self) -> DataArray:
        """
        Return the directionally integrated spectrum.

        :return: 1D spectral values (directionally integrated spectrum).
        """
        return self._directionally_integrate(self.dataset[NAME_E])

    @property
    def a1(self) -> DataArray:
        return (
                self._directionally_integrate(
                    self.dataset[NAME_E] * numpy.cos(self.radian_direction)
                )
                / self.e
        )

    @property
    def b1(self) -> DataArray:
        return (
                self._directionally_integrate(
                    self.dataset[NAME_E] * numpy.sin(self.radian_direction)
                )
                / self.e
        )

    @property
    def a2(self) -> DataArray:
        return (
                self._directionally_integrate(
                    self.dataset[NAME_E] * numpy.cos(2 * self.radian_direction)
                )
                / self.e
        )

    @property
    def b2(self) -> DataArray:
        return (
                self._directionally_integrate(
                    self.dataset[NAME_E] * numpy.sin(2 * self.radian_direction)
                )
                / self.e
        )

    @property
    def direction(self) -> DataArray:
        return self.dataset[NAME_D]

    def as_frequency_spectrum(self):
        return _circular_dependency_workaround(self)


    def differentiate(self, coordinate=None, **kwargs) -> "FrequencyDirectionSpectrum":

        if coordinate is None:
            coordinate = "time"

        if coordinate not in self.dataset:
            raise ValueError(f"Coordinate {coordinate} does not exist in the dataset")

        data = {
            NAME_E: (
                self.dims,
                self.variance_density.differentiate(
                    coordinate, datetime_unit="s", **kwargs
                ).values,
            )
        }
        for x in self.dataset:
            if x in SPECTRAL_VARS:
                continue
            data[x] = (self.dims_space_time, self.dataset[x].values)

        return FrequencyDirectionSpectrum(Dataset(data_vars=data, coords=self.coords()))

    @property
    def number_of_directions(self) -> int:
        return len(self.direction)



def _circular_dependency_workaround(spectrum:FrequencyDirectionSpectrum):
    from .wavespectrum1D import FrequencySpectrum


    dataset = {
        "a1": spectrum.a1,
        "b1": spectrum.b1,
        "a2": spectrum.a2,
        "b2": spectrum.b2,
        "variance_density": spectrum.e,
    }
    for name in spectrum.dataset:
        if name not in SPECTRAL_VARS:
            dataset[name] = spectrum.dataset[name]

    return FrequencySpectrum(Dataset(dataset))