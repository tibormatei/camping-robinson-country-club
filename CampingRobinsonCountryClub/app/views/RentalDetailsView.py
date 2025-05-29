# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental details.
"""

from pathlib import Path
from collections.abc import Iterator

from app.controllers import TentController
from app.controllers import TrailersController
from app.controllers import DogController


class RentalDetailsView():
    """
    @summary: This class handles the view of rental details.
    """

    # Class variables
    RENTAL_DETAILS_SECTION_FILE_CONTENT: str = None
    RENTAL_DETAILS_SECTION_FILE_NAME: str = 'section__rentalDetails.html'
    RENTAL_DETAILS_SECTION_FILE_PATH: Path = Path(__file__).parent.parent.joinpath('templates', RENTAL_DETAILS_SECTION_FILE_NAME)

    def __init__(self):
        """
        @summary: Rental details views.
        @param self: RentalDetailsView self parameter.
        """
        if self.__class__.RENTAL_DETAILS_SECTION_FILE_CONTENT is None:
            self.__class__.RENTAL_DETAILS_SECTION_FILE_CONTENT = self.__readRentalDetailsSectionHtml()

    @classmethod
    def showRentalDetailsView(cls, translations: dict,
                              tentController: TentController,
                              trailersController: TrailersController,
                              trailerControllersList: Iterator,
                              dogController: DogController,
                              priceInformation: str, checkOutinformation: str) -> str:
        """
        @summary: Create the full rental details view.
        @param cls: RentalDetailsView cls parameter.
        @param translations: Language words.
        @param tentController: Tent's controller class.
        @param trailersController: Trailers's controller class.
        @param trailerControllersList: List of TrailerControllers.
        @param dogController: Dog's controller class.
        @param priceInformation: Price details.
        @param checkOutinformation: Check Out time.
        @returns: Returns a full displayable Rental information html code piece.
        """
        rentalDetailsView: str = cls.RENTAL_DETAILS_SECTION_FILE_CONTENT

        # Tent section
        TENT_SECTION_KEY: str = 'tentSection'
        tentSectionContent: str = tentController.showTentView(translations)
        rentalDetailsView = rentalDetailsView.replace('{{' + TENT_SECTION_KEY + '}}', tentSectionContent)

        # Trailers section
        TRAILERS_SECTION_KEY: str = 'trailersSection'
        trailersSectionContent: str = trailersController.showTrailersView(translations, trailerControllersList)
        rentalDetailsView = rentalDetailsView.replace('{{' + TRAILERS_SECTION_KEY + '}}', trailersSectionContent)

        # Dog section
        DOG_SECTION_KEY: str = 'dogSection'
        dogSectionContent: str = dogController.showDogView(translations)
        rentalDetailsView = rentalDetailsView.replace('{{' + DOG_SECTION_KEY + '}}', dogSectionContent)

        # Price Information section
        PRICE_INFORMATION_SECTION_KEY: str = 'priceInformation'
        rentalDetailsView = rentalDetailsView.replace('{{' + PRICE_INFORMATION_SECTION_KEY + '}}', priceInformation)

        # Price Information section
        CHECK_OUTINFORMATION_SECTION_KEY: str = 'checkOutinformation'
        rentalDetailsView = rentalDetailsView.replace('{{' + CHECK_OUTINFORMATION_SECTION_KEY + '}}', checkOutinformation)

        return rentalDetailsView

    @classmethod
    def __readRentalDetailsSectionHtml(cls) -> str:
        """
        @summary: Read in section_rentalDetails.html from templates folder.
        @param cls: RentalDetailsView cls parameter.
        @returns: Returns contents of html file.
        """
        rentalDetailsSectionHtml: str = None

        try:
            with open(cls.RENTAL_DETAILS_SECTION_FILE_NAME, 'r', encoding = 'utf-8') as f:
                rentalDetailsSectionHtml = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.RENTAL_DETAILS_SECTION_FILE_NAME} file not found!")
            rentalDetailsSectionHtml = None

        except Exception as e:
            print(f"Exception Error: reading {cls.RENTAL_DETAILS_SECTION_FILE_NAME}: {e}")
            rentalDetailsSectionHtml = None

        return rentalDetailsSectionHtml
