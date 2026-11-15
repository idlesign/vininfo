from ..dicts.bodies import *
from ..dicts.doors import *
from ._base import Detail, VinDetails

_PLANT_SINDELFINGEN = 'Sindelfingen, Germany'
_PLANT_VANCE = 'Vance, AL, US'


def get_plant(details):
    """Plant code meaning differs between Germany-built and US-built vehicles."""
    if details._vin.wmi in {'4JG', '55S'}:
        return {
            'A': _PLANT_VANCE,
            'B': _PLANT_VANCE,
            'U': _PLANT_VANCE,
        }

    return {
        '1': 'Pune, India',
        'A': _PLANT_SINDELFINGEN,
        'B': _PLANT_SINDELFINGEN,
        'C': _PLANT_SINDELFINGEN,
        'D': _PLANT_SINDELFINGEN,
        'E': [_PLANT_SINDELFINGEN, 'Juiz de Fora, Brazil', 'Mishawaka, IN, US'],
        'F': 'Bremen, Germany',
        'G': 'Bremen, Germany',
        'H': 'Bremen, Germany',
        'J': 'Rastatt, Germany',
        'K': 'Rastatt, Germany',
        'L': 'Pekan, Malaysia',
        'M': 'Woking, United Kingdom',
        'N': 'Kecskemet, Hungary',
        'P': 'Kecskemet, Hungary',
        'R': 'East London, South Africa',
        'S': 'East London, South Africa',
        'T': 'Osnabrück, Germany',
        'U': _PLANT_SINDELFINGEN,
        'V': 'Uusikaupunki, Finland',
        'W': 'Aguascalientes, Mexico',
        'X': 'Graz, Austria',
    }


class MercedesBenzDetails(VinDetails):
    """Mercedes-Benz North America VIN details extractor."""

    # Position 4: model line. Codes repeat across eras, hence candidate lists.
    model = Detail(('vds', 0), {
        'A': ['W123 300-Class', 'C199/R199/Z199 SLR McLaren', 'W206 C-Class', 'W163 M-Class'],
        'B': ['R107 SL-Class', 'C107 SLC-Class', 'W164 M-Class', 'X164 GL-Class'],
        'C': ['W126/C126 S-Class', 'V297 EQS-Class', 'W251 R-Class'],
        'D': ['W201 190-Class', 'C219 CLS-Class', 'W166 M/GLE-Class', 'X166 GL/GLS-Class', 'X296 EQS-Class SUV'],
        'E': ['W124 300/E-Class', 'C216 CL-Class', 'V295 EQE-Class', 'C292 GLE-Class Coupe'],
        'F': ['R129 SL-Class', 'W245 B-Class', 'W167/C167 GLE-Class', 'X167 GLS-Class', 'C174 CLA-Class'],
        'G': ['W140/C140 S-Class', 'W204 C-Class', 'X204 GLK-Class', 'X294 EQE-Class SUV'],
        'H': ['W202 C-Class', 'W212/S212 E-Class'],
        'J': ['W210 E-Class', 'R231 SL-Class'],
        'K': ['R170 SLK-Class', 'C207/A207 E-Class Coupe/Convertible', 'X254/C254 GLC-Class'],
        'L': ['C208/A208 CLK-Class', 'C218 CLS-Class', 'W214/X214 E-Class'],
        'M': ['W246 B-Class', 'C236/A236 CLE-Class'],
        'N': ['W220 S-Class', 'W221 S-Class'],
        'P': ['C215 CL-Class', 'R172 SLK/SLC-Class'],
        'R': ['W203 C-Class', 'C197/R197 SLS AMG', 'C192 AMG GT'],
        'S': ['R230 SL-Class', 'C117 CLA-Class'],
        'T': ['C209/A209 CLK-Class', 'X156 GLA-Class'],
        'U': ['W211 E-Class', 'W222 S-Class'],
        'V': ['W240 Maybach 57/62', 'N242 B-Class Electric', 'R232 SL-Class'],
        'W': ['R171 SLK-Class', 'W205 C-Class', 'W465 G-Class'],
        'X': 'C217/A217 S-Class Coupe/Convertible',
        'Y': ['C190/R190 AMG GT', 'W463 G-Class'],
        'Z': 'W213/S213/X213 E-Class',
        '0': 'X253/C253 GLC-Class',
        '1': 'C238/A238 E-Class Coupe/Convertible',
        '2': 'C257 CLS-Class',
        '3': ['V177 A-Class Sedan', 'W177 A-Class Hatchback'],
        '4': ['H247 GLA-Class', 'X247 GLB-Class'],
        '5': 'C118 CLA-Class',
        '6': 'W223 S-Class',
        '7': 'X290 AMG GT 4-Door Coupe',
        '9': 'X243 EQB-Class',
    })

    # Position 5: body style. Codes are shared between passenger cars and SUVs.
    body = Detail(('vds', 1), {
        'A': BODY_CROSS,
        'B': [BODY_SEDAN, BODY_CROSS],
        'C': BODY_CROSS,
        'D': BODY_CROSS,
        'F': [BODY_SEDAN, BODY_HATCH, BODY_CROSS],
        'G': [BODY_SEDAN, BODY_HATCH, BODY_CROSS],
        'H': [BODY_SW, BODY_HATCH, BODY_CROSS],
        'J': [BODY_COUPE, BODY_CROSS],
        'K': BODY_CABRI,
        'M': BODY_CROSS,
        'N': [BODY_HATCH, BODY_CROSS],
        'P': BODY_HATCH,
        'R': BODY_CROSS,
        'X': [BODY_SEDAN, BODY_COUPE, BODY_CABRI, BODY_CROSS],
    })

    doors = Detail(('vds', 1), {
        'A': DOORS_4,
        'B': DOORS_4,
        'C': DOORS_4,
        'D': DOORS_4,
        'F': DOORS_4,
        'G': DOORS_4,
        'H': [DOORS_4, DOORS_5],
        'J': [DOORS_2, DOORS_4],
        'K': DOORS_2,
        'M': DOORS_4,
        'N': [DOORS_3, DOORS_4],
        'P': DOORS_5,
        'R': DOORS_4,
        'X': [DOORS_2, DOORS_4, DOORS_5],
    })

    plant = Detail(('vis', 1), get_plant)

    serial = Detail(('vis', slice(2, None)))
