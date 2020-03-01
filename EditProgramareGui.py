from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy

import ClasaDB, ClasaPacienti, ClasaProgramari, InterfataMainGUI

class EditProgramare(object):
    def setupUi(self, Form, programarePacient, dataProgramare, fereastraPrincipala):
        Form.setObjectName("Form")
        Form.resize(349, 741)

        # extragem din programare pacient nume si prenume pacient
        vectorProgramarePacient = programarePacient.split()

        prenumePacient = vectorProgramarePacient[0]
        numePacient = vectorProgramarePacient[1]
        oraProgramare = vectorProgramarePacient[2]

        vectorOraProgramare = oraProgramare.split(':')
        ora = int(vectorOraProgramare[0])
        minute = int(vectorOraProgramare[1])
        #secunde = int(vectorOraProgramare[2])

        # cautare in baza de date info despre pacient
        infoPacient = ClasaDB.InfoPacient(self, prenumePacient, numePacient)

        #cautare in baza de date info despre programare
        infoProgramare = ClasaDB.InfoProgramare(self, prenumePacient, numePacient, dataProgramare, oraProgramare)
        

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 680, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 680, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(49, 249, 251, 401))
        self.groupBox.setObjectName("groupBox")

        

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(80, 320, 140, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(dataProgramare), QtCore.QTime(ora, minute)))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateEdit")

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(90, 150, 31, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 150, 31, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 190, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(80, 220, 111, 71))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(16, 50, 51, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(16, 80, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(16, 110, 51, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 51, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 61, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 61, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 80, 41, 61))
        self.label_8.setText("")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setPixmap(QtGui.QPixmap("../icons/Tooth48.png"))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form, infoPacient, infoProgramare, fereastraPrincipala)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, infoPacient, infoProgramare, fereastraPrincipala):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        self.pushButton.setText(_translate("Form", "Salveaza"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.groupBox.setTitle(_translate("Form", "Date Pacient"))
        self.radioButton.setText(_translate("Form", "M"))
        self.radioButton_2.setText(_translate("Form", "F"))

        self.label.setText(_translate("Form", "Nume"))
        self.label_2.setText(_translate("Form", "Prenume"))
        self.label_3.setText(_translate("Form", "CNP"))
        self.label_4.setText(_translate("Form", "Sex"))
        self.label_5.setText(_translate("Form", "Telefon"))
        self.label_6.setText(_translate("Form", "Interventie"))
        self.label_7.setText(_translate("Form", "Programare"))

        for row in infoPacient:
            print('Populam campurile')
            self.lineEdit.setText(_translate("Form", row[2]))
            self.lineEdit_2.setText(_translate("Form", row[1]))
            self.lineEdit_3.setText(_translate("Form", row[7]))
            self.lineEdit_4.setText(_translate("Form", row[6]))

            sexPacient = row[8]
            indexPacient = row[0]

            if(sexPacient == 'M'):
                self.radioButton.setChecked(True)
                self.radioButton_2.setChecked(False)
            else:
                self.radioButton_2.setChecked(True)
                self.radioButton.setChecked(False)

        for row in infoProgramare:
            indexProgramare = row[0]
            self.textEdit.setText(_translate("Form", row[1]))

        self.pushButton.clicked.connect(lambda: self.SalveazaInfoInDB(indexPacient, indexProgramare, fereastraPrincipala, Form))
        self.pushButton_2.clicked.connect(lambda: self.InapoiMeniuPrincipal(fereastraPrincipala, Form))

    def SalveazaInfoInDB(self, indexPacient, indexProgramare, fereastraPrincipala, Form):
        print('Update baza de date')
        sexPacient = self.radioButton.isChecked()

        if sexPacient == True:
            sex = 'M'
        else:
            sex = 'F'
        
        Pacient = ClasaPacienti.Pacient(self.lineEdit_2.text(),
                                        self.lineEdit.text(),
                                        'an',
                                        'luna',
                                        'zi',
                                        self.lineEdit_4.text(),
                                        self.lineEdit_3.text(),
                                        sex)

        Programare = ClasaProgramari.Programare(self.textEdit.toPlainText(),
                                                self.dateTimeEdit.date(),
                                                self.dateTimeEdit.time(),
                                                self.lineEdit_2.text(),
                                                self.lineEdit.text(),                                                
                                                )

        ClasaDB.UpdatePacientiProgramari(self, Pacient, Programare, indexPacient, indexProgramare)

        Form.deleteLater()
        InterfataMainGUI.ShowMainGuiCallback()
    
    def InapoiMeniuPrincipal(self, fereastraPrincipala, Form):
        Form.deleteLater()
        InterfataMainGUI.ShowMainGuiCallback()
