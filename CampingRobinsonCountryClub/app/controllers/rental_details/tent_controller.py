# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the tent model and view.
"""

from models.rental_details import TentModel
from views.rental_details import TentView

class TentController():
    """
    This class controller the tent details.
    """

    def __init__(self, tent_model: TentModel, tent_view: TentView):
        """
        The init method initialize instance attributes.

        Args:
            self: TentController self parameter.
            tent_model: The model class for MVC pattern.
            tent_view: The view class for MVC pattern.
        """
        self._tent_model: TentModel = tent_model
        self._tent_view: TentView = tent_view

    def show_tent_view(self, translations: dict = {}) -> str:
        """
        Return the view of tent.

        Args:
            self: TentController self parameter.
            translations: Language words.
        Returns:
            Returns view of Tent Details in string.
        """
        return self._tent_view.show_tent_view(translations, self._tent_model.tent_capacities,
                                              self._tent_model.lei_price_per_person, self._tent_model.eur_price_per_person)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: TentController self parameter.
        Returns:
            Returns show_tent_view().
        """
        return self.show_tent_view()
