# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of dog details.
"""

from pathlib import Path


class DogView():
    """
    This class handles the view of dog details.
    """

    # Class variables
    DOG_BASE_TABLE_FILE_CONTENT: str = None
    DOG_BASE_TABLE_FILE_NAME: str = 'table_dogBase.html'
    DOG_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('templates', 'rental_details', DOG_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        Dog details views.

        Args:
            self: DogView self parameter.
        """
        if self.__class__.DOG_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.DOG_BASE_TABLE_FILE_CONTENT = self.__read_dog_base_table_html()

    @classmethod
    def show_dog_view(cls, translations: dict, lei_price_per_night: int, eur_price_per_night: int) -> str:
        """
        Create the full tent view.

        Args:
            cls: DogView cls parameter.
            translations: Language dictionary.
            lei_price_per_night: Price / Night in Lei.
            eur_price_per_night: Price / Night in Eur.
        Returns:
            Returns a full displayable dog html code piece.
        """
        # 1. replaces translation texts
        dog_view: str = cls.DOG_BASE_TABLE_FILE_CONTENT
        try:
            for key, item_value in translations['rentalDetails']['dogDetails'].items():
                dog_view = dog_view.replace('{{' + key + '}}', item_value)
        except KeyError as e:
            print(f"KeyError exception in {cls.__class__.__name__}: {e}!")

        # 2. generating and replaces dogTableRows in the content
        dog_name: str = translations['rentalDetails']['dogDetails']['dog']
        price_detail: str = translations['rentalDetails']['dogDetails']['priceDetail']

        capacity_data_cell: str = '<td>' + dog_name + '</td>'
        lei_data_cell: str = '<td>' + str(lei_price_per_night) + price_detail + '</td>'
        eur_data_cell: str = '<td>' + str(eur_price_per_night) + price_detail + '</td>'

        dog_table_rows: str = '<tr>' + capacity_data_cell + lei_data_cell + eur_data_cell + "</tr>"

        DOG_TABLE_ROWS_KEY: str = 'dogTableRows'
        dog_view = dog_view.replace('{{' + DOG_TABLE_ROWS_KEY + '}}', dog_table_rows)

        return dog_view

    @classmethod
    def __read_dog_base_table_html(cls) -> str:
        """
        Read in table_dogBase.html from templates folder.

        Args:
            cls: DogView cls parameter.
        Returns:
            Returns contents of html file.
        """
        dog_base_table_html: str = None

        try:
            with open(cls.DOG_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                dog_base_table_html = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.DOG_BASE_TABLE_FILE_PATH} file not found!")
            dog_base_table_html = None

        except Exception as e:
            print(f"Exception Error: reading {cls.DOG_BASE_TABLE_FILE_PATH}: {e}")
            dog_base_table_html = None

        return dog_base_table_html

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            cls: DogView cls parameter.
        """
        return self.show_dog_view()
