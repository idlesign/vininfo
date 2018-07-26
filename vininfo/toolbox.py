#! -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from itertools import cycle

from .common import Annotatable
from .details import DETAILS
from .dicts import COUNTRIES, WMI, REGIONS
from .exceptions import ValidationError


class Vin(Annotatable):
    """Offers basic VIN data extraction ficilities."""

    annotate_titles = {
        'manufacturer': 'Manufacturer',
        'region': 'Region',
        'country': 'Country',
        'years': 'Years',
    }

    def __init__(self, num):
        self.num = self.validate(num)

        details = DETAILS.get(self.wmi)

        if details:
            details = details(self)

        self.details = details

    def __str__(self):
        return self.num

    @classmethod
    def validate(self, num):
        """Performs basic VIN validation and sanation.

        :param str|unicode num:
        :rtype: str|unicode
        """
        num = num.strip().upper()

        if len(num) != 17:
            raise ValidationError('VIN number requires 17 chars')

        illegal = {'I', 'O', 'Q'}

        for ch in num:
            if ch in illegal:
                raise ValidationError('VIN number should not contain: %s' % ', '.join(illegal))

        return num

    def verify_checksum(self):
        """Performs checksum verification.

        .. warning:: Not every manufacturer uses VIN checksum rules.

        :rtype: bool

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
    def wmi(self):
        """WMI (World Manufacturers Identification)"""
        return self.num[:3]

    @property
    def manufacturer(self):
        wmi = self.wmi

        name = WMI.get(wmi)
        if not name:
            name = WMI.get(wmi[:2])

        return name

    @property
    def vds(self):
        """VDS (Vehicle Description Section)"""
        return self.num[3:9]

    @property
    def vis(self):
        """VIS (Vehicle Identifier Section)"""
        return self.num[9:17]

    @property
    def region_code(self):
        return self.wmi[0]

    @property
    def region(self):
        code = self.region_code

        title = None

        for chars, title_ in REGIONS.items():
            if code in chars:
                title = title_
                break

        return title

    @property
    def country_code(self):
        return self.wmi[0:2]

    @property
    def country(self):
        return COUNTRIES.get(self.country_code)

    @property
    def years(self):
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
