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

from collections.abc import Iterator

from app.models import RentalDetailsModel
from app.views import RentalDetailsView

from app.controllers import TentController
from app.controllers import TrailersController
from app.controllers import DogController

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

    def showRentalDetails(self, translations: dict) -> str:
        """
        @summary: Return the view of tent, trailer and dog detals.
        @param self: RentalDetailsController self parameter.
        @param translations: Language words.
        @returns: Returns view of Rental Details in string.
        """
        tentController: TentController = self._rentalDetailsModel.TentController
        trailersController: TrailersController = self._rentalDetailsModel.TrailersController
        trailerControllersList: Iterator = self._rentalDetailsModel.TrailerControllersList
        dogController: DogController = self._rentalDetailsModel.DogController
        priceInformation: str = self._rentalDetailsModel.PriceInformation
        checkOutinformation: str = self._rentalDetailsModel.CheckOutinformation
        return self._rentalDetailsView.showRentalDetailsView(translations, tentController, trailersController, trailerControllersList,
                                                             dogController, priceInformation, checkOutinformation)

    @classmethod
    def __str__(cls) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: RentalDetailsController cls parameter.
        @returns: Returns showRentalDetails().
        """
        return cls.showRentalDetails()
