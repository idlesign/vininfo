from ._base import VinDetails, Detail
from ..dicts.bodies import *


class AvtoVazDetails(VinDetails):
    """AvtoVAZ VIN details extractor."""

    model = Detail(('vds', 1), {
        'A': 'XRAY',
        'F': 'Vesta',
    })

    body = Detail(('vds', 2), {
        'B': BODY_HATCH_5,
        'K': BODY_SW_5,
        'L': BODY_SEDAN_4,
    })

    engine = Detail(('vds', 3), {
        '1': '21129',
        '2': '11189',
        '3': '21179',
        '4': 'H4M',
        'A': '21129 CNG',
    })

    plant = Detail(('vis', 1), {
        '0': 'Tolyatti',
        'Y': 'Izhevsk',
    })

    transmission = Detail(('vds', 4), {
        '1': 'Manual, 5-Gear (VAZ 21807)',
        '2': 'Semi-automatic, 5-Gear (VAZ 21827)',
        '3': 'Manual, 5-Gear (Renault JH3 514)',
    })

    serial = Detail(('vis', slice(2, None)))
