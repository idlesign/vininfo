from ._base import VinDetails, Detail
from ..dicts.bodies import *

engine_prior_to_1996 = Detail(
    ('vds', 0), {
        '4': '7A-FE Lean Burn',
        'A': '3MZ-FE',
        'B': ['1NZ-FXE', '2AZ-FXE'],
        'D': '2AZ-FE',
        'E': '2AZ-FE',
        'F': '1MZ-FE',
        'G': '5S-FE',
        'H': '1AZ-FE',
        'K': '2GR-FE',
        'L': '2RZ-FE',
        'M': '3RZ-FE',
        'N': '5VZ-FE',
        'P': '3S-FE',
        'R': '1ZZ-FE',
        'S': '1BM',
        'T': ['2UZ-FE', '1NZ-FE', '3S-GTE'],
        'U': '1GR-FE',
        'Y': '2ZZ-GE',
    })

engine_since_1996 = Detail(
    ('vds', 1), {
        'A': ['4A-FE', '7A-FE', '2AD-FTV (2005+)'],
        'B': ['1HZ', '2AD-FHV (2005+)'],
        'C': ['2C', '2CT', '2CT-E'],
        'E': ['2JZ-GT', '2JZ-GTE', '2AZ-FE'],
        'F': ['1MZ-FE', '2AR-FE'],
        'H': ['1AZ-FE', '1NR-FE'],
        'J': ['1FZ-FE', '1AZ-FSE'],
        'N': ['5VZ-FE', '2ZR-FXE'],
        'P': '2AZ-FSE',
        'R': '1ZZ-FE',
        'S': ['3S-FE', 'Electric (RAV4 EV only)'],
        'T': '2UZ-FE',
        'U': '2ZR-FE (Corolla Conquest 2010)',
        'V': ['1NR-FE', '1VD-FTV'],
        'W': ['2NZ-FE', '1CD-FTV'],
        'X': '2TR-FE',
        'Y': ['2ZZ-GE', '3UR-FE'],
        'Z': ['3.5L 2GR-FKS V6 (278 hp)', '2JZ-FE', '1ZZ-FE', '3ZZ-FE'],
    })


