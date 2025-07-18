# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_section.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the rental details classes.
"""

from data import RentalDetailsDataFromJson
from data import TentModelBuilder
from models.rental_details import TentModel
from data import TrailersModelBuilder
from models.rental_details import TrailersModel
from data import DogModelBuilder
from models.rental_details import DogModel
from models.rental_details import RentalDetailsModel
from views.rental_details import RentalDetailsView
from controllers.rental_details import RentalDetailsController


class RentalDetailsSection():
    """
    @summary: This class controller the rental details objects.
    """

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsSection self parameter.
        """
        rentalDetailsData: RentalDetailsDataFromJson = RentalDetailsDataFromJson()

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

    def generateRentalDetailsSection(self, translations: dict = {}) -> str:
        """
        @summary: Generates rental details html section.
        @param self: RentalDetailsSection self parameter.
        @param translations: Language words.
        @returns: Returns a full displayable Rental details information html code piece.
        """
        return self._rentalDetailsController.showRentalDetails(translations)
