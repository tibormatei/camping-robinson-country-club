# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental trailers details.
"""

from pathlib import Path

from models import TrailersModel
from views import TrailerView
from controllers import TrailerController


class TrailersView():
    """
    @summary: This class handles the view of rental trailers details.
    """

    # Class variables
    TRAILER_BASE_TABLE_FILE_CONTENT: str = None
    TRAILER_BASE_TABLE_FILE_NAME: str = 'table_trailerBase.html'
    TRAILER_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.joinpath('templates', 'rental_details', TRAILER_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        @summary: Rental trailers details views.
        @param self: TrailersView self parameter.
        """
        if self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT = self.__readTrailerBaseTableHtml()

    @classmethod
    def showTrailersView(cls, translations: dict, trailersModel: TrailersModel) -> str:
        """
        @summary: Create the full trailers view.
        @param cls: TrailersView cls parameter.
        @param translations: Language dictionary.
        @param trailerControllers: Trailer contollers.
        @returns: Returns a full displayable trailers html code piece.
        """
        # 1. replaces translation texts
        trailersView: str = cls.TRAILER_BASE_TABLE_FILE_CONTENT
        try:
            for key, itemValue in translations['rentalDetails']['trailerDetails'].items():
                trailersView = trailersView.replace('{{' + key + '}}', itemValue)
        except KeyError as e:
            print(f"KeyError exception: {e}!")

        # 2. generating and replaces trailerTableRows in the content
        trailersTableRows: str = str()
        for i in trailersModel:
            trailerView: TrailerView = TrailerView()
            trailerController: TrailerController = TrailerController(i, trailerView)
            trailersTableRows = trailersTableRows + trailerController.showTrailerView(translations)

        TRAILER_TABLE_ROWS_KEY: str = 'trailerTableRows'
        trailersView = trailersView.replace('{{' + TRAILER_TABLE_ROWS_KEY + '}}', trailersTableRows)

        return trailersView

    @classmethod
    def __readTrailerBaseTableHtml(cls) -> str:
        """
        @summary: Read in table_trailerBase.html from templates folder.
        @param cls: TrailersView cls parameter.
        @returns: Returns contents of html file.
        """
        trailerBaseTableHtml: str = None

        try:
            with open(cls.TRAILER_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                trailerBaseTableHtml = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.TRAILER_BASE_TABLE_FILE_PATH} file not found!")
            trailerBaseTableHtml = None

        except Exception as e:
            print(f"Exception Error: reading {cls.TRAILER_BASE_TABLE_FILE_PATH}: {e}")
            trailerBaseTableHtml = None

        return trailerBaseTableHtml

    @classmethod
    def __str__(cls) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: TrailersView self parameter.
        """
        pass
