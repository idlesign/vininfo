from datetime import datetime
from itertools import cycle
from typing import Optional, List

from .common import Annotatable, Brand, UnsupportedBrand
from .dicts import COUNTRIES, WMI, REGIONS
from .exceptions import ValidationError

if False:  # pragma: nocover
    from .details._base import VinDetails  # noqa


class Vin(Annotatable):
    """Offers basic VIN data extraction facilities."""

    annotate_titles = {
        'manufacturer': 'Manufacturer',
        'region': 'Region',
        'country': 'Country',
        'years': 'Years',
    }

    def __init__(self, num: str):
        self.num = self.validate(num)

        details_extractor = self.brand.extractor

        if details_extractor:
            details_extractor = details_extractor(self)

        self.details: VinDetails = details_extractor

    def __str__(self):
        return self.num

    @classmethod
    def validate(self, num: str) -> str:
        """Performs basic VIN validation and sanation.

        :param num:

        """
        num = num.strip().upper()

        num_len = len(num)
        if num_len != 17:
            raise ValidationError(f'VIN number requires 17 chars ({num_len} given)')

        illegal = {'I', 'O', 'Q'}

        for ch in num:
            if ch in illegal:
                raise ValidationError(f"VIN number should not contain: {', '.join(illegal)}")

        return num

    def verify_checksum(self) -> bool:
        """Performs checksum verification.

        .. warning:: Not every manufacturer uses VIN checksum rules.

        """
        if self.vis[0] in {'U', 'Z', '0'}:
            return False

        trans = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,         'P': 7,         'R': 9,
                    'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9,
        }
        weights = (8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2)

        checksum = 0

        for pos, char in enumerate(self.num):
            value = int(trans.get(char, char))
            checksum += (value * weights[pos])

        checksum = int(checksum) % 11

        check_digit = 'X' if checksum == 10 else checksum

        return str(check_digit) == self.vds[5]

    @property
    def wmi(self) -> str:
        """WMI (World Manufacturers Identification)"""
        return self.num[:3]

    @property
    def brand(self) -> Brand:
        """Brand object."""

        wmi = self.wmi

        brand = WMI.get(wmi)

        if not brand:
            brand = WMI.get(wmi[:2])

        if isinstance(brand, str):
            brand = Brand(brand)

        if brand is None:
            brand = UnsupportedBrand()

        return brand

    @property
    def manufacturer(self) -> str:
        """Manufacturer title."""
        return self.brand.manufacturer

    @property
    def manufacturer_is_small(self) -> bool:
        """A manufacturer who builds fewer than 1000 vehicles per year."""
        return str(self.wmi[2]) == '9'

    @property
    def vds(self) -> str:
        """VDS (Vehicle Description Section)"""
        return self.num[3:9]

    @property
    def vis(self) -> str:
        """VIS (Vehicle Identifier Section)"""
        return self.num[9:17]

    @property
    def region_code(self) -> str:
        return self.wmi[0]

    @property
    def region(self) -> Optional[str]:
        code = self.region_code

        title = None

        for chars, title_ in REGIONS.items():
            if code in chars:
                title = title_
                break

        return title

    @property
    def country_code(self) -> str:
        return self.wmi[0:2]

    @property
    def country(self) -> Optional[str]:
        return COUNTRIES.get(self.country_code)

    @property
    def years(self) -> List[int]:
        letters = 'ABCDEFGHJKLMNPRSTVWXY123456789'
        year_letter = self.vis[0]

        year = 1979
        year_current = datetime.now().year

        result = []

        for letter in cycle(letters):
            year += 1

            if letter == year_letter:
                result.append(year)

            if year == year_current:
                break

        result.sort(reverse=True)

        return result
