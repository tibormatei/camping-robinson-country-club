# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsController.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the rental details model, and view.
"""

from app.models import RentalDetailsModel
from app.views import RentalDetailsView


class RentalDetailsController():
    """
    @summary: This class controller the rental details.
    """

    def __init__(self, rentalDetailsModel: RentalDetailsModel, rentalDetailsView: RentalDetailsView):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsController self parameter.
        @param rentalDetailsModel: The model class for MVC pattern.
        @param rentalDetailsView: The view class for MVC pattern.
        """
        self._rentalDetailsModel: RentalDetailsModel = rentalDetailsModel
        self._rentalDetailsView: RentalDetailsView = rentalDetailsView

    def showRentalDetails(self) -> str:
        """
        @summary: Return the view of tent, trailer and dog detals.
        @param self: RentalDetailsController self parameter.
        @returns: Returns view of Rental Details in string.
        """
        rentalDetailsView: str = str()

        rentalDetailsView.append(self._rentalDetailsView.showTentView())
        rentalDetailsView.append(self._rentalDetailsView.showTrailerView())
        rentalDetailsView.append(self._rentalDetailsView.showDogView())

        return rentalDetailsView

    @classmethod
    def __str__(cls) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: RentalDetailsController cls parameter.
        @returns: Returns showRentalDetails().
        """
        return cls.showRentalDetails()
