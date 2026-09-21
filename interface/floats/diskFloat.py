from PySide6 import QtWidgets, QtCore, QtGui
import sys
import os

ac_folder = os.path.dirname(os.path.abspath(__file__))
main_folder = os.path.abspath(os.path.join(ac_folder, '..', '..'))

if main_folder not in sys.path:
    sys.path.append(main_folder)

import servicos

def disk_float():
    window = QtWidgets.QWidget()
    window.setWindowTitle("Disk Management")
    window.setGeometry(100, 100, 400, 300)

    # Create a layout
    layout = QtWidgets.QVBoxLayout()

    # Add a label
    label = QtWidgets.QLabel("Disk Management Interface")
    layout.addWidget(label)

    # Add a button
    optimize_button = QtWidgets.QPushButton("Optimize Disk")
    optimize_button.clicked.connect(servicos.diskOptions.optimize_disk)
    layout.addWidget(optimize_button)

    verify_button = QtWidgets.QPushButton("Verify Disk")
    verify_button.clicked.connect(servicos.diskOptions.verify_disk)
    layout.addWidget(verify_button)

    cleanup_button = QtWidgets.QPushButton("Cleanup Disk")
    cleanup_button.clicked.connect(servicos.diskOptions.cleanup_disk)
    layout.addWidget(cleanup_button)

    # Set the layout to the window
    window.setLayout(layout)

    window.show()
