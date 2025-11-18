# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of rental details.
"""

from pathlib import Path

from models.rental_details import TentModel
from models.rental_details import TrailersModel
from models.rental_details import DogModel
from views.rental_details import TentView
import views.rental_details.trailers_view as from_views
from views.rental_details import DogView
from controllers.rental_details import TentController
from controllers.rental_details import TrailersController
from controllers.rental_details import DogController


class RentalDetailsView():
    """
    This class handles the view of rental details.
    """

    # Class variables
    RENTAL_DETAILS_SECTION_FILE_CONTENT: str = None
    RENTAL_DETAILS_SECTION_FILE_NAME: str = 'section_rentalDetails.html'
    RENTAL_DETAILS_SECTION_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('templates', 'rental_details', RENTAL_DETAILS_SECTION_FILE_NAME)

    def __init__(self):
        """
        Rental details views.

        Args:
            self: RentalDetailsView self parameter.
        """
        if self.__class__.RENTAL_DETAILS_SECTION_FILE_CONTENT is None:
            self.__class__.RENTAL_DETAILS_SECTION_FILE_CONTENT = self.__read_rental_details_section_html()

    @classmethod
    def show_rental_details_view(cls, translations: dict, tent_model: TentModel,
                              trailers_model: TrailersModel, dog_model: DogModel,
                              price_information: str, check_out_information: str) -> str:
        """
        Create the full rental details view.

        Args:
            cls: RentalDetailsView cls parameter.
            translations: Language words.
            tent_model: Tent's Model class.
            trailers_model: Trailers's Model class.
            dog_model: Dog's Model class.
            price_information: Price details.
            check_out_information: Check Out time.
        Returns:
             Returns a full displayable Rental information html code piece.
        """
        rental_details_view: str = cls.RENTAL_DETAILS_SECTION_FILE_CONTENT

        # Tent section
        tent_view: TentView = TentView()
        tent_controller: TentController = TentController(tent_model, tent_view)
        tent_section_content: str = tent_controller.show_tent_view(translations)

        TENT_SECTION_KEY: str = 'tentSection'
        rental_details_view = rental_details_view.replace('{{' + TENT_SECTION_KEY + '}}', tent_section_content)

        # Trailers section
        trailers_view: from_views.TrailersView = from_views.TrailersView()
        trailers_controller: TrailersController = TrailersController(trailers_model, trailers_view)
        trailers_section_content: str = trailers_controller.show_trailers_view(translations)

        TRAILERS_SECTION_KEY: str = 'trailersSection'
        rental_details_view = rental_details_view.replace('{{' + TRAILERS_SECTION_KEY + '}}', trailers_section_content)

        # Dog section
        dog_view: DogView = DogView()
        dog_controller: DogController = DogController(dog_model, dog_view)
        dog_section_content: str = dog_controller.show_dog_view(translations)

        DOG_SECTION_KEY: str = 'dogSection'
        rental_details_view = rental_details_view.replace('{{' + DOG_SECTION_KEY + '}}', dog_section_content)

        # Price Information section
        PRICE_INFORMATION_SECTION_KEY: str = 'priceInformation'
        rental_details_view = rental_details_view.replace('{{' + PRICE_INFORMATION_SECTION_KEY + '}}', price_information)

        # Price Information section
        CHECK_OUTINFORMATION_SECTION_KEY: str = 'checkOutinformation'
        rental_details_view = rental_details_view.replace('{{' + CHECK_OUTINFORMATION_SECTION_KEY + '}}', check_out_information)

        return rental_details_view

    @classmethod
    def __read_rental_details_section_html(cls) -> str:
        """
        Read in section_rentalDetails.html from templates folder.

        Args:
            cls: RentalDetailsView cls parameter.
        Returns:
            Returns contents of html file.
        """
        rental_details_section_html: str = None

        try:
            with open(cls.RENTAL_DETAILS_SECTION_FILE_PATH, 'r', encoding = 'utf-8') as f:
                rental_details_section_html = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.RENTAL_DETAILS_SECTION_FILE_PATH} file not found!")
            rental_details_section_html = None

        except Exception as e:
            print(f"Exception Error: reading {cls.RENTAL_DETAILS_SECTION_FILE_PATH}: {e}")
            rental_details_section_html = None

        return rental_details_section_html
