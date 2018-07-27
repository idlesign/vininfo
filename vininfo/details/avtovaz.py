# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ..dicts import COACHWORK_HATCH, COACHWORK_SW, COACHWORK_SEDAN

from ._base import VinDetails


class AvtoVazDetails(VinDetails):
    """AvtoVAZ VIN details extractor."""

    MODELS = {
        'GA': 'XRAY',
        'GF': 'Vesta',
    }

    COACHWORKS = {
        'B': COACHWORK_HATCH,
        'K': COACHWORK_SW,
        'L': COACHWORK_SEDAN,
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
    def model(self):
        return self.MODELS.get(self.model_code)

    @property
    def coachwork_code(self):
        return self._vin.vds[2]

    @property
    def coachwork(self):
        return self.COACHWORKS.get(self.coachwork_code)

    @property
    def engine_code(self):
        return self._vin.vds[3]

    @property
    def engine(self):
        return self.ENGINES.get(self.engine_code)

    @property
    def transmission_code(self):
        return self._vin.vds[4]

    @property
    def transmission(self):
        return self.TRANSMISSION.get(self.engine_code)

    @property
    def plant_code(self):
        return self._vin.vis[1]

    @property
    def plant(self):
        return self.PLANTS.get(self.plant_code)

    @property
    def serial(self):
        return self._vin.vis[2:]
