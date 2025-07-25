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
from node_socket import NodeSocket
from node_widget import NodeWidget


class Node:
    def __init__(self, scene, title='DEFAULT', inputs=None, outputs=None):
        self.scene = scene
        self.title = title

        self.contents = NodeWidget()
        self.node_graphics = NodeGraphics(self)

        self.scene.add_node(self)
        self.scene.graphics_scene.addItem(self.node_graphics)

        self._inputs: list = []
        self._outputs: list = []

        if inputs is not None:
            for socket in inputs:
                new_socket = NodeSocket(parent_node=self)
                self._inputs.append(new_socket)

        if outputs is not None:
            for socket in outputs:
                new_socket = NodeSocket(parent_node=self)
                self._outputs.append(new_socket)
