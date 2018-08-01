from vininfo import Vin


def test_nissan():

    vin = Vin('5N1NJ01CXST000001')

    assert '%s' % vin
    assert vin.wmi == '5N1'
    assert vin.manufacturer == 'Nissan'
    assert vin.vds == 'NJ01CX'
    assert vin.vis == 'ST000001'
    assert vin.years == [1995]
    assert vin.region_code == '5'
    assert vin.region == 'North America'
    assert vin.country_code == '5N'
    assert vin.country == 'United States'
    assert '%s' % vin.brand == 'Nissan (Nissan)'

    details = vin.details
    assert details.model.code == 'J'
    assert details.model.name == 'Maxima'
    assert details.body.code == '1'
    assert details.body.name == ['Sedan, 4-Door', 'Standard Body Truck']
    assert details.engine.code == 'N'
    assert details.engine.name == 'VH45DE'
    assert details.plant.code == 'T'
    assert details.plant.name == ['Tochigi', 'Oppama']
    assert details.serial.code == '000001'

    assert vin.verify_checksum()
