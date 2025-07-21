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
from node_editor_window_graphics_scene import NodeEditorWindowGraphicsScene


class Scene:

    def __init__(self):
        self.nodes: list = []
        self.connections: list = []
        self.scene_width: int = 64000
        self.scene_height: int = 64000

        self.graphics_scene = None

        self.initialise()

    def initialise(self):
        # Create graphics scene
        self.graphics_scene = NodeEditorWindowGraphicsScene(self)
        self.graphics_scene.set_scene_rectangle(self.scene_width, self.scene_height)

    def add_node(self, node):
        self.nodes.append(node)

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_node(self, node):
        self.nodes.remove(node)

    def remove_connection(self, connection):
        self.connections.remove(connection)
