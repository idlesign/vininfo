from ..common import candidate_by_year_model_mapping, constant_info
from ..dicts.bodies import BODY_MOTORCYCLE
from ._base import Detail, VinDetails


def get_wmi(details: VinDetails):
    # noinspection PyProtectedMember
    return details._vin.wmi


def get_years(details: VinDetails):
    # noinspection PyProtectedMember
    return details._vin.years


def get_model(details: VinDetails):
    """It looks like Bajaj Brazil is using the same VDS mapping that Bajaj India, or a pretty close one"""

    # Model name pattern with spaces
    bajaj_commons_mapping = {
        'A92': 'Dominar 160',
        'A36': 'Dominar 200',
        'A67': 'Dominar 400',
        'B65': 'Dominar 250',
    }

    bajaj_brazil_mapping_by_year_model = {
        '2026-': {
            'A92': 'Dominar NS160',
            'A36': 'Dominar NS200',
        },
        '-': {
            'C41': 'Pulsar N150'
        }
    }

    bajaj_brazil_mapping = bajaj_commons_mapping
    wmi = get_wmi(details)
    if wmi == '92T':
        bajaj_brazil_mapping = bajaj_commons_mapping.copy()
        updates = candidate_by_year_model_mapping(bajaj_brazil_mapping_by_year_model, get_years(details))
        if updates:
            bajaj_brazil_mapping.update(updates)

    candidates = {
        '92T': bajaj_brazil_mapping,
        '95V': {  # Bajaj assembled by Dafra
            '2A1': 'Dominar 160',
            '2B1': 'Dominar 200',
            '3B1': 'Dominar 400',
        },
        'MD2': {
            **bajaj_commons_mapping,
            # Bajaj India
            'B54': 'Pulsar N160',
            'B97': 'Pulsar N250',
        }
    }

    return candidates.get(wmi, {})


def get_plant(details):
    candidates = {
        'MD2': {  # Bajaj India
            'C': 'Chakan',
            'W': 'Waluj',  # Guessing
            'P': 'Pant Nagar'  # Guessing
        }
    }

    return candidates.get(get_wmi(details), {
        # WMI = 95V or 92T
        'M': 'Manaus'
    })


class BajajDetails(VinDetails):
    # for a while, it will be decoded by the first 3 characters of vds
    model = Detail(('vds', slice(0, 3)), get_model)

    # for a while, it will be a motorcycle regardless of the code source
    body = Detail(None, constant_info(BODY_MOTORCYCLE))

    plant = Detail(('vis', 1), get_plant)

    serial = Detail(('vis', slice(2, None)))
