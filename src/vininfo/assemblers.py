from typing import ClassVar

from .brands import Bajaj
from .brands import Dafra as DafraBrand
from .common import Assembler


class Dafra(Assembler):
    brands: ClassVar = {DafraBrand(), Bajaj(), 'BMW'}
