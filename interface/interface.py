from PySide6 import QtWidgets, QtCore, QtGui
import sys
from interface.floats.diskFloat import disk_float

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Resource Management")
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
        label = QtWidgets.QLabel("System Resource Management Interface")

        # Add a button
        disk_button = QtWidgets.QPushButton("Disk Options")
        disk_button.clicked.connect(disk_float) #chama a janela

        # Set the layout to the central widget
        central_widget.setLayout(v_layout)

        #add a label and button to the layout
        h_layout.addWidget(label)
        h_layout.addWidget(disk_button)
        v_layout.addLayout(h_layout)
        v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

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

    