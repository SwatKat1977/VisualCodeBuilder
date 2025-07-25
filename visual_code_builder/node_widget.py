"""
This source file is part of Visual Code Builder
For the latest info, see https://github.com/SwatKat1977/VisualCodeBuilder

Copyright 2025 Visual Code Builder Development Team

This program is free software : you can redistribute it and /or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.If not, see < https://www.gnu.org/licenses/>.
"""
from PySide6 import QtWidgets


class NodeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._label = None
        self._layout = None

        self.initialise()

    def initialise(self):
        # Create vertical box layout.
        self._layout = QtWidgets.QVBoxLayout()

        # Set no 0 margins to remove border.
        self._layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self._layout)

        self._label = QtWidgets.QLabel("Test Widget")
        self._layout.addWidget(self._label)
        self._layout.addWidget(QtWidgets.QTextEdit("Hello world"))
