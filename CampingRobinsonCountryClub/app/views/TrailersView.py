# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TrailersView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental trailers details.
"""

from pathlib import Path
from collections.abc import Iterator

from app.views import TrailerView


class TrailersView():
    """
    @summary: This class handles the view of rental trailers details.
    """

    # Class variables
    TRAILER_BASE_TABLE_FILE_CONTENT: str = None
    TRAILER_BASE_TABLE_FILE_NAME: str = 'table_trailerBase.html'
    TRAILER_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.joinpath('templates', TRAILER_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        @summary: Rental trailers details views.
        @param self: TrailersView self parameter.
        """
        if self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT = self.__readTrailerBaseTableHtml()

    @classmethod
    def showTrailersView(cls, TRANSLATIONS: dict, trailersData: Iterator, trailerView: TrailerView) -> str:
        """
        @summary: Create the full trailers view.
        @param cls: TrailersView cls parameter.
        @param TRANSLATIONS: Language dictionary.
        @param trailersData: Trailer model datas.
        @param trailerView: Delegates Trailer's View class from the controller.
        @returns: Returns a full displayable trailers html code piece.
        """
        # 1. replaces translation texts
        trailersView: str = cls.TRAILER_BASE_TABLE_FILE_CONTENT
        try:
            for key, itemValue in TRANSLATIONS['rentalDetails']['trailerDetails'].items():
                trailersView = trailersView.replace('{{' + key + '}}', itemValue)
        except KeyError as e:
            print(f"KeyError exception: {e}!")

        # 2. generating and replaces trailerTableRows in the content
        trailersTableRows: str = str()
        for i in trailersData:
            trailersTableRows = trailersTableRows + trailerView.showTrailerView(i.TrailerCapacity, i.LeiPrice, i.EurPrice)

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
        A function of a class that can return class state.
        """
        return cls.showTrailersView()
