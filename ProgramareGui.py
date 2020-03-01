from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy
from InterfataMainGUI import ShowMainGuiCallback

import datetime
import ClasaProgramari, ClasaDB

class Programare(object):
    def setupUi(self, Form, numeCompletPacient, fereastraPrincipala):
        
        now = datetime.datetime.now()
        
        Form.setObjectName("Form")
        Form.resize(260, 509)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 200, 140))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 53, 13))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 115, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 450, 115, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(20, 340, 118, 22))
        self.timeEdit.setDate(QtCore.QDate(2019, 11, 13))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")

        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(20, 370, 118, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 250, 200, 71))
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.label_3.setObjectName("label")


        self.retranslateUi(Form, numeCompletPacient)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # should input the selected item
        # creare programare noua
        # adaugare programare noua la baza de date

        self.pushButton.clicked.connect(lambda: self.AdaugareProgramarePacientBtnClicked(Form, self.plainTextEdit.toPlainText(), self.dateEdit.date(), self.timeEdit.time()))

        self.pushButton_2.clicked.connect(lambda: self.BackToMainGUI(Form, fereastraPrincipala))

    def retranslateUi(self, Form, numeCompletPacient):
        _translate = QtCore.QCoreApplication.translate

        prenumePacient = numeCompletPacient.split(' ')[0]
        numePacient = numeCompletPacient.split(' ')[1]

        Form.setWindowTitle(_translate("Form", "Programare"))
        self.groupBox.setTitle(_translate("Form", "Date Pacient"))
        self.label.setText(_translate("Form", numePacient))
        self.label_2.setText(_translate("Form", prenumePacient))
        self.pushButton.setText(_translate("Form", "Adauga Pogramare"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label_3.setText(_translate("Form", "Interventie"))
    
    def BackToMainGUI(self, Form, fereastraPrincipala):
        print('backToMainGUI')
        Form.deleteLater()
        ShowMainGuiCallback()

    def AdaugareProgramarePacientBtnClicked(self, Form, interventie, data, ora):
        print('Adauga Programare Pacient')
        Form.hide()
        ShowMainGuiCallback()

        nume = self.label.text()
        prenume = self.label_2.text()
        dataProgramare = data.toPyDate()
        Programare = ClasaProgramari.Programare(interventie, dataProgramare, ora, prenume, nume)

        
        
        # verifica programare
        existaProgramare = ClasaDB.VerificaExistentaProgramare(self, data, ora)
        
        if(existaProgramare):
            dialog = QMessageBox()
            dialog.setWindowTitle("Aplicatie Medicala")
            dialog.setText("Aveti deja o programare la aceasta ora!")
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()
        else:
            ClasaDB.AdaugareProgramareDB(Programare)

    def Back(self):
        print('Back')
