from ._base import VinDetails, Detail
from ..dicts.bodies import *


def get_engine(details):

    candidates = {
        'P': {
            '1': 'A18XER140HP',
            'B': 'A14XER100HP',
            'C': 'A14NET140HP',
            'D': 'A16XER115HP',
            'J': 'A16LET180HP',
            'N': 'A20DTH165HP',
            'U': 'A14NEL120HP',
        },
        'W': {
            'N': 'A20DTH160HP',
            'C': 'A14NET140HP',
        },
        'G': {
            'A': 'A16XER115HP',
            'B': 'A16LET180HP',
            'C': 'A18XER140HP',
            'D': 'A20NHT220HP',
            'E': 'A20NHT250HP',
            'F': 'A28NET260HP',
            'G': 'A28NER325HP',
            'M': 'A20DTH160HP',
            'N': 'A20DTR195HP',
            'P': 'A14NFT140HP',
            'X': 'A20NHT250HP',
        },
        'V': {
            '1': 'Y13D70HP',
            '2': 'Z14XEP100HP',
        },
        'S': {
            'C': 'Z14XEP100HP',
            'D': 'A14NEL120HP',
            'E': 'A14NET140HP',
        },
        'J': {
            '8': 'A14NET140HP',
        },
    }

    return candidates.get(details.model.code, {})


class OpelDetails(VinDetails):
    """Opel VIN details extractor."""

    model = Detail(('vds', 0), {
        'F': 'Agila',
        'G': 'Insignia',
        'J': 'Mokka',
        'L': 'Antara',
        'M': 'Movano',
        'P': ['Astra J', 'Zafira C'],
        'R': 'Astra GTC J',
        'S': 'Meriva',
        'V': 'Combo II',
        'W': 'Cascada',
    })

    body = Detail(('vds', 2), {
        '2': BODY_HATCH_3,
        '3': BODY_COUPE_2,
        '5': BODY_SEDAN_4,
        '6': BODY_HATCH_5,
        '7': BODY_CROSS_3,
        '8': BODY_SW_5,
        '9': BODY_MINIVAN_5,
        'B': BODY_MINIBUS,
        'C': BODY_VAN,
        'J': BODY_VAN,
        'X': BODY_SW_3,
    })

    engine = Detail(('vds', 4), get_engine)

    plant = Detail(('vis', 1), {
        '1': 'Russelsheim',
        '2': 'Bochum',
        '3': 'Azambuja',
        '4': 'Zaragoza',
        '5': 'Antwerp',
        '6': 'Eisenach',
        '7': 'Luton',
        '8': 'Ellesmere Port',
        '9': 'Uusikaupunki',
        'A': 'Azambuja',
        'B': 'Bertone / Saint Peterburg',
        'C': 'Yelabuga',
        'D': 'Shin Chuang',
        'E': 'Heuliez',
        'F': 'Togliatti',
        'G': 'Gliwice',
        'H': 'Rayong',
        'L': 'Elizabeth',
        'M': 'Millbrook',
        'N': 'Norwich',
        'P': 'Warsaw',
        'R': 'Rosario',
        'S': 'Szentgotthard',
        'V': 'Luton',
        'X': 'Zaporozhia',
        'Z': 'Izmir',
    })

    serial = Detail(('vis', slice(2, None)))
