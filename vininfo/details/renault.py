# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ._base import VinDetails
from ..dicts.bodies import *


class RenaultDetails(VinDetails):
    """Renault VIN details extractor."""

    MODELS = {
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
    }

    BODIES = {
        '2': BODY_SEDAN_2,
        '3': BODY_HATCH_3,
        '4': BODY_SEDAN_4,
        '5': BODY_HATCH_5,
        '6': BODY_SW_5,
        '7': BODY_CABRI_2,
        '8': BODY_COUPE_2,
        'A': BODY_SW_3,
        'B': BODY_HATCH_5,
        'C': BODY_HATCH_3,
        'D': BODY_COUPE_2,
        'E': BODY_CABRI_2,
        'F': BODY_VAN,
        'G': BODY_MINIVAN_3,
        'J': BODY_MINIVAN_5,
        'H': BODY_PICKUP_2,
        'K': BODY_SW_3,
        'L': BODY_SEDAN_4,
        'M': BODY_SEDAN_2,
        'N': BODY_MINIVAN_5,
        'S': BODY_SW_5,
        'U': BODY_PICKUP_2,
    }

    TRANSMISSION = {
        '1': 'Automatic, 3-Gears',
        '2': 'Automatic, 4-Gears',
        '4': 'Manual, 5-Gears',
        '5': 'Manual, 5-Gears',
        '8': 'Manual, 5-Gears, 4x4',
        'C': 'Manual, 5-Gears',
        'D': 'Manual, 5-Gears',
    }

    PLANTS = {
        'A': 'Portugal',
        'B': 'Batilly',
        'С': 'Creil',
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
    }

    @property
    def model_code(self):
        return self._vin.vds[1]

    @property
    def body_code(self):
        return self._vin.vds[0]

    @property
    def plant_code(self):
        return self._vin.vds[4]

    @property
    def transmission_code(self):
        return self._vin.vds[5]

    @property
    def serial(self):
        return self._vin.vis[1:]
