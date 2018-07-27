from .toolbox import Vin
from .exceptions import ValidationError, VininfoException


VERSION = (0, 2, 0)
"""Application version number tuple."""

VERSION_STR = '.'.join(map(str, VERSION))
"""Application version number string."""