class ToyotaDetails(VinDetails):
    """Toyota VIN details extractor."""

    # TODO: get year from VIN
    # 1) Does the current design allow it, or should it evolve?
    # 2) Add `most_likely_year` property to VIN?
    year = 2010

    model = Detail(
        ('vds', 4), {
            '0': ['MR2', 'MR2 Spyder'],
            '1': 'Tundra',
            '3': ['Echo', 'Yaris Verso'],
            '4': ['Yaris', 'Scion xA', 'Scion xB', 'Scion xD', 'Urban Cruiser'],
            '6': 'Hilux',
            '7': 'Scion tC',
            'A': ['Highlander', 'Sequoia', 'Celica RWD', 'Supra'],
            'B': ['Avalon', 'Avensis Verso', 'Ipsum'],
            'C': ['Sienna', 'Previa', 'Aygo'],
            'D': 'T100',
            'E': ['Corolla', 'Matrix', 'Auris'],
            'F': 'FJ Cruiser',
            'G': ['Hilux', 'Fortuner'],
            'H': 'Highlander',
            'J': ['Land Cruiser', 'Land Cruiser Prado'],
            'K': ['Camry', 'Aurion (TRD)'],
            'L': ['Tercel', 'Paseo', 'Avensis'],
            'M': 'Previa',
            'N': ['Tacoma', 'older trucks'],
            'P': ['Camry Solara'],
            'R': ['4Runner', 'Corolla Verso'],
            'S': 'Fortuner',
            'T': 'Celica',
            'U': 'Prius',
            'V': 'RAV4',
            'W': 'MR2 (non-spyder models)',
            'X': 'Cressida',
        })

    if year >= 1996:
        body = Detail(
            ('vds', 0), {
                'A': '2DR Sedan 2WD',
                'B': '4DR Sedan 2WD / Standard Cab Truck, 4WD, Standard Bed, Full-Size Frame',
                'C': '2DR Coupe 2WD',
                'D': '3/5DR Liftback, Double Cab Truck, 4WD, Extra Long Bed, Full-Size Frame',
                'E': 'Station Wagon, MPV, Double Cab Truck, 2WD, Extra Long Bed, Full-Size Frame',
                'F': '2DR Convertible 2WD',
                'G': '4DR Wagon 2WD',
                'H': '4DR Wagon 4WD',
                'J': '5DR Van AWD / Double Cab Truck, 2WD, Long Bed, Small Frame',
                'K': '5DR Wagon 2WD / Double Cab Truck, 2WD, Extra Long Bed, Small Frame',
                'L': '5DR Wagon 4WD / Double Cab Truck, 4WD, Long Bed, Small Frame',
                'M': '5DR Door Van 2WD / Double Cab Truck, 4WD, Extra Long Bed, Small Frame',
                'N': 'Standard Cab 1/2 Ton Truck, 2WD, Short Bed, Full-Size Frame',
                'P': 'Standard Cab 1/2 Ton Truck, 4WD, Short Bed, Full-Size Frame',
                'R': 'Standard Cab Truck, 4WD, Standard Bed, Full-Size Frame',
                'S': '3DR Liftback 4WD',
                'T': 'Extra Cab/Access Pickup, 2WD, Long Bed Small Frame',
                'U': 'Extra Cab/Access Pickup, 4WD, Long Bed Small Frame',
                'W': 'Extra Cab/Access Pickup, 4WD, Long Bed Small Frame TRD',
                'X': '5DR Sport Utility Wagon',
                'Y': 'Sport Van',
                'Z': '5DR Wagon 2WD',
            })

    engine = engine_since_1996 if year >= 1996 else engine_prior_to_1996

    plant = Detail(
        ('vis', 1), {
            '0': 'Japan',
            '1': 'Japan',
            '2': 'Japan',
            '3': 'Japan',
            '4': 'Japan',
            '5': 'Japan',
            '6': 'Japan',
            '7': 'Japan',
            '8': 'Japan',
            '9': 'Japan',
            'A': 'Onnaing-Valenciennes, France (TMMF)',
            'C': 'Cambridge, ON, CA (TMMC)',
            'D': 'Japan',
            'E': 'United Kingdom',
            'K': 'Japan',
            'J': 'Japan',
            'M': 'Baja CA, Mexico (TMMBC)',
            'N': 'Kolín, Czech Republic (TPCA)',
            'R': 'Lafayette, IN, US (Subaru of Indiana Automotive)',
            'S': 'Princeton, IN, US',
            'U': 'Georgetown, KY, US',
            'W': 'Woodstock, ON, CA (TMMC)',
            'X': 'San Antonio, TX, US',
            'Z': 'Fremont, CA, US (NUMMI)',
        })

    series = Detail(
        ('vds', 2), {
            '0': 'Toyota Land Cruiser J100/J105',
            '2': 'Toyota Land Cruiser Prado J120',
        })
    
    restraint = Detail(
        ('vds', 3), {
            '0': 'Manual Belts w/2 Airbags and Side Curtain Airbags',
            '1': 'Manual Belt / 1 STD (North America), No Airbags (International)',
            '2': 'Manual Belts w/2 Airbags (North America), 1 Airbag (Driver Seat) (International)',
            '3': 'Manual Belts w/2 Airbags (North America), 2 Front Airbags (International)',
            '6': 'Manual Belts w/2 Airbags, Side Airbags, Side Curtain Shield Airbags, and Knee Airbag (Driver Seat)',
            '7': 'Manual Belts w/2 Airbags and Knee Airbag (Driver Seat)',
            '8': 'Manual Belts w/2 Airbags and Side Airbags',
            '9': 'Manual Belts w/2 Airbags, Side Airbags, and Front Curtain Airbags.',
            'D': 'Manual Belts w/2 Airbags, Side Airbags, Three-Row Curtain Shield Airbags, and Knee Airbag',
            'F': 'Manual Belts w/2 Airbags, Side Airbags, and Knee Airbag',
        })

    serial = Detail(('vis', slice(2, None)))
