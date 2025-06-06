from .brands import Bajaj, Dafra
from .common import Assembler


class Dafra(Assembler):
    brands = {Dafra(), Bajaj(), 'BMW'}