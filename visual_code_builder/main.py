import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("Test Label")
    label.show()


    sys.exit(app.exec())
