from ..dicts.bodies import *
from ..dicts.doors import *
from ._base import Detail, VinDetails


class RenaultDetails(VinDetails):
    """Renault VIN details extractor."""

    model = Detail(('vds', 1), {
        '0': 'Twingo',
        '1': 'R4',
        '2': 'R25',
        '3': 'R4',
        '4': ['R21', 'Express'],
        '5': ['Clio I', 'Laguna', 'R19', 'Safrane'],
        'A': ['Megane I', 'Master'],
        'B': 'Clio II',
        'C': 'Kangoo',
        'D': 'Master',
        'E': ['Espace III', 'Avantime'],
        'G': 'Laguna II',
        'H': 'Master Propulsion',
        'J': ['Vel Satis', 'New Trafic'],
        'K': 'Espace IV',
        'L': 'Trafic',
        'M': 'Megan II',
        'P': 'Modus',
        'S': ['Logan', 'Sandero', 'Duster', 'Dokker', 'Lodgy'],
        'Y': 'Koleos',
    })

    body = Detail(('vds', 0), {
        '2': BODY_SEDAN,
        '3': BODY_HATCH,
        '4': BODY_SEDAN,
        '5': BODY_HATCH,
        '6': BODY_SW,
        '7': BODY_CABRI,
        '8': BODY_COUPE,
        'A': BODY_SW,
        'B': BODY_HATCH,
        'C': BODY_HATCH,
        'D': BODY_COUPE,
        'E': BODY_CABRI,
        'F': BODY_VAN,
        'G': BODY_MINIVAN,
        'J': BODY_MINIVAN,
        'H': BODY_PICKUP,
        'K': BODY_SW,
        'L': BODY_SEDAN,
        'M': BODY_SEDAN,
        'N': BODY_MINIVAN,
        'S': BODY_SW,
        'U': BODY_PICKUP,
    })

    doors = Detail(('vds', 0), {
        '2': DOORS_2,
        '3': DOORS_3,
        '4': DOORS_4,
        '5': DOORS_5,
        '6': DOORS_5,
        '7': DOORS_2,
        '8': DOORS_2,
        'A': DOORS_3,
        'B': DOORS_5,
        'C': DOORS_3,
        'D': DOORS_2,
        'E': DOORS_2,
        'G': DOORS_3,
        'J': DOORS_5,
        'H': DOORS_2,
        'K': DOORS_3,
        'L': DOORS_4,
        'M': DOORS_2,
        'N': DOORS_5,
        'S': DOORS_5,
        'U': DOORS_2,
    })

    plant = Detail(('vds', 4), {
        'A': 'Portugal',
        'B': 'Batilly',
        'C': 'Creil',
        'D': 'Douai',
        'E': 'Spain',  # ? city
        'V': 'Spain',  # ? city
        'F': 'Flin',
        'G': 'Grand Coronne / Novo Mesto',
        'H': 'Haren',
        'J': 'Billancourt',
        'K': 'Dieppe',
        'N': 'Mexico',
        'P': 'Mexico',
        'R': 'Bursa / Moscow',
        'S': 'Sandouville',
        'T': 'Romorantin',
        'U': 'Maubeuge',
        'W': 'Valladolid',
        'X': 'Heuliez',
        'Z': 'USA',  # ? city
    })

    transmission = Detail(('vds', 5), {
        '1': 'Automatic, 3-Gears',
        '2': 'Automatic, 4-Gears',
        '4': 'Manual, 5-Gears',
        '5': 'Manual, 5-Gears',
        '8': 'Manual, 5-Gears, 4x4',
        'C': 'Manual, 5-Gears',
        'D': 'Manual, 5-Gears',
    })

    serial = Detail(('vis', slice(1, None)))
