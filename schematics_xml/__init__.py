# -*- coding: utf-8 -*-
"""Python schematics models for converting to and from XML."""
# :copyright: (c) 2016 Alex Hayes,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.
from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple

VersionInfo = namedtuple(
    'VersionInfo', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = VersionInfo(0, 1, 2, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/schematics-xml'
__docformat__ = 'restructuredtext'

# -eof meta-

from schematics_xml.models import XMLModel  # pylint: disable=wrong-import-position
