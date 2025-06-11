# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TentController.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the tent model and view.
"""

from app.models import TentModel
from app.views import TentView


class TentController():
    """
    @summary: This class controller the tent details.
    """

    def __init__(self, tentModel: TentModel, tentView: TentView):
        """
        @summary: The init method initialize instance attributes.
        @param self: TentController self parameter.
        @param tentModel: The model class for MVC pattern.
        @param tentView: The view class for MVC pattern.
        """
        self._tentModel: TentModel = tentModel
        self._tentView: TentView = tentView

    def showTentView(self, translations: dict = {}) -> str:
        """
        @summary: Return the view of tent.
        @param self: TentController self parameter.
        @param translations: Language words.
        @returns: Returns view of Tent Details in string.
        """
        return self._tentView.showTentView(translations, self._tentModel.TentCapacities, self._tentModel.LeiPricePerPerson, self._tentModel.EurPricePerPerson)

    @classmethod
    def __str__(cls) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: TentController cls parameter.
        @returns: Returns showTentView().
        """
        return cls.showTentView()
