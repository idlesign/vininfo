import pytest

from vininfo import Vin, ValidationError


def test_validation():

    with pytest.raises(ValidationError):
         Vin('tooshort')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAAAAAAAAAAO')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAAAAAAAAAAO')

    with pytest.raises(ValidationError):
         Vin('1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAIAAAAAAAAA')

    with pytest.raises(ValidationError):
         Vin('AAAAAAA:AAAAAAAAA')


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

    # non strict
    non_strict = Vin('WBA71DC010CH14720')
    assert non_strict.verify_checksum(check_year=False)
    assert not non_strict.verify_checksum()


def test_unsupported_brand():

    vin = Vin('200BL8EV9AX604020')
    assert vin.manufacturer == 'UnsupportedBrand'
    assert vin.country is None


def test_merge_wmi():
    from vininfo.utils import merge_wmi

    missing, lines = merge_wmi({'1DTEST': 'Some', '1GTEST': 'Other'})
    assert missing == {'1DTEST', '1GTEST'}
    assert "    '1D': 'Dodge',\n    '1DTEST': 'Some'," in lines
    assert "    '1GT': 'GMC Truck',\n    '1GTEST': 'Other'," in lines


def test_squish_vin():
     assert Vin('KF1SF08WJ8B257338').squish_vin == 'KF1SF08W8B'
     
