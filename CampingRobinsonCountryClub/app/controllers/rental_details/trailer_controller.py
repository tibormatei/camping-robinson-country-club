# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the trailer model and view.
"""

from models.rental_details import TrailerModel
from views.rental_details import TrailerView


class TrailerController():
    """
    @summary: This class controller the trailer details.
    """

    def __init__(self, trailerModel: TrailerModel, trailerView: TrailerView):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailerController self parameter.
        @param trailerModel: The model class for MVC pattern.
        @param trailerView: The view class for MVC pattern.
        """
        self._trailerModel: TrailerModel = trailerModel
        self._trailerView: TrailerView = trailerView

    def showTrailerView(self, translations: dict = {}) -> str:
        """
        @summary: Return the view of tent.
        @param self: TentController self parameter.
        @returns: Returns view of Tent Details in string.
        """
        trailerCapacity: str = self._trailerModel.TrailerCapacity
        leiPrice: int = self._trailerModel.LeiPrice
        eurPrice: int = self._trailerModel.EurPrice
        return self._trailerView.showTrailerView(translations, trailerCapacity, leiPrice, eurPrice)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: TrailerController self parameter.
        @returns: Returns showTrailerView().
        """
        return self.showTrailerView()
