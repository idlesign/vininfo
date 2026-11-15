from vininfo import Vin


def test_mercedes_benz_germany():

    vin = Vin('WDDGF8AB8EA123456')

    assert f'{vin}'
    assert vin.wmi == 'WDD'
    assert vin.manufacturer == 'Mercedes-Benz'
    assert vin.vds == 'GF8AB8'
    assert vin.vis == 'EA123456'
    assert vin.years_code == 'E'
    assert vin.years == [2014, 1984]
    assert vin.region == 'Europe'
    assert vin.country == 'Germany'
    assert f'{vin.brand}' == 'Mercedes (Mercedes-Benz)'

    details = vin.details
    assert details.model.code == 'G'
    assert 'W204 C-Class' in details.model.name
    assert details.body.code == 'F'
    assert 'Sedan' in details.body.name
    assert details.doors.name == '4'
    assert details.plant.code == 'A'
    assert details.plant.name == 'Sindelfingen, Germany'
    assert details.serial.code == '123456'


def test_mercedes_benz_usa():

    vin = Vin('4JGDA5JB3HA123456')

    assert vin.manufacturer == 'Mercedes-Benz'
    assert vin.country == 'United States'

    details = vin.details
    assert details.model.code == 'D'
    assert 'W166 M/GLE-Class' in details.model.name
    assert details.body.name == 'Crossover'
    assert details.plant.code == 'A'
    assert details.plant.name == 'Vance, AL, US'
