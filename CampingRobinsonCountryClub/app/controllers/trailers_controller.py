# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the trailers model and view.
"""

from models import TrailersModel
import views.trailers_view as from_views


class TrailersController():
    """
    @summary: This class controller the trailersent details.
    """

    def __init__(self, trailersModel: TrailersModel, trailersView: from_views.TrailerView):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailersController self parameter.
        @param trailersModel: The model class for MVC pattern.
        @param trailersView: The view class for MVC pattern.
        """
        self._trailersModel: TrailersModel = trailersModel
        self._trailersView: from_views.TrailerView = trailersView

    def showTrailersView(self, translations: dict = {}) -> str:
        """
        @summary: Return the view of tent.
        @param self: TentController self parameter.
        @param trailerControllers: Trailer controllers, because need to call the view.
        @returns: Returns view of Tent Details in string.
        """
        return self._trailersView.showTrailersView(translations, self._trailersModel)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: TrailersController self parameter.
        @returns: Returns showTrailersView().
        """
        return self.showTrailersView()
