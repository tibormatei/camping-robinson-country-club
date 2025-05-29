# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: DogView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of dog details.
"""

from pathlib import Path


class DogView():
    """
    @summary: This class handles the view of dog details.
    """

    # Class variables
    DOG_BASE_TABLE_FILE_CONTENT: str = None
    DOG_BASE_TABLE_FILE_NAME: str = 'table_dogBase.html'
    DOG_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.joinpath('templates', DOG_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        @summary: Dog details views.
        @param self: DogView self parameter.
        """
        if self.__class__.DOG_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.DOG_BASE_TABLE_FILE_CONTENT = self.__readDogBaseTableHtml()

    @classmethod
    def showDogView(cls, translations: dict, leiPricePerNight: int, eurPricePerNight: int) -> str:
        """
        @summary: Create the full tent view.
        @param cls: DogView cls parameter.
        @param translations: Language dictionary.
        @param leiPricePerNight: Price / Night in Lei.
        @param eurPricePerNight: Price / Night in Eur.
        @returns: Returns a full displayable dog html code piece.
        """
        # 1. replaces translation texts
        dogView: str = cls.DOG_BASE_TABLE_FILE_CONTENT
        try:
            for key, itemValue in translations['rentalDetails']['dogDetails'].items():
                dogView = dogView.replace('{{' + key + '}}', itemValue)
        except KeyError as e:
            print(f"KeyError exception: {e}!")

        # 2. generating and replaces dogTableRows in the content
        dogName: str = translations['rentalDetails']['dogDetails']['dog']
        priceDetail: str = translations['rentalDetails']['dogDetails']['priceDetail']

        capacityDataCell: str = '<td>' + dogName + '</td>'
        leiDataCell: str = '<td>' + str(leiPricePerNight) + priceDetail + '</td>'
        eurDataCell: str = '<td>' + str(eurPricePerNight) + priceDetail + '</td>'

        dogTableRows: str = '<tr>' + capacityDataCell + leiDataCell + eurDataCell + "</tr>"

        DOG_TABLE_ROWS_KEY: str = 'dogTableRows'
        dogView = dogView.replace('{{' + DOG_TABLE_ROWS_KEY + '}}', dogTableRows)

        return dogView

    @classmethod
    def __readDogBaseTableHtml(cls) -> str:
        """
        @summary: Read in table_dogBase.html from templates folder.
        @param cls: DogView cls parameter.
        @returns: Returns contents of html file.
        """
        dogBaseTableHtml: str = None

        try:
            with open(cls.DOG_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                dogBaseTableHtml = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.DOG_BASE_TABLE_FILE_PATH} file not found!")
            dogBaseTableHtml = None

        except Exception as e:
            print(f"Exception Error: reading {cls.DOG_BASE_TABLE_FILE_PATH}: {e}")
            dogBaseTableHtml = None

        return dogBaseTableHtml

    @classmethod
    def __str__(cls) -> str:
        """
        A function of a class that can return class state.
        """
        return cls.showDogView()
