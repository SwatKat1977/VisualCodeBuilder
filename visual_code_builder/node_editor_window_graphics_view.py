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


class NodeEditorWindowGraphicsView(QtWidgets.QGraphicsView):

    def __init__(self, graphics_scene, parent=None):
        super().__init__(parent)
        self.graphics_scene = graphics_scene

        self.initialise()

        self.setScene(self.graphics_scene)

    def initialise(self):
        # Set Anti-aliasing.
        self.setRenderHints(QtGui.QPainter.Antialiasing |
                            QtGui.QPainter.TextAntialiasing |
                            QtGui.QPainter.TextAntialiasing |
                            QtGui.QPainter.SmoothPixmapTransform)

        # Force redraw on dragging to stop 'canvas tearing'.
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)

        # Hide the scrollbars.
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
