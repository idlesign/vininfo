from typing import Dict


def __unpack_countries_map(counties: Dict[str, str]) -> Dict[str, str]:
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


# ISO 3780
# https://standards.iso.org/iso/3780/
# `docs/Current WMI World Codes chart_Sept 2015.pdf`
COUNTRIES = __unpack_countries_map({
    'A-AH': 'South Africa',
    'A-JK': 'Ivory Coast',
    'A-LM': 'Lesotho',
    'A-NP': 'Botswana',
    'A-RS': 'Namibia',
    'A-TU': 'Madagascar',
    'A-VW': 'Mauritius',
    'A-XY': 'Tunisia',
    'A-Z1': 'Cyprus',
    'A-23': 'Zimbabwe',
    'A-45': 'Mozambique',
    'B-AB': 'Angola',
    'B-FG': 'Kenya',
    'B-LL': 'Nigeria',
    'B-RR': 'Algeria',
    'B-34': 'Libya',
    'C-AB': 'Egypt',
    'C-FG': 'Morocco',
    'C-LM': 'Zambia',
    'H-': 'China',
    'J-': 'Japan',
    'K-FH': 'Israel',
    'K-LR': 'South Korea',
    'K-ST': 'Jordan',
    'L-': 'China',
    'M-AE': 'India',
    'M-FK': 'Indonesia',
    'M-LR': 'Thailand',
    'M-SS': 'Myanmar',
    'M-UU': 'Mongolia',
    'M-XX': 'Kazakhstan',
    'M-16': 'India',
    'N-AE': 'Iran',
    'N-FG': 'Pakistan',
    'N-JJ': 'Iraq',
    'N-LR': 'Turkey',
    'N-ST': 'Uzbekistan',
    'N-UU': 'Azerbaijan',
    'N-YY': 'Armenia',
    'N-15': 'Iran',
    'P-AC': 'Philippines',
    'P-FG': 'Singapore',
    'P-LR': 'Malaysia',
    'P-ST': 'Bangladesh',
    'R-AB': 'United Arab Emirates',
    'R-FK': 'Taiwan',
    'R-LN': 'Vietnam',
    'R-PP': 'Laos',
    'R-ST': 'Saudi Arabia',
    'R-UW': 'Russia',
    'R-11': 'Hong Kong',
    'S-AM': 'United Kingdom',
    'S-NT': 'Germany',
    'S-UZ': 'Poland',
    'S-12': 'Latvia',
    'S-33': 'South Ossetia',
    'T-AH': 'Switzerland',
    'T-JP': 'Czech Republic',
    'T-RV': 'Hungary',
    'T-W2': 'Portugal',
    'T-35': 'Serbia & Montenegro',
    'T-66': 'Andorra',
    'U-AC': 'Spain',
    'U-HM': 'Denmark',
    'U-NR': 'Ireland',
    'U-UW': 'Romania',
    'U-12': 'Macedonia',
    'U-57': 'Slovakia',
    'U-80': 'Bosnia & Herzogovina',
    'V-AE': 'Austria',
    'V-FR': 'France',
    'V-SW': 'Spain',
    'V-35': 'Croatia',
    'V-68': 'Estonia',
    'W-': 'Germany',
    'X-AC': 'Bulgaria',
    'X-DE': 'Russia',
    'X-FH': 'Greece',
    'X-JK': 'Russia',
    'X-LR': 'Netherlands',
    'X-SW': 'Russia',
    'X-XY': 'Luxembourg',
    'X-Z0': 'Russia',
    'Y-AE': 'Belgium',
    'Y-FK': 'Finland',
    'Y-NN': 'Malta',
    'Y-SW': 'Sweden',
    'Y-X2': 'Norway',
    'Y-35': 'Belarus',
    'Y-68': 'Ukraine',
    'Z-AU': 'Italy',
    'Z-XZ': 'Slovenia',
    'Z-11': 'San Marino',
    'Z-35': 'Lithuania',
    'Z-60': 'Russia',
    '1-': 'United States',
    '2-A5': 'Canada',
    '3-AX': 'Mexico',
    '3-55': 'Dom. Republic',
    '3-66': 'Honduras',
    '3-77': 'Panama',
    '3-89': 'Puerto Rico',
    '4-': 'United States',
    '5-': 'United States',
    '6-AX': 'Australia',
    '6-Y1': 'New Zealand',
    '7-': 'United States',
    '8-AE': 'Argentina',
    '8-FG': 'Chile',
    '8-LN': 'Ecuador',
    '8-ST': 'Peru',
    '8-XZ': 'Venezuela',
    '8-22': 'Bolivia',
    '9-AE': 'Brazil',
    '9-FG': 'Colombia',
    '9-SV': 'Uruguay',
    '9-39': 'Brazil',
})
