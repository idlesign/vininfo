# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ..common import Annotatable


class VinDetails(Annotatable):
    """Offers advanced (manufacturer specific) VIN data extraction ficilities."""

    annotate_titles = {
        'body': 'Body',
        'engine': 'Engine',
        'model': 'Model',
        'plant': 'Plant',
        'transmission': 'Transmission',
        'serial': 'Serial',
    }

    MODELS = {}
    ENGINES = {}
    BODIES = {}
    PLANTS = {}

    def __init__(self, vin):
        """
        :param Vin vin:
        """
        self._vin = vin

    @property
    def engine(self):
        return self.ENGINES.get(self.engine_code)

    @property
    def model(self):
        return self.MODELS.get(self.model_code)

    @property
    def body(self):
        return self.BODIES.get(self.body_code)

    @property
    def plant(self):
        return self.PLANTS.get(self.plant_code)
