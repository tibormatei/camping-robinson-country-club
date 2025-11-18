# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_section.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the rental details classes.
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
    This class controller the rental details objects.
    """

    def __init__(self):
        """
        The init method initialize instance attributes.

        Args:
            self: RentalDetailsSection self parameter.
        """
        rental_details_data: RentalDetailsDataFromJson = RentalDetailsDataFromJson()

        # 1. Tent controller:
        tent_model_builder: TentModelBuilder = TentModelBuilder(rental_details_data)
        tent_model: TentModel = tent_model_builder.retrive_tent_model()

        # 2. Trailers controller:
        trailers_model_builder: TrailersModelBuilder = TrailersModelBuilder(rental_details_data)
        trailers_model: TrailersModel = trailers_model_builder.retrive_trailers_model()

        # 3. Dog controller:
        dog_model_builder: DogModelBuilder = DogModelBuilder(rental_details_data)
        dog_model: DogModel = dog_model_builder.retrive_dog_model()

        # 4. RentalDetails controller:
        rental_details_model: RentalDetailsModel = RentalDetailsModel(tent_model, trailers_model, dog_model)
        rental_details_view: RentalDetailsView = RentalDetailsView()
        self._rental_details_controller: RentalDetailsController = RentalDetailsController(rental_details_model, rental_details_view)

    def generate_rental_details_section(self, translations: dict = {}) -> str:
        """
        Generates rental details html section.

        Args:
            self: RentalDetailsSection self parameter.
            translations: Language words.
        Returns:
            Returns a full displayable Rental details information html code piece.
        """
        return self._rental_details_controller.show_rental_details(translations)
