# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the dog model and view.
"""

from models.rental_details import DogModel
from views.rental_details import DogView


class DogController():
    """
    This class controller the dog details.
    """

    def __init__(self, dog_model: DogModel, dog_view: DogView):
        """
        The init method initialize instance attributes.

        Args:
            self: DogController self parameter.
            dog_model: The model class for MVC pattern.
            dog_view: The view class for MVC pattern.
        """
        self._dog_model: DogModel = dog_model
        self._dog_view: DogView = dog_view

    def show_dog_view(self, translations: dict = {}) -> str:
        """
        Return the view of tent.

        Args:
            self: TentController self parameter.
            translations: Language words.
        Returns:
            Returns view of Tent Details in string.
        """
        return self._dog_view.show_dog_view(translations, self._dog_model.lei_price_per_night, self._dog_model.eur_price_per_night)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: DogController self parameter.
        Returns:
            Returns show_dog_view().
        """
        return self.show_dog_view()
