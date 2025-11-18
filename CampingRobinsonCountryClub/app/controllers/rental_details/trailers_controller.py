# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the trailers model and view.
"""

from models.rental_details import TrailersModel


class TrailersController():
    """
    This class controller the trailersent details.
    """

    def __init__(self, trailers_model: TrailersModel, trailers_view):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailersController self parameter.
            trailers_model: The model class for MVC pattern.
            trailers_view: The view class for MVC pattern.
        """
        import views.rental_details.trailers_view as from_views

        self._trailers_model: TrailersModel = trailers_model
        self._trailers_view: from_views.TrailersView = trailers_view

    def show_trailers_view(self, translations: dict = {}) -> str:
        """
        Return the view of tent.

        Args:
            self: TentController self parameter.
            trailerControllers: Trailer controllers, because need to call the view.
        Returns:
            Returns view of Tent Details in string.
        """
        return self._trailers_view.show_trailers_view(translations, self._trailers_model)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: TrailersController self parameter.
        Returns:
            Returns show_trailers_view().
        """
        return self.show_trailers_view()
