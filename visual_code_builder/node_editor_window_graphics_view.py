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
from node_editor_state import NodeEditorState
from node_socket_graphics import NodeSocketGraphics
from node_connector_graphics import NodeConnectorGraphics
from node_connector import NodeConnector
from node_connector_type import NodeConnectorType


class NodeEditorWindowGraphicsView(QtWidgets.QGraphicsView):
    CONNECTION_DRAG_START_THRESHOLD: int = 10
    PRINT_DEBUG_INFO: bool = True

    def __init__(self, graphics_scene, parent=None):
        super().__init__(parent)
        self.graphics_scene = graphics_scene

        self._current_state = NodeEditorState.VIEW_MODE
        self._last_lmb_click_scene_position = None
        self._connection_drag = None

        self.initialise()

        self.setScene(self.graphics_scene)

        self._zoom_clamped = True
        self._zoom_factor = 1.25
        self._current_zoom = 10
        self._zoom_step = 1
        self._zoom_min_range_clamp = 0
        self._zoom_max_range_clamp = 10


    def initialise(self):
        # Set Anti-aliasing.
        self.setRenderHints(QtGui.QPainter.RenderHint.Antialiasing |
                            QtGui.QPainter.RenderHint.TextAntialiasing |
                            QtGui.QPainter.RenderHint.TextAntialiasing |
                            QtGui.QPainter.RenderHint.SmoothPixmapTransform)

        # Force redraw on dragging to stop 'canvas tearing'.
        self.setViewportUpdateMode(
            QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate)

        # Hide the scrollbars.
        self.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Force transform to anchor centre on mouse.
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MiddleButton:
            self._middle_mouse_button_press(event)

        elif event.button() == QtCore.Qt.LeftButton:
            self._left_mouse_button_press(event)

        elif event.button() == QtCore.Qt.RightButton:
            self._right_mouse_button_press(event)

        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MiddleButton:
            self._middle_mouse_button_release(event)

        elif event.button() == QtCore.Qt.LeftButton:
            self._left_mouse_button_release(event)

        elif event.button() == QtCore.Qt.RightButton:
            self._right_mouse_button_release(event)

        else:
            super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        """
        Overrides the QGraphicsView mouse wheel event method to implement zoom
        functionality.
        """
        if event.angleDelta().y() > 0:
            zoom_factor = self._zoom_factor
            self._current_zoom += self._zoom_step

        # Calculate zoom factor (out)
        else:
            zoom_factor = 1 / self._zoom_factor
            self._current_zoom -= self._zoom_step

        # Clamp the zoom to within the min/max range.
        clamped = False
        if self._current_zoom < self._zoom_min_range_clamp:
            self._current_zoom = self._zoom_min_range_clamp
            clamped = True

        if self._current_zoom > self._zoom_max_range_clamp:
            self._current_zoom = self._zoom_max_range_clamp
            clamped = True

        # Set scene scale
        if not clamped or self._zoom_clamped is False:
            self.scale(zoom_factor, zoom_factor)

    def mouseMoveEvent(self, event):
        if self._current_state == NodeEditorState.CONNECTION_BEING_DRAGGED:
            mouse_position = self.mapToScene(event.pos())
            self._connection_drag.graphics.set_destination(
                mouse_position.x(), mouse_position.y())
            self._connection_drag.graphics.update()

        super().mouseMoveEvent(event)

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

    def _left_mouse_button_press(self, event):

        clicked_item = self._get_clicked_item(event)

        self._last_lmb_click_scene_position = self.mapToScene(event.pos())

        if type(clicked_item) is NodeSocketGraphics:
            if self._current_state == NodeEditorState.VIEW_MODE:
                self._current_state = NodeEditorState.CONNECTION_BEING_DRAGGED
                self._connection_drag_start(clicked_item)
                return

        if self._current_state == NodeEditorState.CONNECTION_BEING_DRAGGED:
            if self._connection_drag_end(clicked_item):
                return

        super().mousePressEvent(event)

    def _right_mouse_button_press(self, event):
        super().mousePressEvent(event)

        item = self._get_clicked_item(event)

        if self.PRINT_DEBUG_INFO:

            if item is None:
                print("[WindowView::_right_mouse_button_press] Scene:")
                for node in self.graphics_scene.scene.nodes:
                    print(f"    [NODE] {node.title} : #{node}")

                for connection in self.graphics_scene.scene.connections:
                    print(f"    [CONNECTION] #{connection}")

            else:
                if isinstance(item, NodeConnectorGraphics):
                    print(f"[WindowView::_right_mouse_button_press] connector {item.connector} "
                          f"{item.connector.start_socket}<->{item.connector.end_socket}")

                elif type(item) is NodeSocketGraphics:
                    print(f"[WindowView::_right_mouse_button_press] socket {item.socket} "
                          f"has connector {item.socket.connector}")

                else:
                    print(f"[WindowView::_right_mouse_button_press] clicked item: {item}")

    def _left_mouse_button_release(self, event):

        clicked_item = self._get_clicked_item(event)

        if self._current_state == NodeEditorState.CONNECTION_BEING_DRAGGED:
            if self._is_distance_between_position_over_threshold(event):
                if self._connection_drag_end(clicked_item):
                    return

        super().mouseReleaseEvent(event)

    def _middle_mouse_button_release(self, event):
        fake_event = QtGui.QMouseEvent(event.type(),
                                       event.localPos(),
                                       event.screenPos(),
                                       QtCore.Qt.LeftButton,
                                       event.buttons() | QtCore.Qt.LeftButton,
                                       event.modifiers())
        super().mouseReleaseEvent(fake_event)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

    def _right_mouse_button_release(self, event):
        super().mouseReleaseEvent(event)

    def _get_clicked_item(self, event):
        position = event.pos()
        object_clicked = self.itemAt(position)
        return object_clicked

    def _is_distance_between_position_over_threshold(self, event):
        new_lmb_release_scene_position = self.mapToScene(event.pos())
        move_distance = new_lmb_release_scene_position - \
                        self._last_lmb_click_scene_position

        distance_vector = move_distance.x() * move_distance.x() + \
                          move_distance.y() * move_distance.y()
        # Calculate threshold by squaring the constant for it. This is done
        # instead of square rooting it as x or y can be 0 and therefore
        # cause an exception.
        threshold_squared = self.CONNECTION_DRAG_START_THRESHOLD * \
                            self.CONNECTION_DRAG_START_THRESHOLD
        return distance_vector > threshold_squared

    def _connection_drag_start(self, item):
        if self.PRINT_DEBUG_INFO: print("[WindowView::_connection_drag_start] Starting to drag connection")
        if self.PRINT_DEBUG_INFO: print(f"[WindowView::_connection_drag_start] Assigning start socket to {item.socket}")

        self._previous_connection = item.socket.connector
        self._last_start_socket = item.socket

        self._connection_drag = NodeConnector(self.graphics_scene.scene,
                                              item.socket,
                                              None,
                                              NodeConnectorType.BEZIER)
        if self.PRINT_DEBUG_INFO: print(f"[WindowView::_connection_drag_start] New drag connection: {self._connection_drag}")

    def _connection_drag_end(self, item) -> bool:
        self._current_state = NodeEditorState.VIEW_MODE

        if type(item) is NodeSocketGraphics:
            if self.PRINT_DEBUG_INFO: print("[WindowView::_connection_drag_end] Assigning end socket")

            if self._previous_connection is not None:
                self._previous_connection.remove()

            if self.PRINT_DEBUG_INFO: print("Previous connection removed...")

            self._connection_drag.start_socket = self._last_start_socket
            self._connection_drag.end_socket = item.socket
            self._connection_drag.start_socket.set_connector(self._connection_drag)
            self._connection_drag.end_socket.set_connector(self._connection_drag)
            if self.PRINT_DEBUG_INFO: print("[WindowView::_connection_drag_end] reassigning start & end socket")
            self._connection_drag.update_positions()
            return True

        if self.PRINT_DEBUG_INFO: print("[WindowView::_connection_drag_end] End dragging connection")
        self._connection_drag.remove()
        self._connection_drag = None
        if self._previous_connection is not None:
            self._previous_connection.start_socket.set_connector(self._previous_connection)
        if self.PRINT_DEBUG_INFO: print("[WindowView::_connection_drag_end] Complete...")

        return False
