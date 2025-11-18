# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of rental tent details.
"""

from pathlib import Path


class TentView():
    """
    This class handles the view of rental tent details.
    """

    # Class variables
    TENT_BASE_TABLE_FILE_CONTENT: str = None
    TENT_BASE_TABLE_FILE_NAME: str = 'table_tentBase.html'
    TENT_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('templates', 'rental_details', TENT_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        Rental tent details views.

        Args:
            self: TentView self parameter.
        """
        if self.__class__.TENT_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.TENT_BASE_TABLE_FILE_CONTENT = self.__read_tent_base_table_html()

    @classmethod
    def show_tent_view(cls, translations: dict, tent_capacities: list[str], lei_price_per_person: int, eur_price_per_person: int) -> str:
        """
        Create the full tent view.

        Args:
            cls: TentView cls parameter.
            translations: Language dictionary.
            tent_capacities: Capacities dates.
            lei_price_per_person: Price in Lei.
            eur_price_per_person: Price in Eur.
        Returns:
            Returns a full displayable tent html code piece.
        """
        # 1. replaces translation texts
        tent_view: str = cls.TENT_BASE_TABLE_FILE_CONTENT
        try:
            for key, item_value in translations['rentalDetails']['tentDetails'].items():
                tent_view = tent_view.replace('{{' + key + '}}', item_value)
        except KeyError as e:
            print(f"KeyError exception in {cls.__class__.__name__}: {e}!")

        # 2. generating and replaces tent_table_rows in the content
        tent_table_rows: str = str()
        if len(tent_capacities) > 0:
            person_name: str = translations['rentalDetails']['tentDetails']['personName']

            capacity_data_cell: str = '<td>' + tent_capacities[0] + ' ' + person_name + '</td>'
            lei_data_cell: str = '<td rowspan="' + str(len(tent_capacities)) + '">' + str(lei_price_per_person) + '</td>'
            eur_data_cell: str = '<td rowspan="' + str(len(tent_capacities)) + '">' + str(eur_price_per_person) + '</td>'
            tent_table_rows = '<tr>' + capacity_data_cell + lei_data_cell + eur_data_cell + "</tr>"
            for i in range(1, len(tent_capacities)):
                tent_table_rows = tent_table_rows + '<tr><td>' + tent_capacities[i] + ' ' + person_name + '</td></tr>'
        else:
            capacity_data_cell: str = '<td></td>'
            lei_data_cell: str = '<td>' + str(lei_price_per_person) + '</td>'
            eur_data_cell: str = '<td>' + str(eur_price_per_person) + '</td>'
            tent_table_rows = '<tr>' + capacity_data_cell + lei_data_cell + eur_data_cell + "</tr>"

        TENT_TABLE_ROWS_KEY: str = 'tentTableRows'
        tent_view = tent_view.replace('{{' + TENT_TABLE_ROWS_KEY + '}}', tent_table_rows)

        return tent_view

    @classmethod
    def __read_tent_base_table_html(cls) -> str:
        """
        Read in table_tentBase.html from templates folder.

        Args:
            cls: TentView cls parameter.
        Returns:
            Returns contents of html file.
        """
        tent_base_table_html: str = None

        try:
            with open(cls.TENT_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                tent_base_table_html = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.TENT_BASE_TABLE_FILE_PATH} file not found!")
            tent_base_table_html = None

        except Exception as e:
            print(f"Exception Error: reading {cls.TENT_BASE_TABLE_FILE_PATH}: {e}")
            tent_base_table_html = None

        return tent_base_table_html

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            cls: TentView cls parameter.
        """
        return self.show_tent_view()
