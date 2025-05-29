# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsSection.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the rental details classes.
"""

from app.models import TentModel
from app.views import TentView
from app.controllers import TentController


class RentalDetailsSection():
    """
    @summary: This class controller the rental details objects.
    """

    def __init__(self):
        # itt kell egyszer beolvassam az osszes adatot, visszadjam, majd fellepitsem az osszes controller-t
        # 1. Tent controller:
        self._tentModel = TentModel()