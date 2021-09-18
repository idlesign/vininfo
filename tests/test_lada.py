from collections import OrderedDict

from vininfo import Vin


def test_lada():

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
    assert vin.country == 'Russia'
    assert vin.annotate() == OrderedDict([
        ('Country', 'Russia'),
        ('Manufacturer', 'AvtoVAZ'),
        ('Region', 'Europe'),
        ('Years', '2018, 1988'),
    ])
    assert '%s' % vin.brand == 'Lada (AvtoVAZ)'

    details = vin.details
    assert details.model.code == 'F'
    assert details.model.name == 'Vesta'
    assert details.body.code == 'K'
    assert details.body.name == 'Station Wagon, 5-Door'
    assert details.engine.code == '3'
    assert details.engine.name == '21179'
    assert details.transmission.code == '3'
    assert details.transmission.name == 'Manual, 5-Gear (Renault JH3 514)'
    assert details.plant.code == 'Y'
    assert details.plant.name == 'Izhevsk'
    assert details.annotate() == OrderedDict([
        ('Body', 'Station Wagon, 5-Door'),
        ('Engine', '21179'),
        ('Model', 'Vesta'),
        ('Plant', 'Izhevsk'),
        ('Serial', '144213'),
        ('Transmission', 'Manual, 5-Gear (Renault JH3 514)'),
    ])
    assert not vin.verify_checksum()
