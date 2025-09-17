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
from node_connector_graphics_bezier import NodeConnectorGraphicsBezier
from node_connector_graphics_direct import NodeConnectorGraphicsDirect
from node_connector_type import NodeConnectorType


class NodeConnector:
    def __init__(self,
                 scene,
                 start_socket,
                 end_socket,
                 connector_type: NodeConnectorType = NodeConnectorType.DIRECT):
        self.scene = scene
        self.start_socket = start_socket
        self.end_socket = end_socket

        self.start_socket.set_connector(self)

        if self.end_socket is not None:
            self.end_socket.set_connector(self)

        self.graphics = NodeConnectorGraphicsDirect(self) \
            if connector_type == NodeConnectorType.DIRECT \
            else NodeConnectorGraphicsBezier(self)

        self.update_positions()

        self.scene.graphics_scene.addItem(self.graphics)
        self.scene.add_connection(self)

    def update_positions(self):
        source_position = self.start_socket.get_socket_position()
        source_position[0] += self.start_socket.parent_node.node_graphics.pos().x()
        source_position[1] += self.start_socket.parent_node.node_graphics.pos().y()

        self.graphics.set_source(*source_position)

        if self.end_socket is not None:
            end_position = self.end_socket.get_socket_position()
            end_position[0] += self.end_socket.parent_node.node_graphics.pos().x()
            end_position[1] += self.end_socket.parent_node.node_graphics.pos().y()

            self.graphics.set_destination(*end_position)

        self.graphics.update()

    def remove_from_sockets(self):
        if self.start_socket.connector is not None:
            self.start_socket.connector = None

        if self.end_socket.connector is not None:
            self.end_socket.connector = None

        self.end_socket = None
        self.start_socket = None

    def remove(self):
        self.remove_from_sockets()
        self.scene.graphics_scene.removeItem(self.graphics)
        self.graphics = None
        self.scene.remove_connection(self)

    def __str__(self):
        return f"{hex(id(self))[2:5]}..{hex(id(self))[-4:]}"
