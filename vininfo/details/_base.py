# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ..common import Annotatable

if False:  # pragma: nocover
    from ..toolbox import Vin


class DetailWrapper(object):

    __slots__ = ['code', 'name']

    def __init__(self, details, detail):
        """
        :param VinDetails details:
        :param Detail detail: 
        """
        vin = details._vin
        attr_name, attr_idx = detail.source
        code_source = getattr(vin, attr_name)

        code = code_source[attr_idx]

        defs = detail.defs

        if callable(defs):
            defs = defs(details)

        self.code = code
        self.name = defs.get(code)

    def __str__(self):
        return self.name or self.code


class Detail(object):
    """Vin detail descriptor."""

    __slots__ = ['source', 'defs']

    def __init__(self, code_source=None, definitions=None):
        self.source = code_source
        self.defs = definitions or {}

    def __get__(self, instance, owner):
        """
        :param VinDetails instance:
        :param owner:
        :rtype: DetailWrapper
        """

        return DetailWrapper(instance, self)


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

    def __init__(self, vin):
        """
        :param Vin vin:
        """
        self._vin = vin
        # self._cached = {}

    body = Detail()
    engine = Detail()
    model = Detail()
    plant = Detail()
    transmission = Detail()
    serial = Detail()
