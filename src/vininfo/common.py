from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING: # pragma: nocover
    from .details._base import VinDetails


def constant_info(info):
    """Emulate details logic to always return the same information."""
    return lambda details: type("", (), {"get": (lambda code: info)})


def candidate_by_year_model_mapping(mapping: dict[str, dict[str, str]], years: list[int]):
    candidate_mapping = {}
    for model_year_range, candidates in mapping.items():
        start_model_year, end_model_year = model_year_range.split('-')

        if not start_model_year and not end_model_year:
            candidate_mapping.update(candidates)
            continue

        start_model_year = int(start_model_year)
        end_model_year = (
            int(end_model_year)
            if end_model_year else
            max(datetime.now(tz=timezone.utc).year, start_model_year) + 1
        )

        filter_years = [year for year in years if start_model_year <= year <= end_model_year]
        if filter_years:
            candidate_mapping.update(candidates)

    return candidate_mapping


class Annotatable:

    annotate_titles: ClassVar = {}

    def annotate(self) -> dict[str, Any]:

        annotations = {}
        no_attr = set()

        for attr_name, label in self.annotate_titles.items():
            value = getattr(self, attr_name, no_attr)

            if value is no_attr:
                continue

            if isinstance(value, list):
                value = ', '.join(f'{val}' for val in value)

            annotations[label] = f'{value}'

        return dict(sorted(annotations.items(), key=lambda item: item[0]))


class Assembler:
    """Assembler is a manufacturer that has a WMI and assemble vehicles for other brands using its own WMI."""
    __slots__ = ['manufacturer']

    brands: ClassVar[set['Brand']] = None

    def __init__(self, manufacturer: str | None = None):
        self.manufacturer = manufacturer or self.title

    @property
    def title(self) -> str:
        return self.__class__.__name__

    def __str__(self):
        return f'{self.title} ({self.manufacturer})'


class Brand(Assembler):
    extractor: type['VinDetails'] = None

    @property
    def brands(self) -> set['Brand']:
        return {self}


class UnsupportedBrand(Brand):
    """Unsupported brand."""