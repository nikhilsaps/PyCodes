import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a QLabel with the text "Hello, World!"
        hello_label = QLabel('Hello, World!', self)

        # Create a QVBoxLayout to arrange the label vertically
        layout = QVBoxLayout()
        layout.addWidget(hello_label)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Hello World App')
        self.setGeometry(100, 100, 300, 100)  # Set window size (x, y, width, height)

if __name__ == '__main__':
    # Create the application object
    app = QApplication(sys.argv)

    # Create an instance of the HelloWorldApp
    hello_world_app = HelloWorldApp()

    # Show the application window
    hello_world_app.show()

    # Start the application event loop
    sys.exit(app.exec_())
