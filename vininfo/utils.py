# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import sys


PY3 = sys.version_info[0] == 3

if PY3:  # pragma: nocover
    string_types = str,

else:  # pragma: nocover
    string_types = basestring,


def merge_wmi(new_wmis):
    """Helper. Used to update vininfo.dicts.wmi.WMI dictionary
    with entries from another dictionary.

    Existing keys are skipped, new keys are added, result is sorted.

    Returns a two-items tuple:
        0. set of new keys borrowed from `new_wmis`;
        1. source code string to replace the current `WMI` dictionary with.

    :param dict new_wmis: Mapping from WMI (two or three chars) to manufacturer title.
    :rtype: tuple[set, str]
    """
    import inspect
    import re

    from .dicts import wmi

    wmi_src = re.search('WMI = {([^}]+)}', inspect.getsource(wmi), re.MULTILINE)

    assert wmi_src, 'Unable to parse WMI dict body'

    wmi_src_dict = {}

    for line in wmi_src.group(1).splitlines():
        line = line.strip(', ')

        if not line:
            continue

        key, _, value = line.partition(':')
        wmi_src_dict[key.strip('\'"')] = value.strip()

    wmi_missing = set(new_wmis.keys()).difference(wmi_src_dict.keys())

    for key in wmi_missing:
        wmi_src_dict[key] = "'%s'" % new_wmis[key]

    wmi_dst = ['WMI = {']

    for key, value in sorted(wmi_src_dict.items(), key=lambda item: item[0]):
        wmi_dst.append("    '%s': %s," % (key, value))

    wmi_dst.append('}')

    return wmi_missing, '\n'.join(wmi_dst)
