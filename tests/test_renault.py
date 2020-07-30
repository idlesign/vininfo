from vininfo import Vin


def test_renault():

    vin = Vin('VF14SRAP451234567')

    assert '%s' % vin
    assert vin.wmi == 'VF1'
    assert vin.manufacturer == 'Renault'
    assert vin.vds == '4SRAP4'
    assert vin.vis == '51234567'
    assert vin.years == [2005]
    assert vin.region_code == 'V'
    assert vin.region == 'Europe'
    assert vin.country_code == 'VF'
    assert vin.country == 'France'
    assert '%s' % vin.brand == 'Renault (Renault)'

    details = vin.details
    assert not details.engine
    assert details.model
    assert details.model.code == 'S'
    assert details.model.name == ['Logan', 'Sandero', 'Duster', 'Dokker', 'Lodgy']
    assert details.body.code == '4'
    assert details.body.name == 'Sedan, 4-Door'
    assert details.plant.code == 'P'
    assert details.plant.name == 'Mexico'
    assert details.transmission.code == '4'
    assert details.transmission.name == 'Manual, 5-Gears'
    assert details.serial.code == '1234567'


def test_bogus():
    vin = Vin('VF1KG1PBE34488860')
    details = vin.details
    assert details.engine.code == ''
    assert not details.engine
