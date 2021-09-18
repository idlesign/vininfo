from vininfo import Vin


def test_opel():

    vin = Vin('W0LPC6DB3CC123456')

    assert '%s' % vin
    assert vin.wmi == 'W0L'
    assert vin.manufacturer == 'Opel/Vauxhall'
    assert vin.vds == 'PC6DB3'
    assert vin.vis == 'CC123456'
    assert vin.years == [2012, 1982]
    assert vin.region_code == 'W'
    assert vin.region == 'Europe'
    assert vin.country_code == 'W0'
    assert vin.country == 'Germany'
    assert '%s' % vin.brand == 'Opel (Opel/Vauxhall)'

    details = vin.details
    assert details.model.code == 'P'
    assert details.model.name == ['Astra J', 'Zafira C']
    assert details.body.code == '6'
    assert details.body.name == 'Hatchback, 5-Door'
    assert details.engine.code == 'B'
    assert details.engine.name == 'A14XER100HP'
    assert details.plant.code == 'C'
    assert details.plant.name == 'Yelabuga'
    assert details.serial.code == '123456'
