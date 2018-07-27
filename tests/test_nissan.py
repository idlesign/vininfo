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
    assert details.model_code == 'J'
    assert details.model == ['Maxima']
    assert details.body_code == '1'
    assert details.body == ['4-Door Sedan', 'Standard Body Truck']
    assert details.engine_code == 'N'
    assert details.engine == ['VH45DE']
    assert details.plant_code == 'T'
    assert details.plant == ['Tochigi', 'Oppama']
    assert details.serial == '000001'

    assert vin.verify_checksum()
