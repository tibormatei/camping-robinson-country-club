# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TentView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental tent details.
"""


class TentView() :
    """
    @summary: This class handles the view of rental tent details.
    """

    # Class variables
    TENT_BASE_TABLE : str = None

    TENT_BASE_TABLE_FILE_NAME : str = 'table_tentBase.html'

    def __init__(self) :
        """
        @summary: Rental tent details views.
        @param self: TentView self parameter.
        """
        if self.TENT_BASE_TABLE is None :
            self.TENT_BASE_TABLE =  self.__readTentBaseTableHtml()

    @classmethod
    def __readTentBaseTableHtml(cls) -> str :
        """
        @summary: Read in table_tentBase.html from templates folder.
        @param cls: TentView cls parameter.
        @returns: Returns contents of html file.
        """
        tentBaseTableHtml : str = None

        try :
            with open(cls.TENT_BASE_TABLE_FILE_NAME, 'r', encoding = 'utf-8') as f :
                tentBaseTableHtml = f.read()

        except FileNotFoundError :
            print(f"Exception Error: {cls.TENT_BASE_TABLE_FILE_NAME} file not found!")
            tentBaseTableHtml = None

        except Exception as e :
            print(f"Exception Error: reading {cls.TENT_BASE_TABLE_FILE_NAME}: {e}")
            tentBaseTableHtml = None

        return tentBaseTableHtml

# To Do here