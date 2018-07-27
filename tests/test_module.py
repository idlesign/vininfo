import pytest

from vininfo import Vin, ValidationError


def test_validation():

    with pytest.raises(ValidationError):
         Vin('tooshort')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAAAAAAAAAAO')


def test_basic():

    # faked
    assert Vin('JSA12345678901234').manufacturer == 'Suzuki'


def test_checksum():

    assert Vin('1M8GDM9AXKP042788').verify_checksum()

    # faked
    assert not Vin('1M8GDM9AyKP042788').verify_checksum()
