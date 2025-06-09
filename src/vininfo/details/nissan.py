from ._base import VinDetails, Detail
from ..dicts.bodies import *


class NissanDetails(VinDetails):
    """Nissan VIN details extractor."""

    model = Detail(('vds', 1), {
        'A': ['Armada', 'Titan', 'Maxima'],
        'B': 'Sentra',
        'C': 'Versa (07-11)',
        'D': ['Truck', 'Xterra (00-04)', 'Frontier'],
        'J': 'Maxima',
        'N': 'Xterra (05-11)',
        'R': 'Pathfinder',
        'S': ['240SX', 'Rogue (08-11)'],
        'U': 'Altima',
        'Z': ['300Z', '350Z', 'Murano'],
    })

    body = Detail(('vds', 3), {
        '1': [BODY_SEDAN_4, 'Standard Body Truck'],
        '4': BODY_COUPE_2,
        '5': BODY_SW_5,
        '6': [BODY_CABRI_2, 'Fastback', 'King Cab Truck'],
        '7': 'Crew Cab Truck',
        '8': BODY_SW_8,
    })

    engine = Detail(('vds', 0), {
        'A': ['VG30D', 'VK45DE', 'VQ35DE', 'VK56DE', 'VQ40DE', 'QR25DE'],
        'B': ['KA24DE', 'SR20DE', 'VQ35HR', 'MR18DE', 'QR25DE'],
        'C': ['SR20DE', 'VG30DETT', 'QG18DE'],
        'D': ['KA24DE', 'QG18DE', 'VQ35DE'],
        'E': ['VE30DE', 'GA16DE', 'VG33E'],
        'F': 'KA24E',
        'H': 'VG30E',
        'M': ['KA24DE', 'VG33ER'],
        'N': 'VH45DE',
        'R': 'VG30DE',
        'S': 'KA24E',
        'T': 'VG33E',
    })

    plant = Detail(('vis', 1), {
        'C': 'Smyrna',
        'L': 'Aguas Calientes',
        'M': 'Tochigi',
        'N': 'Canton',
        'T': ['Tochigi', 'Oppama'],
        'W': 'Kyushyu',
    })

    serial = Detail(('vis', slice(2, None)))
