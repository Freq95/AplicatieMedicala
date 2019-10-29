# TO-DO: make an executable for test --->>> [done once - it works but the code had some errors]
# nu lasa introducerea multipla a aceleiasi persoane
# !!!! repara introducerea de pdf in baza de date - check -  daca e necesar sa-l introduci sau e dee ajuns sa-l salvvezi local in proiect, same shit si cu imaginea + adauga data

import UI.InterfataMainGUI as mainGUI


from tkinter import filedialog
from tkinter import *
import webbrowser as wb

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot








    #gui_IntroducerePacientNou()
    #mainApplication(Pacient)
    #formularPacient()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = mainGUI.MainGUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
