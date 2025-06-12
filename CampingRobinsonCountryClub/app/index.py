# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: index.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class creates index.html.
"""

from pathlib import Path


class Index():
    """
    @summary: This class creates index.html.
    """

    # Class variables
    INDEX_FILE_NAME: str = 'index.html'

    def __init__(self, path: str):
        """
        @summary: The init method initialize instance attributes.
        @param self: Index self parameter.
        @param path: Root path.
        """
        self._index_file_path: Path = Path(path).joinpath('templates', self.__class__.INDEX_FILE_NAME)
        self._index_file_content: str = self.__readIndexHtml()

    def buildIndexPage(self) -> str:
        return self._index_file_content

    def __readIndexHtml(cls) -> str:
        """
        @summary: Read in index.html from templates folder.
        @param cls: Index cls parameter.
        @returns: Returns contents of html file.
        """
        indexHtml: str = None

        try:
            with open(cls._index_file_path, 'r', encoding = 'utf-8') as f:
                indexHtml = f.read()

        except FileNotFoundError:
            print(f"Exception Error: {cls._index_file_path} file not found!")
            indexHtml = "Server error!"

        except Exception as e:
            print(f"Exception Error: reading {cls._index_file_path}: {e}")
            indexHtml = "Server html file error!"

        return indexHtml

    @classmethod
    def __str__(cls) -> str:
        """
        A function of a class that can return index.html page.
        """
        return cls.buildIndexPage()
