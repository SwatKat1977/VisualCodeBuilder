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

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MiddleButton:
            self._middle_mouse_button_press(event)

            """
        elif event.button() == QtCore.Qt.LeftButton:
            self._left_mouse_button_press(event)

        elif event.button() == QtCore.Qt.RightButton:
            self._right_mouse_button_press(event)
            """
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # Disabling invalid-name as this is a QT override method and cannot be
        # changed.
        # pylint: disable=invalid-name

        if event.button() == QtCore.Qt.MiddleButton:
            self._middle_mouse_button_release(event)

            """
        elif event.button() == QtCore.Qt.LeftButton:
            self._left_mouse_button_release(event)

        elif event.button() == QtCore.Qt.RightButton:
            self._right_mouse_button_release(event)
            """
        else:
            super().mouseReleaseEvent(event)

    def _middle_mouse_button_press(self, event):
        release_event = QtGui.QMouseEvent(
            QtCore.QEvent.MouseButtonRelease,
            event.localPos(), event.screenPos(),
            QtCore.Qt.LeftButton, QtCore.Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(release_event)

        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

        fake_event = QtGui.QMouseEvent(event.type(),
                                       event.localPos(),
                                       event.screenPos(),
                                       QtCore.Qt.LeftButton,
                                       event.buttons() | QtCore.Qt.LeftButton,
                                       event.modifiers())
        super().mousePressEvent(fake_event)

    def _middle_mouse_button_release(self, event):
        fake_event = QtGui.QMouseEvent(event.type(), event.localPos(),
                                 event.screenPos(), QtCore.Qt.LeftButton,
                                 event.buttons() | QtCore.Qt.LeftButton,
                                 event.modifiers())
        super().mouseReleaseEvent(fake_event)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
