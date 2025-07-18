# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the dog model and view.
"""

from models.rental_details import DogModel
from views.rental_details import DogView


class DogController():
    """
    @summary: This class controller the dog details.
    """

    def __init__(self, dogModel: DogModel, dogView: DogView):
        """
        @summary: The init method initialize instance attributes.
        @param self: DogController self parameter.
        @param dogModel: The model class for MVC pattern.
        @param dogView: The view class for MVC pattern.
        """
        self._dogModel: DogModel = dogModel
        self._dogView: DogView = dogView

    def showDogView(self, translations: dict = {}) -> str:
        """
        @summary: Return the view of tent.
        @param self: TentController self parameter.
        @param translations: Language words.
        @returns: Returns view of Tent Details in string.
        """
        return self._dogView.showDogView(translations, self._dogModel.LeiPricePerNight, self._dogModel.EurPricePerNight)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: DogController self parameter.
        @returns: Returns showDogView().
        """
        return self.showDogView()
