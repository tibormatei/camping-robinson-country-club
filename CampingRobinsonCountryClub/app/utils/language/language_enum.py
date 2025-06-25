# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_enum.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

from enum import Enum


class LanguageCodes(Enum):
    """
    @summary: This is an enum, that represent Language codes.
    """
    en = 'English'
    hu = 'Hungarian'
    ro = 'Romanian'
