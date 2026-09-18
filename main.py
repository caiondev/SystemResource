from interface import interface
from utilitys import utils
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from interface.floats.diskFloat import disk_float

def main_window(app):
    window = interface.Interface()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #Chama a função para verificar se o programa está sendo executado como administrador

    if utils.admin_verify():
        main_window(app)
    else:
        print("O programa precisa ser executado como administrador.")
        QtWidgets.QMessageBox.critical(None, "Erro", "O programa precisa ser executado como administrador.")
        sys.exit(1)
