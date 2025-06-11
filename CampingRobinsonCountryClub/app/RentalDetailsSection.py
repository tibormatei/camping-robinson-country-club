# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsSection.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the rental details classes.
"""

from app.data import RentalDetailsDataFromFile
from app.data import TentModelBuilder
from app.models import TentModel
from app.data import TrailersModelBuilder
from app.models import TrailersModel
from app.data import DogModelBuilder
from app.models import DogModel
from app.models import RentalDetailsModel
from app.views import RentalDetailsView
from app.controllers import RentalDetailsController


class RentalDetailsSection():
    """
    @summary: This class controller the rental details objects.
    """

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsSection self parameter.
        """
        rentalDetailsData: RentalDetailsDataFromFile = RentalDetailsDataFromFile()

        # 1. Tent controller:
        tentModelBuilder: TentModelBuilder = TentModelBuilder(rentalDetailsData)
        tentModel: TentModel = tentModelBuilder.RetriveTentModel()

        # 2. Trailers controller:
        trailersModelBuilder: TrailersModelBuilder = TrailersModelBuilder(rentalDetailsData)
        trailersModel: TrailersModel = trailersModelBuilder.RetriveTrailersModel()

        # 3. Dog controller:
        dogModelBuilder: DogModelBuilder = DogModelBuilder(rentalDetailsData)
        dogModel: DogModel = dogModelBuilder.RetriveDogModel()

        # 4. RentalDetails controller:
        rentalDetailsModel: RentalDetailsModel = RentalDetailsModel(tentModel, trailersModel, dogModel)
        rentalDetailsView: RentalDetailsView = RentalDetailsView()
        self._rentalDetailsController: RentalDetailsController = RentalDetailsController(rentalDetailsModel, rentalDetailsView)

    @classmethod
    def generateRentalDetailsSection(cls, translations: dict = {}) -> str:
        """
        @summary: Generates rental details html section.
        @param cls: RentalDetailsSection cls parameter.
        @param translations: Language words.
        @returns: Returns a full displayable Rental details information html code piece.
        """
        return cls._rentalDetailsController.showRentalDetails(translations)
