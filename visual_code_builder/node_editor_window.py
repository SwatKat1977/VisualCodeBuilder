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
import typing
from PySide6 import QtWidgets
from node_editor_window_graphics_scene import NodeEditorWindowGraphicsScene


class NodeEditorWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout: typing.Optional[QtWidgets.QVBoxLayout] = None
        self.view: typing.Optional[QtWidgets.QGraphicsView] = None
        self.graphics_scene: typing.Optional[QtWidgets.QGraphicsScene] = None

        self.init()

    def init(self):
        # x offset, y offset, width, height
        self.setGeometry(200, 200, 1024, 768)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create graphics scene
        self.graphics_scene = NodeEditorWindowGraphicsScene()

        # Create graphics view
        self.view = QtWidgets.QGraphicsView(self)
        self.view.setScene(self.graphics_scene)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()
