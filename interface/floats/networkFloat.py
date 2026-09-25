from PySide6 import QtWidgets, QtCore, QtGui
import sys

def network_float():
    window = QtWidgets.QWidget()
    window.setWindowTitle("Network Management")
    window.setGeometry(100, 100, 400, 300)

    # Create a layout
    layout = QtWidgets.QVBoxLayout()

    # Add a label
    label = QtWidgets.QLabel("Network Management Interface")
    layout.addWidget(label)

    # Add a button
    one_button = QtWidgets.QPushButton("1 Network")
    one_button.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, "Information", "Network management clicked!"))
    layout.addWidget(one_button)

    two_button = QtWidgets.QPushButton("2 Network")
    two_button.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, "Information", "Network management clicked!"))
    layout.addWidget(two_button)

    three_button = QtWidgets.QPushButton("3 Network")
    three_button.clicked.connect(lambda: QtWidgets.QMessageBox.information(window, "Information", "Network management clicked!"))
    layout.addWidget(three_button)    

    # Set the layout to the window
    window.setLayout(layout)

    window.show()