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
                 type: NodeConnectorType = NodeConnectorType.DIRECT):
        self.scene = scene
        self.start_socket = start_socket
        self.end_socket = end_socket

        self.connector_graphics = NodeConnectorGraphicsDirect(self) \
            if type == NodeConnectorType.DIRECT else NodeConnectorGraphicsBezier(self)

        self.scene.graphics_scene.addItem(self.connector_graphics)
