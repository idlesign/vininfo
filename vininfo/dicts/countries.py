# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


def __unpack_countries_map(counties):
    unpacked = {}

    seq = 'ABCDEFGHJKLMNPRSTUVWXYZ1234567890'

    for code, title in counties.items():
        first, _, span  = code.partition('-')

        if span:
            ch_from, ch_till = span

        else:
            ch_from = 'A'
            ch_till = '0'

        for ch in seq[seq.index(ch_from):seq.index(ch_till) + 1]:
            unpacked[first + ch] = title

    return unpacked


COUNTRIES = __unpack_countries_map({
    'A-AH': 'South Africa',
    'A-JN': "Cote d'Ivoire",
    'B-AE': 'Angola',
    'B-FK': 'Kenya',
    'B-LR': 'Tanzania',
    'C-AE': 'Benin',
    'C-FK': 'Madagascar',
    'C-LR': 'Tunisia',
    'D-AE': 'Egypt',
    'D-FK': 'Morocco',
    'D-LR': 'Zambia',
    'E-AE': 'Ethiopia',
    'E-FK': 'Mozambique',
    'F-AE': 'Ghana',
    'F-FK': 'Nigeria',
    'J-': 'Japan',
    'K-AE': 'Sri Lanka',
    'K-FK': 'Israel',
    'K-LR': 'Korea (South)',
    'K-S0': 'Kazakhstan',
    'L-': 'China (Mainland)',
    'M-AE': 'India',
    'M-FK': 'Indonesia',
    'M-LR': 'Thailand',
    'M-S0': 'Myanmar',
    'N-AE': 'Iran',
    'N-FK': 'Pakistan',
    'N-LR': 'Turkey',
    'P-AE': 'Philippines',
    'P-FK': 'Singapore',
    'P-LR': 'Malaysia',
    'R-AE': 'United Arab Emirates',
    'R-FK': 'Taiwan, China',
    'R-LR': 'Vietnam',
    'R-S0': 'Saudi Arabia',
    'S-AM': 'United Kingdom',
    'S-NT': 'Germany/East Germany',
    'S-UZ': 'Poland',
    'S-14': 'Latvia',
    'T-AH': 'Switzerland',
    'T-JP': 'Czech Republic',
    'T-RV': 'Hungary',
    'T-W1': 'Portugal',
    'U-HM': 'Denmark',
    'U-NT': 'Ireland',
    'U-UZ': 'Romania',
    'U-57': 'Slovakia',
    'V-AE': 'Austria',
    'V-FR': 'France',
    'V-SW': 'Spain',
    'V-X2': 'Serbia',
    'V-35': 'Croatia',
    'V-60': 'Estonia',
    'W-': 'Germany/West Germany',
    'X-AE': 'Bulgaria',
    'X-FK': 'Greece',
    'X-LR': 'Netherlands',
    'X-SW': 'USSR/CIS',
    'X-X2': 'Luxembourg',
    'X-30': 'Russia',
    'Y-AE': 'Belgium',
    'Y-FK': 'Finland',
    'Y-LR': 'Malta',
    'Y-SW': 'Sweden',
    'Y-X2': 'Norway',
    'Y-35': 'Belarus',
    'Y-60': 'Ukraine',
    'Z-AR': 'Italy',
    'Z-X2': 'Slovenia',
    'Z-35': 'Lithuania',
    '1-': 'United States',
    '2-': 'Canada',
    '3-AW': 'Mexico',
    '3-X7': 'Costa Rica',
    '3-89': 'Cayman Islands',
    '4-': 'United States',
    '5-': 'United States',
    '6-': 'Australia',
    '7-': 'New Zealand',
    '8-AE': 'Argentina',
    '8-FK': 'Chile',
    '8-LR': 'Ecuador',
    '8-SW': 'Peru',
    '8-X2': 'Venezuela',
    '9-AE': 'Brazil',
    '9-FK': 'Colombia',
    '9-LR': 'Paraguay',
    '9-SW': 'Uruguay',
    '9-X2': 'Trinidad & Tobago',
    '9-39': 'Brazil',
})
