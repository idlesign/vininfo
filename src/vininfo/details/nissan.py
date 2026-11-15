from ..dicts.bodies import *
from ..dicts.cabs import *
from ..dicts.doors import *
from ._base import Detail, VinDetails


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
        '1': [BODY_SEDAN, BODY_PICKUP],
        '4': BODY_COUPE,
        '5': BODY_SW,
        '6': [BODY_CABRI, 'Fastback', BODY_PICKUP],
        '7': BODY_PICKUP,
        '8': BODY_SW,
    })

    cab = Detail(('vds', 3), {
        '1': CAB_REGULAR,
        '6': CAB_ACCESS,
        '7': CAB_CREW,
    })

    doors = Detail(('vds', 3), {
        '1': [DOORS_2, DOORS_4],
        '4': DOORS_2,
        '5': DOORS_5,
        '6': DOORS_2,
        '7': DOORS_4,
        '8': DOORS_8,
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
