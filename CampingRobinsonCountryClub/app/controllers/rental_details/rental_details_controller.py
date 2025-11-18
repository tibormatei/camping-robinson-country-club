# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the rental details model, and view.
"""

import models.rental_details.rental_details_model as models
import views.rental_details.rental_details_view as views

from models.rental_details import TentModel
from models.rental_details import TrailersModel
from models.rental_details import DogModel


class RentalDetailsController():
    """
    This class controller the rental details.
    """

    def __init__(self, rental_details_model: models.RentalDetailsModel, rental_details_view: views.RentalDetailsView):
        """
        The init method initialize instance attributes.

        Args:
            self: RentalDetailsController self parameter.
            rental_details_model: The model class for MVC pattern.
            rental_details_view: The view class for MVC pattern.
        """
        self._rental_details_model: models.RentalDetailsModel = rental_details_model
        self._rental_details_view: views.RentalDetailsView = rental_details_view

    def show_rental_details(self, translations: dict = {}) -> str:
        """
        Return the view of tent, trailer and dog detals.

        Args:
            self: RentalDetailsController self parameter.
            translations: Language words.
        Returns:
            Returns view of Rental Details in string.
        """
        tent_model: TentModel = self._rental_details_model.tent_model
        trailers_model: TrailersModel = self._rental_details_model.trailers_model
        dog_model: DogModel = self._rental_details_model.dog_model
        try:
            price_information: str = translations['rentalDetails']['priceInformation']
            check_out_information: str = translations['rentalDetails']['checkOutinformation']
        except KeyError:
            price_information: str = self._rental_details_model.price_information
            check_out_information: str = self._rental_details_model.check_out_information
        finally:
            return self._rental_details_view.show_rental_details_view(translations, tent_model, trailers_model, 
                                                                      dog_model, price_information, check_out_information)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: RentalDetailsController self parameter.
        Returns:
            Returns show_rental_details().
        """
        return self.show_rental_details()
