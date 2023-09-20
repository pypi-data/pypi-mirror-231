from roguewavespectrum.spectrum._directions import wave_directional_spread, wave_mean_direction, convert_unit, convert_angle_convention
import numpy as np


def test_convert_unit():
    assert convert_unit(180, "radians", "degrees") == np.pi
    assert convert_unit(np.pi/2, "degrees", "radians") == 90
    assert convert_unit(1, "radians", "radians") == 1
    assert convert_unit(1, "degrees", "degrees") == 1


def test_convert_angle_convention():
    assert convert_angle_convention(180,'nautical','mathematical', 'degrees') == 270
    assert convert_angle_convention(np.pi, 'nautical', 'mathematical', 'radians') == 3 / 2  * np.pi
    assert convert_angle_convention(180, 'nautical', 'meteorological', 'degrees') == 0
    assert convert_angle_convention(180, 'nautical', 'nautical', 'degrees') == 180

    assert convert_angle_convention(180,'meteorological','mathematical', 'degrees') == 90
    assert convert_angle_convention(np.pi, 'meteorological', 'mathematical', 'radians') == 1 / 2  * np.pi
    assert convert_angle_convention(180, 'meteorological', 'meteorological', 'degrees') == 180
    assert convert_angle_convention(180, 'meteorological', 'nautical', 'degrees') == 0

    assert convert_angle_convention(180,'mathematical','mathematical', 'degrees') == 180
    assert convert_angle_convention(np.pi, 'mathematical', 'mathematical', 'radians') == np.pi
    assert convert_angle_convention(180, 'mathematical', 'meteorological', 'degrees') == 90
    assert convert_angle_convention(180, 'mathematical', 'nautical', 'degrees') == 270
