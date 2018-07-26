# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


class VininfoException(Exception):
    """Base exception."""


class ValidationError(VininfoException):
    """Data validation exception."""
