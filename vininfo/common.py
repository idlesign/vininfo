from typing import Dict, Any, Type

if False:  # pragma: nocover
    from .details._base import VinDetails  # noqa


class Annotatable:

    annotate_titles = {}

    def annotate(self) -> Dict[str, Any]:

        annotations = {}
        no_attr = set()

        for attr_name, label in self.annotate_titles.items():
            value = getattr(self, attr_name, no_attr)

            if value is no_attr:
                continue

            if isinstance(value, list):
                value = ', '.join(f'{val}' for val in value)

            annotations[label] = f'{value}'

        return dict((title, value) for title, value in sorted(annotations.items(), key=lambda item: item[0]))


class Brand:

    __slots__ = ['manufacturer']

    extractor: Type['VinDetails'] = None

    def __init__(self, manufacturer: str = None):
        self.manufacturer = manufacturer or self.title

    @property
    def title(self) -> str:
        return self.__class__.__name__

    def __str__(self):
        return f'{self.title} ({self.manufacturer})'


class UnsupportedBrand(Brand):
    """Unsupported brand."""
