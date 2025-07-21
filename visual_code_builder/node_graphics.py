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


class NodeGraphics(QtWidgets.QGraphicsItem):
    def __init__(self, node, title: str = "Node Graphics Item", parent=None):
        super().__init__(parent)

        self._title = title

        # Node settings
        self._width = 180
        self._height = 240
        self._title_height = 25
        self._text_padding = 10.0

        self._edge_roundness = 10

        # Pens for drawing the node edge
        self._pen_outline_unselected = QtGui.QPen(QtGui.QColor("#7F000000"))
        self._pen_outline_selected = QtGui.QPen(QtGui.QColor("#FFFFA637"))

        # Brush for the title
        self._brush_title = QtGui.QBrush(QtGui.QColor("#FF313131"))

        # Node background brush
        self._brush_background = QtGui.QBrush(QtGui.QColor("#E3212121"))

        self._title_colour = QtCore.Qt.white
        self._title_font = QtGui.QFont("Ubuntu", 10)

        self.initialise_title()
        self.title = title

        self.initialise()

    def initialise(self):
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

    def initialise_title(self):
        # Create title
        self.title_item = QtWidgets.QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_colour)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self._text_padding, 0)
        self.title_item.setTextWidth(self._width - 2 * self._text_padding)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title
        self.title_item.setPlainText(self._title)

    def boundingRect(self) -> QtCore.QRectF:
        """
        Implement QGraphicsItem boundingRect() to Define a bounding
        rectangle
        """
        return QtCore.QRectF(
            0,
            0,
            2 * self._edge_roundness + self._width,
            2 * self._edge_roundness + self._height
        ).normalized()

    def paint(self, painter, _unused1, _unused2):
        """
        Override the paint method for a rounded rectangle `Node`
        """

        # Paint the node title
        path_title: QtGui.QPainterPath = QtGui.QPainterPath()
        path_title.setFillRule(QtCore.Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self._width, self._title_height,
                                  self._edge_roundness, self._edge_roundness)
        path_title.addRect(0, self._title_height - self._edge_roundness,
                           self._edge_roundness, self._edge_roundness)
        path_title.addRect(self._width - self._edge_roundness,
                           self._title_height - self._edge_roundness,
                           self._edge_roundness, self._edge_roundness)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # Paint the node body
        path_body = QtGui.QPainterPath()
        path_body.setFillRule(QtCore.Qt.WindingFill)
        path_body.addRoundedRect(0, self._title_height, self._width,
                                 self._height - self._title_height,
                                 self._edge_roundness, self._edge_roundness)
        path_body.addRect(0, self._title_height, self._edge_roundness,
                          self._edge_roundness)
        path_body.addRect(self._width - self._edge_roundness,
                          self._title_height, self._edge_roundness,
                          self._edge_roundness)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_body.simplified())

        # Paint the node outline
        path_outline = QtGui.QPainterPath()
        path_outline.addRoundedRect(0, 0, self._width, self._height,
                                    self._edge_roundness, self._edge_roundness)
        painter.setPen(self._pen_outline_unselected if not self.isSelected()
                       else self._pen_outline_selected)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
