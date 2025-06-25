# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_ontroller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the rental details model, and view.
"""

import models.rental_details.rental_details_model as models
import views.rental_details.rental_details_view as views

from models.rental_details import TentModel
from models.rental_details import TrailersModel
from models.rental_details import DogModel


class RentalDetailsController():
    """
    @summary: This class controller the rental details.
    """

    def __init__(self, rentalDetailsModel: models.RentalDetailsModel, rentalDetailsView: views.RentalDetailsView):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsController self parameter.
        @param rentalDetailsModel: The model class for MVC pattern.
        @param rentalDetailsView: The view class for MVC pattern.
        """
        self._rentalDetailsModel: models.RentalDetailsModel = rentalDetailsModel
        self._rentalDetailsView: views.RentalDetailsView = rentalDetailsView

    def showRentalDetails(self, translations: dict = {}) -> str:
        """
        @summary: Return the view of tent, trailer and dog detals.
        @param self: RentalDetailsController self parameter.
        @param translations: Language words.
        @returns: Returns view of Rental Details in string.
        """
        tentModel: TentModel = self._rentalDetailsModel.TentModel
        trailersModel: TrailersModel = self._rentalDetailsModel.TrailersModel
        dogModel: DogModel = self._rentalDetailsModel.DogModel
        try:
            priceInformation: str = translations['rentalDetails']['priceInformation']
            checkOutinformation: str = translations['rentalDetails']['checkOutinformation']
        except KeyError:
            priceInformation: str = self._rentalDetailsModel.PriceInformation
            checkOutinformation: str = self._rentalDetailsModel.CheckOutInformation
        return self._rentalDetailsView.showRentalDetailsView(translations, tentModel, trailersModel,
                                                             dogModel, priceInformation, checkOutinformation)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: RentalDetailsController self parameter.
        @returns: Returns showRentalDetails().
        """
        return self.showRentalDetails()
