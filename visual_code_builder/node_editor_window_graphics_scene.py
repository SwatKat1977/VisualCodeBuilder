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
import math
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


class NodeEditorWindowGraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene
        self.grid_size: int = 20
        self.grid_squares: int = 5

        # Scene background colour
        self.colour_background: QtGui.QColor = QtGui.QColor("#393939")

        # Grid line (light)
        self.grid_line_light_colour: QtGui.QColor = QtGui.QColor("#2f2f2f")
        self.light_grid_line_pen: QtGui.QPen = QtGui.QPen(self.grid_line_light_colour)
        self.light_grid_line_pen.setWidth(1)

        # Grid line (dark)
        self.grid_line_dark_colour: QtGui.QColor = QtGui.QColor("#292929")
        self.dark_grid_line_pen : QtGui.QPen = QtGui.QPen(self.grid_line_dark_colour)
        self.dark_grid_line_pen.setWidth(2)

        self.setBackgroundBrush(self.colour_background)

    def set_scene_rectangle(self, width: int, height: int):
        # Set focus of the window to be right in the middle
        self.setSceneRect(-width // 2, -height // 2, width, height)

    def drawBackground(self, painter, rect):
        """ PyQt method that is called every time the view is drawn. """
        super().drawBackground(painter, rect)

        # Create grid
        left: int = int(math.floor(rect.left()))
        right: int = int(math.ceil(rect.right()))
        top: int = int(math.floor(rect.top()))
        bottom: int = int(math.ceil(rect.bottom()))

        first_vertical_line = left - (left % self.grid_size)
        first_horizontal_line = top - (top % self.grid_size)

        # Compute lines to be drawn
        lines_light = []
        lines_dark = []
        for x_position in range(first_vertical_line, right, self.grid_size):
            if x_position % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QtCore.QLine(x_position, top, x_position, bottom))
            else:
                lines_dark.append(QtCore.QLine(x_position, top, x_position, bottom))

        for y_position in range(first_horizontal_line, bottom, self.grid_size):
            if y_position % (self.grid_size * self.grid_squares) != 0:
                lines_light.append(QtCore.QLine(left, y_position, right, y_position))
            else:
                lines_dark.append(QtCore.QLine(left, y_position, right, y_position))

        # Draw light Lines
        painter.setPen(self.light_grid_line_pen)
        painter.drawLines(lines_light)

        # Draw dark Lines
        painter.setPen(self.dark_grid_line_pen)
        painter.drawLines(lines_dark)
