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


class FordAustralia(Brand):

    extractor = FordAustraliaDetails

    # Year letter at VIN position 11 (vis index 1), not SAE position 10.
    year_position = 1

    # Position 9 is a model code, not an SAE check digit.
    uses_sae_checkdigit = False