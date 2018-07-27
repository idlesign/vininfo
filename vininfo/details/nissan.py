# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ..dicts import BODY_HATCH, BODY_SW, BODY_SEDAN

from ._base import VinDetails


class NissanDetails(VinDetails):
    """Nissan VIN details extractor."""

    MODELS = {
        'A': ['Armada', 'Titan', 'Maxima'],
        'B': ['Sentra'],
        'C': ['Versa (07-11)'],
        'D': ['Truck', 'Xterra (00-04)', 'Frontier'],
        'J': ['Maxima'],
        'N': ['Xterra (05-11)'],
        'R': ['Pathfinder'],
        'S': ['240SX', 'Rogue (08-11)'],
        'U': ['Altima'],
        'Z': ['300Z', '350Z', 'Murano'],
    }

    BODIES = {
        '1': ['4-Door Sedan', 'Standard Body Truck'],
        '4': ['2-Door Coupe'],
        '5': ['4-Door Wagon'],
        '6': ['2-Door Convertible', 'Fastback', 'King Cab Truck'],
        '7': ['Crew Cab Truck'],
        '8': ['8-Door Wagon'],
    }

    ENGINES = {
        'A': ['VG30D', 'VK45DE', 'VQ35DE', 'VK56DE', 'VQ40DE', 'QR25DE'],
        'B': ['KA24DE', 'SR20DE', 'VQ35HR', 'MR18DE', 'QR25DE'],
        'C': ['SR20DE', 'VG30DETT', 'QG18DE'],
        'D': ['KA24DE', 'QG18DE', 'VQ35DE'],
        'E': ['VE30DE', 'GA16DE', 'VG33E'],
        'F': ['KA24E'],
        'H': ['VG30E'],
        'M': ['KA24DE', 'VG33ER'],
        'N': ['VH45DE'],
        'R': ['VG30DE'],
        'S': ['KA24E'],
        'T': ['VG33E'],
    }

    PLANTS = {
        'C': ['Smyrna'],
        'L': ['Aguas Calientes'],
        'M': ['Tochigi'],
        'N': ['Canton'],
        'T': ['Tochigi', 'Oppama'],
        'W': ['Kyushyu'],
    }

    @property
    def model_code(self):
        return self._vin.vds[1]

    @property
    def body_code(self):
        return self._vin.vds[3]

    @property
    def engine_code(self):
        return self._vin.vds[0]

    @property
    def plant_code(self):
        return self._vin.vis[1]

    @property
    def serial(self):
        return self._vin.vis[2:]
