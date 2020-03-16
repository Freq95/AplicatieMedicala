from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy
from shutil import copy
from PIL import Image

import sys, os, pathlib, PyPDF2, shutil
import ClasaDocuments, ClasaDB
import cssStyle


class Document(object):
    def setupUi(self, Form, numePacient):
        
        Form.setObjectName("Form")
        #Form.resize(400, 620)
        Form.setMinimumSize(QtCore.QSize(400, 620))
        Form.setMaximumSize(QtCore.QSize(400, 620))
        print("Docs  GUI NumePacient = " +  numePacient)
        button = Button(numePacient, Form)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(151, 50, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/drag2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        button.setPalette(palette)
        button.setAutoFillBackground(True)
        button.setCheckable(False)
        button.setAutoDefault(False)
        button.setFlat(True)
      
        Form.setWindowTitle('Aplicatie Medicala')
        Form.setWindowOpacity(0.95)
        Form.setStyleSheet(cssStyle.css)

        button.setGeometry(QtCore.QRect(0, 210, 401, 411))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Documente"))

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.setAcceptDrops(True)
        print('Titlul  =  '+ title)
        #print('Parintele  =  '+ parent)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()

        contorFisiere = 0
        listaFisiere = []

        for i in range(len(urls)):
            
            if urls and urls[i].scheme() == 'file':
                filepath = str(urls[i].path())[1:]
                pacient = self.text()
                path, fileName = os.path.split(filepath)
                (prenume, nume) = pacient.split(maxsplit=1)

                pacientDirectory  = "\\DocumentePacienti\\" +  prenume + "_" + nume
                copiedFile = pacientDirectory  + "\\" + fileName
                
                extension = copiedFile.split('.')
                extension = extension[len(extension) - 1]
                extension = extension.upper()
                
                if extension == "SL":
                    slFile = 1
                #check if the file format is correct
                if (extension == "PDF" or extension == "JPG" or extension == "PNG" or extension == "JPEG" or extension == "BMP" or extension == "SL"):
                    AdaugaDocumente(filepath, pacient, extension, fileName)                    
                    document = copiedFile
                    Document = ClasaDocuments.Documents(prenume, nume, document)
                    ClasaDB.AdaugaDocumentInDB(Document)                        
                    
                    if os.path.isfile(os.getcwd() + copiedFile):
                        contorFisiere = contorFisiere + 1
                    else:
                        listaFisiere.append(fileName)

                else:
                    listaFisiere.append(fileName)
        
        contineSL = 0
        
        for fisiere in listaFisiere:
            extension = fisiere.split('.')
            extension = extension[len(extension) - 1]
            extension = extension.upper()
            if extension == "SL":
                contineSL = 1
        
        if contorFisiere == len(urls) or contineSL == 1:
            dialog1 = QMessageBox()
            dialog1.setWindowTitle("Aplicatie Medicala")
            dialog1.setText("Adaugare cu succes.")
            dialog1.setIcon(QMessageBox.Information)
            dialog1.exec_()
        else:
            mesajFisiere = ''
            for i in range(len(listaFisiere)):
                mesajFisiere = mesajFisiere + '\n' + listaFisiere[i]

            dialog2 = QMessageBox()
            dialog2.setWindowTitle("Aplicatie Medicala")
            dialog2.setText("Urmatoarele fisiere NU respecta formatul:\n" + mesajFisiere)
            dialog2.setIcon(QMessageBox.Critical)
            dialog2.exec_()

def AdaugaDocumente(fileSource, numePacient, extensie, fileName):    
    path = os.getcwd() # current path
    rootDirectory = path  + "\\DocumentePacienti"
    
    prenume = numePacient.split()[0]
    nume = numePacient.split()[1]
    pacientDirectory  = rootDirectory +  "\\" +  prenume + "_" + nume
    
    # check root directory
    if(os.path.isdir(rootDirectory)):
        print('DocumentePacienti Exista')
    else:
        print('DocumentePacienti Nu Exista')
        os.mkdir(rootDirectory)

    
    # check pacient directory
    if(os.path.isdir(pacientDirectory)):
        print('pacientDirectory Exista')
        
    else:
        print('pacientDirectory Nu Exista')
        os.mkdir(pacientDirectory)
    
    # copy the file from source to destination
    if extensie == "SL":
        pacientDirectory = pacientDirectory + "\\CT_" + fileName
        folderExist = os.path.exists(pacientDirectory) 
        if not folderExist:
            copytree(fileSource, pacientDirectory)
        else:
            dialog2 = QMessageBox()
            dialog2.setWindowTitle("Aplicatie Medicala")
            dialog2.setText("Un CT cu acelasi nume exista.\n")
            dialog2.setIcon(QMessageBox.Critical)
            dialog2.exec_()
    else:
        copy(fileSource, pacientDirectory)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)