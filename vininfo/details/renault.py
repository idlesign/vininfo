# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ._base import VinDetails


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
        '2': '2-Door Sedan',
        '3': '3-Door Hatchback',
        '4': '4-Door Sedan',
        '5': '5-Door Hatchback',
        '6': '5-Door Station Wagon',
        '7': '2-Door Cabriolet',
        '8': '2-Door Coupe',
        'A': '3-Door Station Wagon',
        'B': '5-Door Hatchback',
        'C': '3-Door Hatchback',
        'D': '2-Door Coupe',
        'E': '2-Door Cabriolet',
        'F': 'Van',
        'G': '3-Door Minivan',
        'J': '5-Door Minivan',
        'H': '2-Door Pickup',
        'K': '3-Door Station Wagon',
        'L': '4-Door Sedan',
        'M': '2-Door Sedan',
        'N': '5-Door Minivan',
        'S': '5-Door Station Wagon',
        'U': '2-Door Pickup',
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
