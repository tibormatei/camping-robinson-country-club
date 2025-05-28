# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental details.
"""

from app.views import TentView
from app.views import TrailersView
from app.views import DogView


class RentalDetailsView():
    """
    @summary: This class handles the view of rental details.
    """

    def __init__(self):
        """
        @summary: Rental details views.
        @param self: RentalDetailsView self parameter.
        """
        pass

    @classmethod
    def showRentalDetailsView(cls, tentView: TentView, trailersView: TrailersView, dogView: DogView,
                              priceInformation: str, checkOutinformation: str) -> str:
        """
        @summary: Create the full rental details view.
        @param cls: RentalDetailsView cls parameter.
        @param tentView: Delegates Tent's View class from the controller.
        @param trailersView: Delegates Trailer's View class from the controller.
        @param dogView: Delegates Dog's View class from the controller.
        @param priceInformation: Price information data.
        @param checkOutinformation: Check Out information data.
        @returns: Returns a full displayable Rental information html code piece.
        """
        rentalDetailsView: str = str()
        # itt valoszinuleg a controllerek fognak keleni, s akkor azoknak felhivni a show-jat es akkor itt ok
        # tentSection: str = tentView.showTentView()

        return rentalDetailsView
