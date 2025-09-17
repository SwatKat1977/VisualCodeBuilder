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
from node_socket import SocketPosition


class NodeConnectorGraphicsBezier(NodeConnectorGraphics):
    def update_path(self):
        source = self._position_source
        destination = self._position_destination
        distance = (destination[0] - source[0]) * 0.5

        cpx_source = +distance
        cpx_destination = -distance
        cpy_source = 0
        cpy_destination = 0

        starting_socket_position = self.connector.start_socket.position
        if (source[0] > destination[0] and starting_socket_position in (
                SocketPosition.RIGHT_TOP, SocketPosition.RIGHT_BOTTOM)) or \
            (source[0] < destination[0] and starting_socket_position in (
                SocketPosition.LEFT_BOTTOM, SocketPosition.LEFT_TOP)):
            cpx_destination *= -1
            cpx_source *= -1

        path = QtGui.QPainterPath(QtCore.QPointF(self._position_source[0],
                                                 self._position_source[1]))
        path.cubicTo(source[0] + cpx_source,
                     source[1] + cpy_source,
                     destination[0] + cpx_destination,
                     destination[1] + cpy_destination,
                     self._position_destination[0],
                     self._position_destination[1])

        self.setPath(path)
