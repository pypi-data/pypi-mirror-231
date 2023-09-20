import numpy as np
from typing import TypeVar, Literal

_T = TypeVar("_T")

DirectionalUnit = Literal['degrees', 'radians']
DirectionalConvention = Literal['nautical', 'mathematical', 'meteorological']


def wave_mean_direction(a1: _T, b1: _T, unit: DirectionalUnit = 'degrees', convention: DirectionalConvention = 'mathematical') -> _T:
    angle = convert_unit(np.arctan2(b1, a1), unit, 'radians')

    return convert_angle_convention(angle, convention, 'mathematical', unit)


def wave_directional_spread(a1: _T, b1: _T, unit: DirectionalUnit = 'degrees') -> _T:
    return convert_unit(np.sqrt(2 - 2 * np.sqrt(a1 ** 2 + b1 ** 2)), to=unit, _from='radians')


def convert_unit(angle: _T, to: DirectionalUnit = 'degrees', _from: DirectionalUnit = 'degrees') -> _T:
    """
    Convert angle from one unit to another.
    :param angle: angle in radians or degrees
    :param to: unit to convert to, one of 'degrees', 'radians'
    :param _from: unit to convert from, one of 'degrees', 'radians'
    :return:
    """
    if to == _from and to in ['degrees', 'radians']:
        return angle

    elif to == 'degrees':
        return angle * 180 / np.pi

    elif to == 'radians':
        return angle / 180 * np.pi

    else:
        if to not in ['degrees', 'radians']:
            raise ValueError('Unknown unit to convert to')
        else:
            raise ValueError('Unknown unit to convert from')


def convert_angle_convention(
        angle: _T,
        to_convention: DirectionalConvention = 'mathematical',
        from_convention: DirectionalConvention = 'mathematical',
        units: DirectionalUnit = 'radians') -> _T:
    """
    Convert angle from one convention to another. Conventions are:

    - mathematical: 0 degrees / radians is east, going to, measured positive counterclockwise.
    - nautical: 0 degrees / radians is north, going to, measured positive clockwise.
    - meteorological: 0 / radians degrees is north, coming from, measured positive counterclockwise.

    :param angle: angle in radians or degrees
    :param to_convention: convention to convert to, one of 'mathematical', 'nautical', 'meteorological'
    :param from_convention: convention to convert from, one of 'mathematical', 'nautical', 'meteorological'
    :param units: default 'radians', one of 'radians', 'degrees'
    :return: angle in radians or degrees (depending on units), in the new convention
    """

    if units == 'degrees':
        wrapping_length = 360

    elif units == 'radians':
        wrapping_length = 2 * np.pi
    else:
        raise ValueError('Unknown units')

    if from_convention == 'mathematical':
        pass
    elif from_convention == 'nautical':
        angle = (wrapping_length / 4 - angle) % (wrapping_length)
    elif from_convention == 'meteorological':
        angle = (3 * wrapping_length / 4 - angle) % (wrapping_length)
    else:
        raise ValueError('Unknown convention')

    if to_convention == 'mathematical':
        return angle

    elif to_convention == 'nautical':
        return (wrapping_length / 4 - angle) % (wrapping_length)

    elif to_convention == 'meteorological':
        return (3 * wrapping_length / 4 - angle) % (wrapping_length)

    else:
        raise ValueError('Unknown convention')
