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
    assert details.model_code == 'S'
    assert details.model == ['Logan', 'Sandero', 'Duster', 'Dokker', 'Lodgy']
    assert details.body_code == '4'
    assert details.body == 'Sedan 4-Door'
    assert details.plant_code == 'P'
    assert details.transmission_code == '4'
    assert details.transmission == 'Manual, 5-Gears'
    assert details.plant == 'Mexico'
    assert details.serial == '1234567'
