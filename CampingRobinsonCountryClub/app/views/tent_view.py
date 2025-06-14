# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental tent details.
"""

from pathlib import Path


class TentView():
    """
    @summary: This class handles the view of rental tent details.
    """

    # Class variables
    TENT_BASE_TABLE_FILE_CONTENT: str = None
    TENT_BASE_TABLE_FILE_NAME: str = 'table_tentBase.html'
    TENT_BASE_TABLE_FILE_PATH: Path = Path(__file__).parent.parent.joinpath('templates', 'rentalDetails', TENT_BASE_TABLE_FILE_NAME)

    def __init__(self):
        """
        @summary: Rental tent details views.
        @param self: TentView self parameter.
        """
        if self.__class__.TENT_BASE_TABLE_FILE_CONTENT is None:
            self.__class__.TENT_BASE_TABLE_FILE_CONTENT = self.__readTentBaseTableHtml()

    @classmethod
    def showTentView(cls, translations: dict, tentCapacities: list[str], leiPricePerPerson: int, eurPricePerPerson: int) -> str:
        """
        @summary: Create the full tent view.
        @param cls: TentView cls parameter.
        @param translations: Language dictionary.
        @param tentCapacities: Capacities dates.
        @param leiPricePerPerson: Price in Lei.
        @param eurPricePerPerson: Price in Eur.
        @returns: Returns a full displayable tent html code piece.
        """
        # 1. replaces translation texts
        tentView: str = cls.TENT_BASE_TABLE_FILE_CONTENT
        try:
            for key, itemValue in translations['rentalDetails']['tentDetails'].items():
                tentView = tentView.replace('{{' + key + '}}', itemValue)
        except KeyError as e:
            print(f"KeyError exception: {e}!")

        # 2. generating and replaces tentTableRows in the content
        tentTableRows: str = str()
        if len(tentCapacities) > 0:
            personName: str = translations['rentalDetails']['tentDetails']['personName']

            capacityDataCell: str = '<td>' + tentCapacities[0] + ' ' + personName + '</td>'
            leiDataCell: str = '<td rowspan="' + str(len(tentCapacities)) + '">' + str(leiPricePerPerson) + '</td>'
            eurDataCell: str = '<td rowspan="' + str(len(tentCapacities)) + '">' + str(eurPricePerPerson) + '</td>'
            tentTableRows = '<tr>' + capacityDataCell + leiDataCell + eurDataCell + "</tr>"
            for i in range(1, len(tentCapacities)):
                tentTableRows = tentTableRows + '<tr><td>' + tentCapacities[i] + ' ' + personName + '</td></tr>'
        else:
            capacityDataCell: str = '<td></td>'
            leiDataCell: str = '<td>' + str(leiPricePerPerson) + '</td>'
            eurDataCell: str = '<td>' + str(eurPricePerPerson) + '</td>'
            tentTableRows = '<tr>' + capacityDataCell + leiDataCell + eurDataCell + "</tr>"

        TENT_TABLE_ROWS_KEY: str = 'tentTableRows'
        tentView = tentView.replace('{{' + TENT_TABLE_ROWS_KEY + '}}', tentTableRows)

        return tentView

    @classmethod
    def __readTentBaseTableHtml(cls) -> str:
        """
        @summary: Read in table_tentBase.html from templates folder.
        @param cls: TentView cls parameter.
        @returns: Returns contents of html file.
        """
        tentBaseTableHtml: str = None

        try:
            with open(cls.TENT_BASE_TABLE_FILE_PATH, 'r', encoding = 'utf-8') as f:
                tentBaseTableHtml = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls.TENT_BASE_TABLE_FILE_PATH} file not found!")
            tentBaseTableHtml = None

        except Exception as e:
            print(f"Exception Error: reading {cls.TENT_BASE_TABLE_FILE_PATH}: {e}")
            tentBaseTableHtml = None

        return tentBaseTableHtml

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: TentView cls parameter.
        """
        return self.showTentView()
