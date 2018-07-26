from collections import OrderedDict

import pytest

from vininfo import Vin, ValidationError


def test_validation():

    with pytest.raises(ValidationError):
         Vin('tooshort')

    with pytest.raises(ValidationError):
         Vin('AAAAAAAAAAAAAAAAO')


def test_basic():

    vin = Vin('XTAGFK330JY144213')

    assert '%s' % vin
    assert vin.wmi == 'XTA'
    assert vin.manufacturer == 'AvtoVAZ'
    assert vin.vds == 'GFK330'
    assert vin.vis == 'JY144213'
    assert vin.years == [2018, 1988]
    assert vin.region_code == 'X'
    assert vin.region == 'Europe'
    assert vin.country_code == 'XT'
    assert vin.country == 'USSR/CIS'
    assert vin.annotate() == OrderedDict([
        ('Country', 'USSR/CIS'),
        ('Manufacturer', 'AvtoVAZ'),
        ('Region', 'Europe'),
        ('Years', '2018, 1988'),
    ])

    details = vin.details
    assert details.model_code == 'GF'
    assert details.model == 'Vesta'
    assert details.coachwork_code == 'K'
    assert details.coachwork == 'Station Wagon'
    assert details.engine_code == '3'
    assert details.engine == '21179'
    assert details.transmission_code == '3'
    assert details.transmission == 'Manual Renault'
    assert details.plant_code == 'Y'
    assert details.plant == 'Izhevsk'
    assert details.annotate() == OrderedDict([
        ('Coachwork', 'Station Wagon'),
        ('Engine', '21179'),
        ('Model', 'Vesta'),
        ('Plant', 'Izhevsk'),
        ('Serial', '144213'),
        ('Transmission', 'Manual Renault'),
    ])
    assert not vin.verify_checksum()

    # faked
    assert Vin('JSA12345678901234').manufacturer == 'Suzuki'


def test_checksum():

    assert Vin('1M8GDM9AXKP042788').verify_checksum()

    # faked
    assert Vin('11111111111111111').verify_checksum()

    # faked
    assert not Vin('11111111101111111').verify_checksum()
