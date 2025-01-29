from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tall Box with Outline")

        # Main horizontal layout
        main_layout = QHBoxLayout(self)

        # Tall box layout
        tall_box_layout = QVBoxLayout()
        tall_box_layout.addWidget(QLabel("Item 1"))
        tall_box_layout.addWidget(QLabel("Item 2"))
        tall_box_layout.addWidget(QLabel("Item 3"))
        tall_box_layout.addWidget(QPushButton("Button 1"))
        tall_box_layout.addWidget(QPushButton("Button 2"))

        # Widget for tall box
        tall_box_widget = QWidget()
        tall_box_widget.setLayout(tall_box_layout)

        # Add an outline to the tall box using a stylesheet
        tall_box_widget.setStyleSheet("""
            QWidget {
                border: 2px solid black; /* Thickness and color of the outline */
                border-radius: 5px;     /* Rounded corners */
                padding: 5px;           /* Space between border and content */
            }
        """)

        # Add the tall box to the main layout
        main_layout.addWidget(tall_box_widget)

        # Add other elements to the main layout
        main_layout.addWidget(QPushButton("Other Element 1"))
        main_layout.addWidget(QPushButton("Other Element 2"))

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
