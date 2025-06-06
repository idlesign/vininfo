from ._base import VinDetails, Detail
from ..common import constant_info
from ..dicts.bodies import BODY_MOTORCYCLE


class DafraDetails(VinDetails):

    model = Detail(('vds', slice(0, 2)), {
        'CA': 'SPEED 150',
        'CB': 'KANSAS 150',
    })

    # for a while, it will be a motorcycle regardless of the code source
    body = Detail(None, constant_info(BODY_MOTORCYCLE))

    plant = Detail(('vis', 1), {
        'M': 'Manaus',
    })

    serial = Detail(('vis', slice(2, None)))