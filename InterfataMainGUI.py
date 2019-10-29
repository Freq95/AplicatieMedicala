# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FromQt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget

import sys
import calendar
import ClasaDB, ClasaPacienti


class MainGui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(850, 510, 81, 101))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel) #|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(330, 60, 471, 481))
        self.calendarWidget.setObjectName("calendarWidget")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(39, 59, 251, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 50, 80))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 45, 161, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 75, 161, 21))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 231, 351))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(850, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 70, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #ARROWS
        prev_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
        next_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")
        prev_button.setIcon(QtGui.QIcon("leftArrow.png"))
        next_button.setIcon(QtGui.QIcon("rightArrow.png"))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aplicatie Medicala"))

        # LABELS
        self.label.setText(_translate("Dialog", "13"))
        self.label_2.setText(_translate("Dialog", "Saturday"))
        self.label_3.setText(_translate("Dialog", "October 2019"))

        # LABELS FONT
        fontDayNumber = QtGui.QFont()
        fontDayNumber.setPointSize(32)
        fontDayNumber.setBold(True)
        fontDayNumber.setWeight(50)

        fontDay = QtGui.QFont()
        fontDay.setPointSize(18)
        fontDay.setBold(True)
        fontDay.setWeight(35)

        fontYear = QtGui.QFont()
        fontYear.setPointSize(10)
        fontYear.setBold(False)
        fontYear.setWeight(20)

        self.label.setFont(fontDayNumber)
        self.label_2.setFont(fontDay)
        self.label_3.setFont(fontYear)

        # BUTTONS
        self.pushButton.setText(_translate("Dialog", "Programare Noua"))
        self.pushButton_2.setText(_translate("Dialog", "Vizualizare"))
        self.pushButton_3.setText(_translate("Dialog", "Pacient Nou"))

        # LIST ITEMS -> make them show current day
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)



        self.listWidget.addItem('Marian Parcalab' + '\n12:00')
        self.listWidget.addItem('Sorin Gheba 13:00')
        self.listWidget.addItem('Cristian Porcaru 14:00')
        self.listWidget.setFont(listFont)

        # /CALENDAR SELECTION
        self.calendarWidget.clicked.connect(self.selectDate)
        # CALENDAR SELECTION/

        # /BUTTON ACTIONS
        self.pushButton_3.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.clicked.connect(self.on_pushButton_clicked2)
        # BUTTON ACTIONS/   


    # DISPLAY THE SELECTED DATE FROM CALENDAR
    def selectDate(self):
        _translate = QtCore.QCoreApplication.translate
        
        date = self.calendarWidget.selectedDate()
        self.fullDate = str(date.day()) + " / " + str(date.month()) + " / " + str(date.year())
        print("full date: %s" % self.fullDate)

        self.label.setText(_translate("Dialog", str(date.day())))
        self.label_2.setText(_translate("Dialog", "Saturday"))
        self.label_3.setText(_translate("Dialog", calendar.month_name[date.month()] + "  "+ str(date.year())))

    # START PACIENT GUI
    def on_pushButton_clicked(self):
        self.Form = QtWidgets.QWidget()
        self.ui = PacientGui()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Dialog.hide()

    def on_pushButton_clicked2(self):
        self.Form = QtWidgets.QWidget()
        self.ui = ProgramatorGui()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Dialog.hide()



class PacientGui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 560)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 240, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 270, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 300, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 330, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 360, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/DentistIcon2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 270, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 330, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 360, 47, 13))
        self.label_6.setObjectName("label_6")


        
        # /BUTTON ACTIONS LINK
        self.AdaugarePacietnBtn = QtWidgets.QPushButton(Form)
        self.AdaugarePacietnBtn.setGeometry(QtCore.QRect(160, 440, 75, 23))
        self.AdaugarePacietnBtn.setObjectName("AdaugarePacietnBtn")

        self.AdaugarePacietnBtn.clicked.connect(self.AdaugarePacietnBtnClicked)
        # BUTTON ACTIONS LINK/
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Prenume"))
        self.label_3.setText(_translate("Form", "Nume"))
        self.label_4.setText(_translate("Form", "Varsta"))
        self.label_5.setText(_translate("Form", "Sex"))
        self.label_6.setText(_translate("Form", "Nothing Yet"))
        self.AdaugarePacietnBtn.setText(_translate("Form", "Adauga Pacient"))

    
    # /BUTTON ACTIONS
    def AdaugarePacietnBtnClicked(self):
        Dialog.show()
        Pacient = ClasaPacienti.Pacient(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        ClasaDB.AdaugarePacientDB(self,Pacient)
        #!!!! GET ALL GUI's OPENED AND CLOSE WHICH ONE YOU LIKE

    # BUTTON ACTIONS/



class ProgramatorGui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 538)
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(30, 410, 115, 31))
        self.timeEdit.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 210, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 240, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 290, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 310, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 330, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 350, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 180, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 210, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 240, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(160, 420, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 40, 111, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/Tooth.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(240, 110, 341, 381))
        self.listWidget.setObjectName("listWidget")



        # /LIST ITEMS -> make them show current day
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)

        self.listWidget.addItem('Marian Parcalab' + '\n12:00')
        self.listWidget.addItem('Sorin Gheba 13:00')
        self.listWidget.addItem('Cristian Porcaru 14:00')
        self.listWidget.setFont(listFont)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget()
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)
        # LIST ITEMS/

        # /BUTTON ACTIONS LINK
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.AdaugarePacietnBtnClicked)
        # BUTTON ACTIONS LINK/

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeEdit.setDisplayFormat(_translate("Form", "hh:mm AP"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Adaugare Programare"))
    
    def AdaugarePacietnBtnClicked(self):
        ###    
        print("")



class CustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomQWidget, self).__init__(parent)
        label = QLabel("Macedon Novi Sad 3 Gratiela A Patra B cea ")
        button = QPushButton("+")
        button.setGeometry(QtCore.QRect(10, 10, 10, 10))
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainGui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())