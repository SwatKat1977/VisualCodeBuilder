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
from node_graphics import NodeGraphics
from node_socket import NodeSocket, SocketPosition
from node_widget import NodeWidget


class Node:
    def __init__(self, scene, title='DEFAULT', inputs=None, outputs=None):
        self.scene = scene
        self.title = title

        self.contents = NodeWidget()
        self.node_graphics = NodeGraphics(self)

        self.scene.add_node(self)
        self.scene.graphics_scene.addItem(self.node_graphics)

        self._socket_spacing = 30

        self.inputs: list = []
        self.outputs: list = []

        if inputs is not None:
            input_idx = 0
            for socket in inputs:
                new_socket = NodeSocket(parent_node=self,
                                        position_index=input_idx,
                                        position=SocketPosition.LEFT_TOP)
                input_idx += 1
                self.inputs.append(new_socket)

        if outputs is not None:
            output_idx = 0
            for socket in outputs:
                new_socket = NodeSocket(parent_node=self,
                                        position_index=output_idx,
                                        position=SocketPosition.RIGHT_TOP)
                output_idx += 1
                self.outputs.append(new_socket)

    @property
    def position(self):
        return self.node_graphics.pos()

    def set_position(self, x_position: int, y_position: int):
        self.node_graphics.setPos(x_position, y_position)

    def calculate_socket_position(self, index : int, position : SocketPosition):
        """
        Calculate and return the X,Y position for a socket.
        """

        x_pos = 0 if position in (SocketPosition.LEFT_TOP,
                                  SocketPosition.LEFT_BOTTOM) else \
            self.node_graphics.width

        if position in (SocketPosition.LEFT_BOTTOM, SocketPosition.RIGHT_BOTTOM):
            y_pos = (self.node_graphics.height -
                     self.node_graphics.edge_roundness -
                     self.node_graphics.text_padding -
                     index * self._socket_spacing)

        else:
            y_pos = (self.node_graphics.title_height +
                     self.node_graphics.text_padding +
                     self.node_graphics.edge_roundness + index *
                     self._socket_spacing)

        return x_pos, y_pos
