# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ._base import VinDetails
from ..dicts.bodies import *


class AvtoVazDetails(VinDetails):
    """AvtoVAZ VIN details extractor."""

    MODELS = {
        'GA': 'XRAY',
        'GF': 'Vesta',
    }

    BODIES = {
        'B': BODY_HATCH_5,
        'K': BODY_SW_5,
        'L': BODY_SEDAN_4,
    }

    ENGINES = {
        '1': '21129',
        '2': '11189',
        '3': '21179',
        '4': 'H4M',
        'A': '21129 CNG',
    }

    TRANSMISSION = {
        '1': 'Manual VAZ',
        '2': 'Semi-automatic',
        '3': 'Manual Renault',
    }

    PLANTS = {
        '0': 'Tolyatti',
        'Y': 'Izhevsk',
    }

    @property
    def model_code(self):
        return self._vin.vds[:2]

    @property
    def body_code(self):
        return self._vin.vds[2]

    @property
    def engine_code(self):
        return self._vin.vds[3]

    @property
    def transmission_code(self):
        return self._vin.vds[4]

    @property
    def plant_code(self):
        return self._vin.vis[1]

    @property
    def serial(self):
        return self._vin.vis[2:]
