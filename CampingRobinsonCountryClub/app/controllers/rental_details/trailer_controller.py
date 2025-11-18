# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the trailer model and view.
"""

from models.rental_details import TrailerModel
from views.rental_details import TrailerView


class TrailerController():
    """
    This class controller the trailer details.
    """

    def __init__(self, trailer_model: TrailerModel, trailer_view: TrailerView):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailerController self parameter.
            trailer_model: The model class for MVC pattern.
            trailer_view: The view class for MVC pattern.
        """
        self._trailer_model: TrailerModel = trailer_model
        self._trailer_view: TrailerView = trailer_view

    def show_trailer_view(self, translations: dict = {}) -> str:
        """
        Return the view of tent.

        Args:
            self: TentController self parameter.
        Returns:
            Returns view of Tent Details in string.
        """
        trailer_capacity: str = self._trailer_model.trailer_capacity
        lei_price: int = self._trailer_model.lei_price
        eur_price: int = self._trailer_model.eur_price
        return self._trailer_view.show_trailer_view(translations, trailer_capacity, lei_price, eur_price)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: TrailerController self parameter.
        Returns:
            Returns show_trailer_view().
        """
        return self.show_trailer_view()
