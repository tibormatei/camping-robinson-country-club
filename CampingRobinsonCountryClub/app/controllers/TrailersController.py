# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TrailersController.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the trailers model and view.
"""

from collections.abc import Iterator

from app.models import TrailersModel
from app.views import TrailersView


class TrailersController():
    """
    @summary: This class controller the trailersent details.
    """

    def __init__(self, trailersModel: TrailersModel, trailersView: TrailersView):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailersController self parameter.
        @param trailersModel: The model class for MVC pattern.
        @param trailersView: The view class for MVC pattern.
        """
        self._trailersModel: TrailersModel = trailersModel
        self._trailersView: TrailersView = trailersView

    def showTrailersView(self, translations: dict = {}, trailerControllers: Iterator = None) -> str:
        """
        @summary: Return the view of tent.
        @param self: TentController self parameter.
        @returns: Returns view of Tent Details in string.
        """
        return self._trailersView.showTrailersView(translations, trailerControllers)

    @classmethod
    def __str__(cls) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: TrailersController cls parameter.
        @returns: Returns showTrailersView().
        """
        return cls.showTrailersView()
