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
from node_connector_graphics import NodeConnectorGraphics


class NodeConnectorGraphicsBezier(NodeConnectorGraphics):
    def update_path(self):
        path = QtGui.QPainterPath(QtCore.QPointF(self._position_source[0],
                                                 self._position_source[1]))
        source = self._position_source
        destination = self._position_destination
        distance = (destination[0] - source[0]) * 0.5

        # If destination is on the left-hand side, we need to make the
        # distance a minus.
        if source[1] > destination[1]:
            print("Swapping")
            distance *= -1

        path.cubicTo(source[0] + distance,
                     source[1],
                     destination[0] - distance,
                     destination[1],
                     destination[0],
                     destination[1])
        self.setPath(path)