from vininfo import Vin


def test_ford_north_america():

    vin = Vin('1FA6P8TH5L5100001')

    assert f'{vin}'
    assert vin.wmi == '1FA'
    assert vin.manufacturer == 'Ford'
    assert vin.vds == '6P8TH5'
    assert vin.vis == 'L5100001'
    assert vin.years_code == 'L'
    assert vin.years == [2020, 1990]
    assert vin.region == 'North America'
    assert vin.country == 'United States'
    assert f'{vin.brand}' == 'Ford (Ford)'

    details = vin.details
    assert details.model.code == 'P8T'
    assert details.model.name == 'Ford Mustang'
    assert details.engine.code == 'H'
    assert '2.3L I4' in details.engine.name
    assert details.plant.code == '5'
    assert details.plant.name == 'Flat Rock, MI, US'
    assert details.serial.code == '100001'


def test_ford_mexico():

    vin = Vin('3FA6P0H75HR100001')

    assert vin.manufacturer == 'Ford'
    assert vin.country == 'Mexico'

    details = vin.details
    assert details.model.code == 'P0H'
    assert details.model.name == 'Ford Fusion'
    assert details.plant.code == 'R'
    assert details.plant.name == ['Milpitas, CA, US', 'Hermosillo, Mexico']
