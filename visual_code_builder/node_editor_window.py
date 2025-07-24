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
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
from scene import Scene
from node import Node
from node_editor_window_graphics_view import NodeEditorWindowGraphicsView


class NodeEditorWindow(QtWidgets.QWidget):
    """
    A QWidget-based window that sets up a node editor environment using a
    QGraphicsScene and QGraphicsView.

    This window initializes a vertical layout containing a QGraphicsView, which
    displays a custom QGraphicsScene for visual node editing. It is designed to
    act as the main GUI component for a node-based editor.
    """

    def __init__(self, parent=None):
        """
        Initialize the NodeEditorWindow.

        :param parent: Optional QWidget parent. Defaults to None.
        """
        super().__init__(parent)

        self.layout: typing.Optional[QtWidgets.QVBoxLayout] = None
        self.view: typing.Optional[QtWidgets.QGraphicsView] = None
        self.scene: typing.Optional[Scene] = None

        self._stylesheet_filename = "stylesheets/node_style.qss"
        self._load_style_sheet(self._stylesheet_filename)

        self.init()

    def init(self):
        """
        Set up the UI components for the node editor window.

        This includes setting the window geometry, creating the layout,
        initializing the QGraphicsScene and QGraphicsView, and adding them to
        the layout.
        """
        # x offset, y offset, width, height
        self.setGeometry(200, 200, 1024, 768)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create graphics scene
        self.scene = Scene()

        node_1 = Node(self.scene, "Node #1")

        # Create graphics view
        self.view = NodeEditorWindowGraphicsView(self.scene.graphics_scene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

        # self.add_test_contents()

    def add_test_contents(self):
        green_brush = QtGui.QBrush(QtCore.Qt.GlobalColor.green)
        outline_pen = QtGui.QPen(QtCore.Qt.GlobalColor.black)
        outline_pen.setWidth(2)

        rect = self.graphics_scene.addRect(-100, -100, 80, 100, outline_pen, green_brush)
        rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

        text = self.graphics_scene.addText("Movable tests string", QtGui.QFont("Ubuntu"))
        text.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        text.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QtGui.QColor.fromRgbF(1.0, 1.0, 1.0))

        widget_1 = QtWidgets.QPushButton("Push me")
        proxy_1 = self.graphics_scene.addWidget(widget_1)
        proxy_1.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        proxy_1.setPos(0, 30)

        widget_2 = QtWidgets.QTextEdit()
        proxy_2 = self.graphics_scene.addWidget(widget_2)
        proxy_2.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        proxy_2.setPos(-400, -400)

        line = self.graphics_scene.addLine(-200, -200, 400, -100, outline_pen)
        line.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

    def _load_style_sheet(self, stylesheet_file: str):
        print(f"Loading node stylesheet '{stylesheet_file}")
        file: QtCore.QFile = QtCore.QFile(stylesheet_file)
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stylesheet = file.readAll()
        QtWidgets.QApplication.instance().setStyleSheet(str(stylesheet,
                                                            encoding="utf-8"))
