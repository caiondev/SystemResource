from PySide6 import QtWidgets, QtCore, QtGui
import sys

def performance_float():
    window = QtWidgets.QWidget()
    window.setWindowTitle("Performance Management")
    window.setGeometry(100, 100, 400, 300)

    # Create a layout
    layout = QtWidgets.QVBoxLayout()

    # Add a label
    label = QtWidgets.QLabel("Performance Management Interface")
    layout.addWidget(label)

    # Add a button
    button = QtWidgets.QPushButton("Manage Performance")
    button.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, "Information", "Performance management clicked!"))
    layout.addWidget(button)

    # Set the layout to the window
    window.setLayout(layout)

    window.show()