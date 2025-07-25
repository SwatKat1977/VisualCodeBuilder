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
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


class NodeSocketGraphics(QtWidgets.QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._radius = 6.0
        self._background_colour = QtGui.QColor("#FFFF7700")
        self._outline_colour = QtGui.QColor("#FF000000")
        self._outline_width = 0.5

        self._pen = QtGui.QPen(self._outline_colour)
        self._pen.setWidthF(self._outline_width)
        self._brush = QtGui.QBrush(self._background_colour)

    def paint(self, painter, style_options, widget=None):
        # pylint: disable=unused-argument
        """
        Override QGraphicsItem's paint method to draw the socket.
        """

        # Paint the circle
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self._radius,
                            -self._radius,
                            2 * self._radius,
                            2 * self._radius)

    def boundingRect(self):
        """
        Override QGraphicsItem's boundingRect method to determine the bounding
        box for the graphics item """
        return QtCore.QRectF(
            -self._radius - self._outline_width,
            -self._radius - self._outline_width,
            2 * (self._radius + self._outline_width),
            2 * (self._radius + self._outline_width)
        )
