# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\03_Projects\AplicatieMedicala\edit_programare.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class EditProgramare(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 741)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 680, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 680, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(49, 249, 251, 401))
        self.groupBox.setObjectName("groupBox")
        
        
        #self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        #self.dateEdit.setGeometry(QtCore.QRect(80, 320, 110, 22))
        #self.dateEdit.setObjectName("dateEdit")


        now = datetime.datetime.now()
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(80, 320, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")



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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Salveaza"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.groupBox.setTitle(_translate("Form", "Date Pacient"))
        self.radioButton.setText(_translate("Form", "M"))
        self.radioButton_2.setText(_translate("Form", "F"))
        self.label.setText(_translate("Form", "Nume"))
        self.label_2.setText(_translate("Form", "Prenume"))
        self.label_3.setText(_translate("Form", "CNP"))
        self.label_4.setText(_translate("Form", "Sex"))
        self.label_5.setText(_translate("Form", "Telefon"))
        self.label_6.setText(_translate("Form", "Diagnostic"))
        self.label_7.setText(_translate("Form", "Programare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = EditProgramare()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
