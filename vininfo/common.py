# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict


class Annotatable(object):

    annotate_titles = {}

    def annotate(self):

        annotations = {}
        no_attr = set()

        for attr_name, label in self.annotate_titles.items():
            value = getattr(self, attr_name, no_attr)

            if value is no_attr:
                continue

            if isinstance(value, list):
                value = ', '.join('%s' % val for val in value)
            annotations[label] = value

        return OrderedDict((title, value) for title, value in sorted(annotations.items(), key=lambda item: item[0]))


class Brand(object):

    __slots__ = ['manufacturer']

    extractor = None

    def __init__(self, manufacturer=None):
        self.manufacturer = manufacturer or self.title

    @property
    def title(self):
        return self.__class__.__name__

    def __str__(self):
        return '%s (%s)' % (self.title, self.manufacturer)
