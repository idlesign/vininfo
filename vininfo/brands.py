# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from .common import Brand
from .details import *


class Lada(Brand):

    extractor = AvtoVazDetails


class Nissan(Brand):

    extractor = NissanDetails

