from vininfo import Vin


def test_toyota():

    vin = Vin('4T1BF3EK5BU123456')

    assert f'{vin}'
    assert vin.wmi == '4T1'
    assert vin.manufacturer == 'Toyota'
    assert vin.vds == 'BF3EK5'
    assert vin.vis == 'BU123456'
    assert vin.years_code == 'B'
    assert vin.years == [2011, 1981]
    assert vin.region == 'North America'
    assert vin.country == 'United States'
    assert f'{vin.brand}' == 'Toyota (Toyota)'

    details = vin.details
    assert details.model.code == 'K'
    assert details.model.name == 'Toyota Camry'
    assert details.body.code == 'B'
    assert details.body.name == ['Sedan', 'Station Wagon']
    assert details.doors.code == 'B'
    assert details.doors.name == ['4', '5']
    assert details.drive.code == 'B'
    assert details.drive.name == ['2WD', '4WD']
    assert details.engine.code == 'F'
    assert details.engine.name == ['2AR-FE', '2GR-FXS', '4GR-FSE', 'T24A-FTS']
    assert details.plant.code == 'U'
    assert details.plant.name == 'Georgetown, KY, US'
    assert details.serial.code == '123456'


def test_toyota_lexus():

    vin = Vin('58ABK1GG1GG123456')

    assert vin.manufacturer == 'Lexus'
    assert f'{vin.brand}' == 'Toyota (Lexus)'

    details = vin.details
    assert details.model.code == 'G'
    assert details.model.name == ['Lexus ES', 'Toyota Corolla Cross']
    assert details.plant.code == 'G'
    assert details.plant.name == 'Gliwice, Poland'
