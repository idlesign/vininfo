import re
from datetime import datetime, timezone
from typing import TYPE_CHECKING, ClassVar

from .common import Annotatable, Assembler, Brand, UnsupportedBrand
from .dicts import COUNTRIES, REGIONS, WMI
from .exceptions import ValidationError

if TYPE_CHECKING:
    from .details._base import VinDetails


class Vin(Annotatable):
    """Offers basic VIN data extraction facilities."""

    annotate_titles: ClassVar = {
        'manufacturer': 'Manufacturer',
        'region': 'Region',
        'country': 'Country',
        'years': 'Years',
    }

    def __init__(self, num: str):
        self._brand = None
        self.num = self.validate(num)

        _details  = None
        for brand in self.assembler.brands:
            if isinstance(brand, str):
                brand = Brand(brand)
            details_extractor = brand.extractor

            if details_extractor:
                _details = details_extractor(self)
                if _details.model and _details.model.name:
                    self._brand = brand
                    break

        self.details: VinDetails = _details

    def __str__(self):
        return self.num

    @classmethod
    def validate(cls, num: str) -> str:
        """Performs basic VIN validation and sanation.

        :param num:

        """
        num = num.strip().upper()

        num_len = len(num)
        if num_len != 17:
            raise ValidationError(f'VIN number requires 17 chars ({num_len} given)')

        pattern = r"^[A-HJ-NPR-Z0-9]{17}$"
        if not re.match(pattern, num):
            raise ValidationError("VIN number must only contain alphanumeric symbols except 'I', 'O', and 'Q' ")

        return num

    def verify_checksum(self, *, check_year: bool = True) -> bool:
        """Performs checksum verification.

        .. warning:: Not every manufacturer uses VIN checksum rules.

        :param check_year: Whether to also check the model year.
            Note that not all manufacturer abey the rule. Default: True.

        """
        if check_year and self.vis[0] in {'U', 'Z', '0'}:
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

        return f'{check_digit}' == self.vds[5]

    @property
    def wmi(self) -> str:
        """WMI (World Manufacturers Identification)"""
        return self.num[:3]

    @property
    def assembler(self) -> Assembler:
        """Assembler object."""

        wmi = self.wmi

        assembler = WMI.get(wmi)

        if not assembler:
            assembler = WMI.get(wmi[:2])

        if isinstance(assembler, str):
            assembler = Brand(assembler)

        if assembler is None:
            assembler = UnsupportedBrand()

        return assembler

    @property
    def brand(self) -> Brand:
        """Brand object."""
        brand = self._brand
        return UnsupportedBrand() if brand is None else brand

    @property
    def manufacturer(self) -> str:
        """Manufacturer title."""
        return self.assembler.manufacturer

    @property
    def manufacturer_is_small(self) -> bool:
        """A manufacturer who builds fewer than 1000 vehicles per year."""
        return f'{self.wmi[2]}' == '9'

    @property
    def vds(self) -> str:
        """VDS (Vehicle Descriptor Section)"""
        return self.num[3:9]

    @property
    def vis(self) -> str:
        """VIS (Vehicle Identifier Section)"""
        return self.num[9:17]

    @property
    def region_code(self) -> str:
        return self.wmi[0]

    @property
    def region(self) -> str | None:
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
    def country(self) -> str | None:
        return COUNTRIES.get(self.country_code)

    @property
    def years_code(self) -> str:
        return self.vis[0]

    @property
    def years(self) -> list[int]:
        letters = 'ABCDEFGHJKLMNPRSTVWXY123456789'
        overflow_delta = len(letters)
        start_year_iso_table = 1980
        net_year = datetime.now(tz=timezone.utc).year + 1
        delta = letters.index(self.years_code)
        year = delta + start_year_iso_table
        result = [year]
        while year + overflow_delta <= net_year:
            year += overflow_delta
            result.append(year)

        result.sort(reverse=True)

        return result

    @property
    def squish_vin(self) -> str:
        """Squish (or Pattern) VIN.

        The first 11 digits of the VIN minus the 9th digit (positions 1-8,
        positions 10 and 11).

        Squish VIN encodes vehicle information while preventing its precise
        identification. It can be useful for anonymization and privacy purposes.
        """
        return self.num[:8] + self.num[9:11]
