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
from PySide6.QtWidgets import QGraphicsItem


class NodeConnectorGraphics(QtWidgets.QGraphicsPathItem):
    def __init__(self, connector, parent=None):
        super().__init__(parent)

        self.connector = connector

        self._colour_unselected = QtGui.QColor("#001000")
        self._colour_selected = QtGui.QColor("#00ff00")
        self._pen_unselected = QtGui.QPen(self._colour_unselected)
        self._pen_selected = QtGui.QPen(self._colour_selected)
        self._pen_unselected.setWidthF(2.0)
        self._pen_selected.setWidthF(2.0)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setZValue(-1)

        # X, Y
        self._position_source = [0, 0]

        # X, Y
        self._position_destination = [200, 100]

    def set_source(self, source_x: int, source_y: int):
        self._position_source = [source_x, source_y]

    def set_destination(self, destination_x: int, destination_y: int):
        self._position_destination = [destination_x, destination_y]

    def paint(self, painter, _option, _widget=None):
        self.update_path()

        painter.setPen(self._pen_unselected if not self.isSelected() else
                       self._pen_selected)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.BrushStyle.NoBrush))
        painter.drawPath(self.path())

    def update_path(self):
        """ Calculate path """
        raise NotImplementedError(
            "NodeConnectorGraphics::update_path() is not implemented")
