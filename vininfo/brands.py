from .common import Brand
from .details import *


class Lada(Brand):

    extractor = AvtoVazDetails


class Nissan(Brand):

    extractor = NissanDetails


class Opel(Brand):

    extractor = OpelDetails


class Renault(Brand):

    extractor = RenaultDetails
