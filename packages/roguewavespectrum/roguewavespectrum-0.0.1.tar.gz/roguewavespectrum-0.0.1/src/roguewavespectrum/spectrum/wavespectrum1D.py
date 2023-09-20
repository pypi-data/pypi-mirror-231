import numpy
from .wavespectrum import WaveSpectrum
from roguewavespectrum.estimators.estimate import (
    estimate_directional_distribution,
    Estimators,
)
from roguewavespectrum.time import to_datetime64
from roguewavespectrum.physical_constants import PhysicsOptions
from typing import TypeVar, Literal
from xarray import (
    Dataset,
    DataArray,
    zeros_like,
    ones_like,
    concat
)
from .spline_interpolation import cumulative_frequency_interpolation_1d_variable
from .variable_names import (
    NAME_F,
    NAME_D,
    NAME_E,
    NAME_a1,
    NAME_b1,
    NAME_a2,
    NAME_b2,
    NAMES_1D,
    SPECTRAL_VARS,
)
from .wavespectrum2D import FrequencyDirectionSpectrum
from .extrapolate import numba_fill_zeros_or_nan_in_tail

_T = TypeVar("_T")


class FrequencySpectrum(WaveSpectrum):
    def __init__(self, dataset: Dataset, physics_options:PhysicsOptions=None,**kwargs):
        super(FrequencySpectrum, self).__init__(dataset, physics_options=physics_options,**kwargs)
        for name in [NAME_F, NAME_E]:
            if name not in dataset and name not in dataset.coords:
                raise ValueError(
                    f"Required variable/coordinate {name} is"
                    f" not specified in the dataset"
                )

    def __len__(self):
        return int(numpy.prod(self.variance_density.shape[:-1]))

    def interpolate_frequency(
            self: "FrequencySpectrum",
            new_frequencies,
            extrapolation_value=0.0,
            method: Literal["nearest", "linear", "spline"] = "linear",
            **kwargs,
    ) -> "FrequencySpectrum":

        if isinstance(new_frequencies, DataArray):
            new_frequencies = new_frequencies.values

        if method == "spline":
            self.fillna(0.0)
            frequency_axis = self.dims.index(NAME_F)
            interpolated_data = cumulative_frequency_interpolation_1d_variable(
                new_frequencies, self.dataset, frequency_axis=frequency_axis, **kwargs
            )
            object = FrequencySpectrum(interpolated_data)
            object.fillna(extrapolation_value)
            return object
        else:
            return self.interpolate(
                {NAME_F: new_frequencies},
                extrapolation_value=extrapolation_value,
                method=method
            )

    def interpolate(self: _T, coordinates, extrapolation_value=0.0, method='linear',**kwargs) -> _T:
        """
        Interpolate the spectrum to the given coordinates. The coordinates should be a dictionary with the dimension
        name as key and the coordinate as value. Uses the xarray interp method. Extrapolation is done by filling the
        NaN values with the given extrapolation value (0.0 by default).

        For physical reasons it is better to interpolate the scaled moments - as opposed to the normalized moments.
        For the dataset we interpolate we set a1: to A1 etc. Afterwards we scale the output back to the normalized
        state.

        :param coordinates: dictionary with coordinates for each dimension
        :param extrapolation_value: value to use for extrapolation
        :param method: interpolation method to use (see xarray interp method)
        :return: interpolated spectrum object
        """

        _dataset = Dataset()
        _moments = [NAME_a1, NAME_b1, NAME_a2, NAME_b2]

        if 'time' in coordinates:
            coordinates['time'] = to_datetime64(coordinates['time'])

        for name in self.dataset:
            _name = str(name)
            if _name in _moments:
                _dataset = _dataset.assign({_name: getattr(self, _name) * self.e})
            else:
                _dataset = _dataset.assign({_name: self.dataset[_name]})

        interpolated_data = _dataset.interp(
            coords=coordinates, method=method
        )
        for name in _moments:
            interpolated_data[name] = (
                    interpolated_data[name] / interpolated_data[NAME_E]
            )

        object = FrequencySpectrum(interpolated_data)
        object.fillna(extrapolation_value)
        return object

    @property
    def e(self):
        """
        Directionally integrated spectra. Synonym for variance_density for 1D spectra.

        :return: directionally integrated spectra.
        """
        return self.dataset[NAME_E]

    def extrapolate_tail(
        self,
        end_frequency,
        power=None,
        tail_energy=None,
        tail_bounds=None,
        tail_moments=None,
        tail_frequency=None,
    ) -> "FrequencySpectrum":
        """
        Extrapolate the tail using the given power
        :param end_frequency: frequency to extrapolate to
        :param power: power to use. If None, a best fit -4 or -5 tail is used.
        :return:
        """
        e = self.e
        a1 = self.a1
        b1 = self.b1
        a2 = self.a2
        b2 = self.b2

        frequency = self.frequency.values
        frequency_delta = frequency[-1] - frequency[-2]
        n = int((end_frequency - frequency[-1]) / frequency_delta) + 1

        fstart = frequency[-1] + frequency_delta
        fend = frequency[-1] + n * frequency_delta

        if tail_frequency is None:
            tail_frequency = numpy.linspace(fstart, fend, n, endpoint=True)

        tail_frequency = DataArray(
            data=tail_frequency, coords={"frequency": tail_frequency}, dims="frequency"
        )
        variance_density = concat(
            (e, e.isel(frequency=-1) * zeros_like(tail_frequency)), dim="frequency"
        )

        tail_a1 = a1.isel(frequency=-1) if tail_moments is None else tail_moments["a1"]
        tail_b1 = b1.isel(frequency=-1) if tail_moments is None else tail_moments["b1"]
        tail_a2 = a2.isel(frequency=-1) if tail_moments is None else tail_moments["a2"]
        tail_b2 = b2.isel(frequency=-1) if tail_moments is None else tail_moments["b2"]

        a1 = concat((a1, tail_a1 * ones_like(tail_frequency)), dim="frequency")
        b1 = concat((b1, tail_b1 * ones_like(tail_frequency)), dim="frequency")
        a2 = concat((a2, tail_a2 * ones_like(tail_frequency)), dim="frequency")
        b2 = concat((b2, tail_b2 * ones_like(tail_frequency)), dim="frequency")

        if tail_energy is not None:
            if isinstance(tail_energy, DataArray):
                tail_energy = tail_energy.values

            tail_information = (tail_bounds, tail_energy)
        else:
            tail_information = None

        variance_density = DataArray(
            data=numba_fill_zeros_or_nan_in_tail(
                variance_density.values,
                variance_density.frequency.values,
                power,
                tail_information=tail_information,
            ),
            dims=a1.dims,
            coords=a1.coords,
        )

        dataset = Dataset(
            {
                "variance_density": variance_density,
                "a1": a1,
                "b1": b1,
                "a2": a2,
                "b2": b2,
            }
        )

        for name in self.dataset:
            if name in SPECTRAL_VARS:
                continue
            else:
                dataset = dataset.assign({name: self.dataset[name]})

        return FrequencySpectrum(dataset)

    def downsample(self, frequencies) -> "FrequencySpectrum":
        cdf = self.cumulative_density_function()
        diff = numpy.diff(
            frequencies,
            append=2 * frequencies[-1] - frequencies[-2],
            prepend=2 * frequencies[0] - frequencies[1]
        )
        frequency_step = diff[0:-1] * 0.5 + diff[1:] * 0.5

        sampling_frequencies = numpy.concatenate(([0], numpy.cumsum(frequency_step)))
        sampling_frequencies = (
                sampling_frequencies - frequency_step[0] / 2 + frequencies[0]
        )

        dims = self.dims
        sampled_cdf = cdf.sel({"frequency": sampling_frequencies}, method="nearest")
        data = {
            NAME_E: (dims, sampled_cdf.diff(dim="frequency").values / frequency_step),
            NAME_a1: (
                dims,
                self.a1.sel({"frequency": frequencies}, method="nearest").values,
            ),
            NAME_b1: (
                dims,
                self.b1.sel({"frequency": frequencies}, method="nearest").values,
            ),
            NAME_a2: (
                dims,
                self.a2.sel({"frequency": frequencies}, method="nearest").values,
            ),
            NAME_b2: (
                dims,
                self.b2.sel({"frequency": frequencies}, method="nearest").values,
            ),
        }

        coords = {x: self.dataset[x].values for x in self.dims}
        coords[NAME_F] = frequencies

        for x in self.dataset:
            if x in SPECTRAL_VARS:
                continue
            data[x] = (self.dims_space_time, self.dataset[x].values)

        return FrequencySpectrum(Dataset(data_vars=data, coords=coords))

    def as_frequency_direction_spectrum(
            self,
            number_of_directions,
            method: Estimators = "mem2",
            solution_method="scipy",
    ) -> "FrequencyDirectionSpectrum":

        direction = numpy.linspace(0, 360, number_of_directions, endpoint=False)

        output_array = (
                estimate_directional_distribution(
                    self.a1.values,
                    self.b1.values,
                    self.a2.values,
                    self.b2.values,
                    direction,
                    method=method,
                    solution_method=solution_method,
                )
                * self.e.values[..., None]
        )

        dims = self.dims_space_time + [NAME_F, NAME_D]
        coords = {x: self.dataset[x].values for x in self.dims}
        coords[NAME_D] = direction

        data = {NAME_E: (dims, output_array)}
        for x in self.dataset:
            if x in SPECTRAL_VARS:
                continue
            data[x] = (self.dims_space_time, self.dataset[x].values)

        return FrequencyDirectionSpectrum(Dataset(data_vars=data, coords=coords))
