from PySide6 import QtWidgets, QtCore, QtGui
import sys

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Create a central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout
        v_layout = QtWidgets.QVBoxLayout()
        h_layout = QtWidgets.QHBoxLayout()

        # Add a label
        label = QtWidgets.QLabel("Hello, World!")

        # Add a button
        button = QtWidgets.QPushButton("Click Me")
        button.clicked.connect(self.on_button_click)

        # Set the layout to the central widget
        central_widget.setLayout(v_layout)

    def on_button_click(self):
        QtWidgets.QMessageBox.information(self, "Information", "Button clicked!")


    #Application Close Event
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Quit",
            "Are you sure you want to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()