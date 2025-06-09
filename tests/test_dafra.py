from vininfo import Vin

base_expected = {
    'wmi': '95V',
    'region_code': '9',
    'region': 'South America',
    'country_code': '95',
    'country': 'Brazil',
    'assembler': 'Dafra (Dafra)',
    'manufacturer': 'Dafra',
    'brand': 'Dafra (Dafra)',
    'body_code': '',
    'body_name': 'Motorcycle',
    'plant_code': 'M',
    'plant_name': 'Manaus',
}

def data_provider():
    return [
        {
            'vin': '95VCB1K589M017683',
            'expected': {
                'vds': 'CB1K58',
                'vis': '9M017683',
                'serial_code': '017683',
                'squish_vin': '95VCB1K59M',
                'years_code': '9',
                'years': [2009],
                'model_code': 'CB',
                'model_name': 'Kansas 150',
                **base_expected
            }
        },
        {
            'vin': '95VCB1K589M022466',
            'expected': {
                'vds': 'CB1K58',
                'vis': '9M022466',
                'serial_code': '022466',
                'squish_vin': '95VCB1K59M',
                'years_code': '9',
                'years': [2009],
                'model_code': 'CB',
                'model_name': 'Kansas 150',
                **base_expected
            }
        },
        {
            'vin': '95VCA1C899M010049',
            'expected': {
                'vds': 'CA1C89',
                'vis': '9M010049',
                'serial_code': '010049',
                'squish_vin': '95VCA1C89M',
                'years_code': '9',
                'years': [2009],
                'model_code': 'CA',
                'model_name': 'Speed 150',
                **base_expected
            }
        },
        {
            'vin': '95VCA4A8BBM001656',
            'expected': {
                'vds': 'CA4A8B',
                'vis': 'BM001656',
                'serial_code': '001656',
                'squish_vin': '95VCA4A8BM',
                'years_code': 'B',
                'years': [2011, 1981],
                'model_code': 'CA',
                'model_name': 'Speed 150',
                **base_expected
            }
        },
    ]


def test_dafra():
    for data in data_provider():
        vin = data.get('vin')
        expected = data.get('expected')
        vin = Vin(vin)

        assert f'{vin}'
        assert vin.wmi == expected.get('wmi'), f'For {vin}'
        assert vin.manufacturer == expected.get('manufacturer'), f'For {vin}'
        assert f'{vin.assembler}' == expected.get('assembler'), f'For {vin}'
        assert vin.vds == expected.get('vds'), f'For {vin}'
        assert vin.vis == expected.get('vis'), f'For {vin}'
        assert vin.years_code == expected.get('years_code'), f'For {vin}'
        assert vin.years == expected.get('years'), f'For {vin}'
        assert vin.region_code == expected.get('region_code'), f'For {vin}'
        assert vin.region == expected.get('region'), f'For {vin}'
        assert vin.country_code == expected.get('country_code'), f'For {vin}'
        assert vin.country == expected.get('country'), f'For {vin}'
        assert f'{vin.brand}' == expected.get('brand'), f'For {vin}'
        assert vin.squish_vin == expected.get('squish_vin'), f'For {vin}'

        details = vin.details
        assert details.model.code == expected.get('model_code'), f'For {vin}'
        assert details.model.name == expected.get('model_name'), f'For {vin}'
        assert details.body.code == expected.get('body_code'), f'For {vin}'
        assert details.body.name == expected.get('body_name'), f'For {vin}'
        assert not details.engine, f'For {vin}'
        assert not details.transmission, f'For {vin}'
        assert details.plant.code == expected.get('plant_code'), f'For {vin}'
        assert details.plant.name == expected.get('plant_name'), f'For {vin}'
        assert details.serial.code == expected.get('serial_code'), f'For {vin}'
