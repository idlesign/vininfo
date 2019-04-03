import pytest

from vininfo import Vin, ValidationError


def test_validation():

    with pytest.raises(ValidationError):
         Vin('tooshort')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAAAAAAAAAAO')


def test_basic():

    # number faked
    vin = Vin('JSA12345678901234')
    assert vin.manufacturer == 'Suzuki'
    assert not vin.manufacturer_is_small

    # number faked
    assert Vin('TM912345678901234').manufacturer_is_small


def test_checksum():

    assert Vin('1M8GDM9AXKP042788').verify_checksum()

    # faked
    assert not Vin('1M8GDM9AyKP042788').verify_checksum()


def test_unsupported_brand():

    vin = Vin('200BL8EV9AX604020')
    assert vin.manufacturer == 'UnsupportedBrand'
    assert vin.country == 'Canada'
