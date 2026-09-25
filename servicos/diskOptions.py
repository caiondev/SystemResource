import os
import shutil
import subprocess
from PySide6 import QtWidgets, QtGui, QtCore

def cleanup_disk():
    temp = os.environ.get("TEMP")
    tmp = os.environ.get("TMP")

    temp_archives = {temp,tmp}

    erro_encontrado = False

    for directory in temp_archives:
        print(directory)
        for item in os.listdir(directory):
            caminho = os.path.join(directory, item)

            try:
                if os.path.isfile(caminho):
                    os.remove(caminho)

                elif os.path.isdir(caminho):
                    shutil.rmtree(caminho)

            except Exception as erro:
                print("Não foi possível remover:", caminho)
                print(erro)
                erro_encontrado = True
                


    if erro_encontrado == True:
        QtWidgets.QMessageBox.warning(
            None,
            "Limpeza",
            "Limpeza concluída com alguns conflitos."
            )
    else:
        QtWidgets.QMessageBox.information(
            None,
            "Limpeza",
            "Limpeza concluída com sucesso!"
        )


class dks_verify(QtCore.QThread):
    ...

class dsk_correction(QtCore.QThread):
    progress = QtCore.Signal(int)

    def run(self):
        subprocess.Popen(
            [
                "Powershell",
                "-Command",
                "DISM /Online /Cleanup-image /RestoreHealth ; sfc /scannow ; echo S | chkdsk c: /f /r /x"
            ]
        )



dsk_correction = dsk_correction()