from ..common import constant_info
from ..dicts.bodies import BODY_MOTORCYCLE
from ._base import Detail, VinDetails


class DafraDetails(VinDetails):

    model = Detail(('vds', slice(0, 2)), {
        'CA': 'Speed 150',
        'CB': 'Kansas 150',
    })

    # for a while, it will be a motorcycle regardless of the code source
    body = Detail(None, constant_info(BODY_MOTORCYCLE))

    plant = Detail(('vis', 1), {
        'M': 'Manaus',
    })

    serial = Detail(('vis', slice(2, None)))