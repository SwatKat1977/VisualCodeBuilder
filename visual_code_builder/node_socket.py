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
from enum import Enum
from node_socket_graphics import NodeSocketGraphics


class SocketPosition(Enum):
    """ Socket start position enumeration """

    LEFT_TOP = 1
    LEFT_BOTTOM = 2
    RIGHT_TOP = 3
    RIGHT_BOTTOM = 4


class NodeSocket:
    def __init__(self, parent_node,
                 position_index=0,
                 position: SocketPosition = SocketPosition.LEFT_TOP):
        self._parent_node = parent_node
        self._position_index = position_index
        self._position = position

        self.socket_graphics = NodeSocketGraphics(self._parent_node.node_graphics)

        socket_pos = self._parent_node.calculate_socket_position(position_index,
                                                                 position)
        self.socket_graphics.setPos(*socket_pos)

        self._connector = None

    @property
    def parent_node(self):
        return self._parent_node

    def get_socket_position(self):
        return self._parent_node.calculate_socket_position(
            self._position_index, self._position)

    def set_connector(self, connector=None):
        self._connector = connector

    @property
    def connector(self):
        return self._connector

    def has_connector(self) -> bool:
        return self._connector is not None
