# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import sys


PY3 = sys.version_info[0] == 3

if PY3:  # pragma: nocover
    string_types = str,

else:  # pragma: nocover
    string_types = basestring,
