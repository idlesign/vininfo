# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from ._base import VinDetails


class OpelDetails(VinDetails):
    """Opel VIN details extractor."""

    MODELS = {
        'F': 'Agila',
        'G': 'Insignia',
        'J': 'Mokka',
        'L': 'Antara',
        'M': 'Movano',
        'P': ['Astra J', 'Zafira C'],
        'R': 'Astra GTC J',
        'S': 'Meriva',
        'V': 'Combo II',
        'W': 'Cascada',
    }

    BODIES = {
        '2': '3-Door Hatchback',
        '3': '2-Door Coupe',
        '5': '4-Door Sedan',
        '6': '5-Door Hatchback',
        '7': '3-Door Crossover',
        '8': '5-Door Wagon',
        '9': '5-Door Minivan',
        'B': 'Minibus',
        'C': 'Van',
        'J': 'Van',
        'X': '3-Door Station Wagon',
    }

    PLANTS = {
        '1': 'Russelsheim',
        '2': 'Bochum',
        '3': 'Azambuja',
        '4': 'Zaragoza',
        '5': 'Antwerp',
        '6': 'Eisenach',
        '7': 'Luton',
        '8': 'Ellesmere Port',
        '9': 'Uusikaupunki',
        'A': 'Azambuja',
        'B': 'Bertone / Saint Peterburg',
        'C': 'Yelabuga',
        'D': 'Shin Chuang',
        'E': 'Heuliez',
        'F': 'Togliatti',
        'G': 'Gliwice',
        'H': 'Rayong',
        'L': 'Elizabeth',
        'M': 'Millbrook',
        'N': 'Norwich',
        'P': 'Warsaw',
        'R': 'Rosario',
        'S': 'Szentgotthard',
        'V': 'Luton',
        'X': 'Zaporozhia',
        'Z': 'Izmir',
    }

    @property
    def model_code(self):
        return self._vin.vds[0]

    @property
    def body_code(self):
        return self._vin.vds[2]

    @property
    def engine_code(self):
        return self._vin.vds[4]

    @property
    def engine(self):
        candidates = {
            'P': {
                '1': 'A18XER140HP',
                'B': 'A14XER100HP',
                'C': 'A14NET140HP',
                'D': 'A16XER115HP',
                'J': 'A16LET180HP',
                'N': 'A20DTH165HP',
                'U': 'A14NEL120HP',
            },
            'W': {
                'N': 'A20DTH160HP',
                'C': 'A14NET140HP',
            },
            'G': {
                'A': 'A16XER115HP',
                'B': 'A16LET180HP',
                'C': 'A18XER140HP',
                'D': 'A20NHT220HP',
                'E': 'A20NHT250HP',
                'F': 'A28NET260HP',
                'G': 'A28NER325HP',
                'M': 'A20DTH160HP',
                'N': 'A20DTR195HP',
                'P': 'A14NFT140HP',
                'X': 'A20NHT250HP',
            },
            'V': {
                '1': 'Y13D70HP',
                '2': 'Z14XEP100HP',
            },
            'S': {
                'C': 'Z14XEP100HP',
                'D': 'A14NEL120HP',
                'E': 'A14NET140HP',
            },
            'J': {
                '8': 'A14NET140HP',
            },
        }
        model_engines = candidates.get(self.model_code, {})
        return model_engines.get(self.engine_code)

    @property
    def plant_code(self):
        return self._vin.vis[1]

    @property
    def serial(self):
        return self._vin.vis[2:]
