from typing import TYPE_CHECKING, ClassVar

from ..common import Annotatable

if TYPE_CHECKING:  # pragma: nocover
    from ..toolbox import Vin


class DetailWrapper:

    __slots__ = ['_supported', 'code', 'name']

    def __init__(self, details: 'VinDetails', detail: 'Detail'):
        """
        :param details:
        :param detail:

        """
        vin = details._vin

        source = detail.source

        code = ''

        if source:
            attr_name, attr_idx = source
            code_source = getattr(vin, attr_name)

            code = code_source[attr_idx]

        defs = detail.defs

        if callable(defs):
            defs = defs(details)

        self.code: str = code
        self.name: str | None = defs.get(code)

        self._supported = bool(source) or bool(self.name)
        """Flag indicating that this detail extraction is available."""

    def __str__(self):
        return self.name or self.code

    def __bool__(self):
        return self._supported


class Detail:
    """Vin detail descriptor."""

    __slots__ = ['defs', 'source']

    def __init__(self, code_source=None, definitions=None):
        self.source = code_source
        self.defs = definitions or {}

    def __get__(self, instance: 'VinDetails', owner: type['VinDetails']) -> DetailWrapper:
        """
        :param instance:
        :param owner:

        """
        return DetailWrapper(instance, self)


class VinDetails(Annotatable):
    """Offers advanced (manufacturer specific) VIN data extraction ficilities."""

    annotate_titles: ClassVar = {
        'body': 'Body',
        'engine': 'Engine',
        'model': 'Model',
        'plant': 'Plant',
        'transmission': 'Transmission',
        'serial': 'Serial',
    }

    def __init__(self, vin: 'Vin'):
        self._vin = vin

    body = Detail()
    engine = Detail()
    model = Detail()
    plant = Detail()
    transmission = Detail()
    serial = Detail()
