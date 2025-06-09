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


class Dafra(Brand):

    extractor = DafraDetails


class Bajaj(Brand):

    extractor = BajajDetails