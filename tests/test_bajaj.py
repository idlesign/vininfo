from vininfo import Vin

base_expected = {
    'brand': 'Bajaj (Bajaj)',
    'body_code': '',
    'body_name': 'Motorcycle',
}

brazil_base_expected = {
    'wmi': '92T',
    'manufacturer': 'Bajaj',
    'region_code': '9',
    'region': 'South America',
    'country_code': '92',
    'country': 'Brazil',
    'assembler': 'Bajaj (Bajaj)',
    'plant_code': 'M',
    'plant_name': 'Manaus',
    **base_expected
}

dafra_base_expected = {
    'wmi': '95V',
    'manufacturer': 'Dafra',
    'region_code': '9',
    'region': 'South America',
    'country_code': '95',
    'country': 'Brazil',
    'assembler': 'Dafra (Dafra)',
    'plant_code': 'M',
    'plant_name': 'Manaus',
    **base_expected
}

india_base_expected = {
    'wmi': 'MD2',
    'manufacturer': 'Bajaj',
    'region_code': 'M',
    'region': 'Asia',
    'country_code': 'MD',
    'country': 'India',
    'assembler': 'Bajaj (Bajaj)',
    'plant_code': 'C',
    'plant_name': 'Chakan',
    **base_expected
}


def data_provider():
    return [
        {
            'vin': '95V2A1E5PPM099209',
            'expected': {
                'vds': '2A1E5P',
                'vis': 'PM099209',
                'serial_code': '099209',
                'squish_vin': '95V2A1E5PM',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': '2A1',
                'model_name': 'Dominar 160',
                **dafra_base_expected
            }
        },
        {
            'vin': '95V2B1K5NPM099112',
            'expected': {
                'vds': '2B1K5N',
                'vis': 'PM099112',
                'serial_code': '099112',
                'squish_vin': '95V2B1K5PM',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': '2B1',
                'model_name': 'Dominar 200',
                **dafra_base_expected
            }
        },
        {
            'vin': '95V3B1J5NPM099022',
            'expected': {
                'vds': '3B1J5N',
                'vis': 'PM099022',
                'serial_code': '099022',
                'squish_vin': '95V3B1J5PM',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': '3B1',
                'model_name': 'Dominar 400',
                **dafra_base_expected
            }
        },
        {
            'vin': '92TA92DZXRMC09006',
            'expected': {
                'vds': 'A92DZX',
                'vis': 'RMC09006',
                'serial_code': 'C09006',
                'squish_vin': '92TA92DZRM',
                'years_code': 'R',
                'years': [2024, 1994],
                'model_code': 'A92',
                'model_name': 'Dominar 160',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TA92DX4TML92419',
            'expected': {
                'vds': 'A92DX4',
                'vis': 'TML92419',
                'serial_code': 'L92419',
                'squish_vin': '92TA92DXTM',
                'years_code': 'T',
                'years': [2026, 1996],
                'model_code': 'A92',
                'model_name': 'Dominar NS160',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TA36FZ8RMC90909',
            'expected': {
                'vds': 'A36FZ8',
                'vis': 'RMC90909',
                'serial_code': 'C90909',
                'squish_vin': '92TA36FZRM',
                'years_code': 'R',
                'years': [2024, 1994],
                'model_code': 'A36',
                'model_name': 'Dominar 200',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TA36FX9TML92914',
            'expected': {
                'vds': 'A36FX9',
                'vis': 'TML92914',
                'serial_code': 'L92914',
                'squish_vin': '92TA36FXTM',
                'years_code': 'T',
                'years': [2026, 1996],
                'model_code': 'A36',
                'model_name': 'Dominar NS200',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TB65GZ1RMD90922',
            'expected': {
                'vds': 'B65GZ1',
                'vis': 'RMD90922',
                'serial_code': 'D90922',
                'squish_vin': '92TB65GZRM',
                'years_code': 'R',
                'years': [2024, 1994],
                'model_code': 'B65',
                'model_name': 'Dominar 250',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TA67MZ1RMC90909',
            'expected': {
                'vds': 'A67MZ1',
                'vis': 'RMC90909',
                'serial_code': 'C90909',
                'squish_vin': '92TA67MZRM',
                'years_code': 'R',
                'years': [2024, 1994],
                'model_code': 'A67',
                'model_name': 'Dominar 400',
                **brazil_base_expected
            }
        },
        {
            'vin': '92TC41CX1TMB90948',
            'expected': {
                'vds': 'C41CX1',
                'vis': 'TMB90948',
                'serial_code': 'B90948',
                'squish_vin': '92TC41CXTM',
                'years_code': 'T',
                'years': [2026, 1996],
                'model_code': 'C41',
                'model_name': 'Pulsar N150',
                **brazil_base_expected
            }
        },
        {
            'vin': 'MD2A67MXXRCK99693',
            'expected': {
                'vds': 'A67MXX',
                'vis': 'RCK99693',
                'serial_code': 'K99693',
                'squish_vin': 'MD2A67MXRC',
                'years_code': 'R',
                'years': [2024, 1994],
                'model_code': 'A67',
                'model_name': 'Dominar 400',
                **india_base_expected
            }
        },
        {
            'vin': 'MD2B65GX9PCF91987',
            'expected': {
                'vds': 'B65GX9',
                'vis': 'PCF91987',
                'serial_code': 'F91987',
                'squish_vin': 'MD2B65GXPC',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': 'B65',
                'model_name': 'Dominar 250',
                **india_base_expected
            }
        },
        {
            'vin': 'MD2B97FX1PCB96793',
            'expected': {
                'vds': 'B97FX1',
                'vis': 'PCB96793',
                'serial_code': 'B96793',
                'squish_vin': 'MD2B97FXPC',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': 'B97',
                'model_name': 'Pulsar N250',
                **india_base_expected
            }
        },
        {
            'vin': 'MD2B54DX5PCB94941',
            'expected': {
                'vds': 'B54DX5',
                'vis': 'PCB94941',
                'serial_code': 'B94941',
                'squish_vin': 'MD2B54DXPC',
                'years_code': 'P',
                'years': [2023, 1993],
                'model_code': 'B54',
                'model_name': 'Pulsar N160',
                **india_base_expected
            }
        },
    ]


def test_bajaj():
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
