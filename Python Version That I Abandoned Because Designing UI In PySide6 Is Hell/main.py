import os
import sys
import qdarktheme
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Cosmic Magic")
        
        self.mainLayout = QHBoxLayout(self)
        
        self.secondLayout = QVBoxLayout(self)
        self.filePathWidget = QWidget(self)
        self.filePathWidget.setStyleSheet("""QWidget {
                border: 2px solid black; /* Thickness and color of the outline */
                border-radius: 5px;     /* Rounded corners */
                padding: 5px;           /* Space between border and content */
            }""")
        self.filePathWidget.setLayout(self.secondLayout)

        #self.button.clicked.connect(self.magic)
        for widget in self.mainLayout.children():
            if widget is not self.mainLayout:
                self.mainLayout.setAlignment(widget, QtCore.Qt.AlignmentFlag.AlignTop)
        

    @QtCore.Slot()
    def magic(self):
        print("Wow!")
        
if __name__ == "__main__":
    app = QApplication([])

    window = MyWidget()
    window.setWindowTitle(f"Cosmic Magic - {sys.platform.capitalize()}")
    window.resize(800, 600)
    window.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window.show()

    sys.exit(app.exec())