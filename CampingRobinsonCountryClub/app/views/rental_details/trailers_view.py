# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of rental trailers details.
"""

from pathlib import Path

from models.rental_details import TrailersModel
from views.rental_details import TrailerView
from controllers.rental_details import TrailerController


class TrailersView():
    """
    This class handles the view of rental trailers details.
    """

    # Class variables
    TRAILER_BASE_TABLE_FILE_CONTENT: str = None
    TRAILER_BASE_TABLE_FILE_NAME: str = 'table_trailerBase.html'
    TRAILER_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('templates', 'rental_details', TRAILER_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        Rental trailers details views.

        Args:
            self: TrailersView self parameter.
        """
        if self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.TRAILER_BASE_TABLE_FILE_CONTENT = self.__read_trailer_base_table_html()

    @classmethod
    def show_trailers_view(cls, translations: dict, trailers_model: TrailersModel) -> str:
        """
        Create the full trailers view.

        Args:
            cls: TrailersView cls parameter.
            translations: Language dictionary.
            trailers_model: Trailer models.
        Returns:
            Returns a full displayable trailers html code piece.
        """
        # 1. replaces translation texts
        trailers_view: str = cls.TRAILER_BASE_TABLE_FILE_CONTENT
        try:
            for key, item_value in translations['rentalDetails']['trailerDetails'].items():
                trailers_view = trailers_view.replace('{{' + key + '}}', item_value)
        except KeyError as e:
            print(f"KeyError exception in {cls.__class__.__name__}: {e}!")

        # 2. generating and replaces trailerTableRows in the content
        trailers_table_rows: str = str()
        for i in trailers_model:
            trailer_view: TrailerView = TrailerView()
            trailer_controller: TrailerController = TrailerController(i, trailer_view)
            trailers_table_rows = trailers_table_rows + trailer_controller.show_trailer_view(translations)

        TRAILER_TABLE_ROWS_KEY: str = 'trailerTableRows'
        trailers_view = trailers_view.replace('{{' + TRAILER_TABLE_ROWS_KEY + '}}', trailers_table_rows)

        return trailers_view

    @classmethod
    def __read_trailer_base_table_html(cls) -> str:
        """
        Read in table_trailerBase.html from templates folder.

        Args:
            cls: TrailersView cls parameter.
        Returns:
            Returns contents of html file.
        """
        trailer_base_table_html: str = None

        try:
            with open(cls.TRAILER_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                trailer_base_table_html = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.TRAILER_BASE_TABLE_FILE_PATH} file not found!")
            trailer_base_table_html = None

        except Exception as e:
            print(f"Exception Error: reading {cls.TRAILER_BASE_TABLE_FILE_PATH}: {e}")
            trailer_base_table_html = None

        return trailer_base_table_html

    @classmethod
    def __str__(cls) -> str:
        """
        A function of a class that can return class state.

        Args:
            cls: TrailersView self parameter.
        """
        pass
