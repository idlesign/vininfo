from __future__ import unicode_literals

from ..common import Annotatable


class VinDetails(Annotatable):
    """Offers advanced (manufacturer specific) VIN data extraction ficilities."""

    annotate_titles = {
        'coachwork': 'Coachwork',
        'engine': 'Engine',
        'model': 'Model',
        'plant': 'Plant',
        'transmission': 'Transmission',
        'serial': 'Serial',
    }

    def __init__(self, vin):
        """
        :param Vin vin:
        """
        self._vin = vin
