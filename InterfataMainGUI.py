# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'D:\03_Projects\AplicatieMedicala\test22.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy

import sys, datetime, calendar
import ClasaDB, ClasaPacienti, ClasaProgramari, ClasaDocuments
import PacientGui, EditProgramareGui, ViewPacientGui

class Main(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(950, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)  
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        
        Dialog.setPalette(palette)
        
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.listWidget.setMaximumSize(QtCore.QSize(280, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(400, 463))
        self.calendarWidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_3.addWidget(self.calendarWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_3.setIcon(QtGui.QIcon('icons/add.png'))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setIcon(QtGui.QIcon('icons/edit5.png'))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setIcon(QtGui.QIcon('icons/delete2.png'))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 4, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 4, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Calendar Arrow Customization
        self.calendarWidget.setStyleSheet("""
            #qt_calendar_prevmonth, #qt_calendar_nextmonth{
                qproperty-iconSize: 35px
            }
        """
        ) # 35px is the arrow size

        prev_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
        next_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")
        prev_button.setIcon(QtGui.QIcon("icons/leftArrow.png"))
        next_button.setIcon(QtGui.QIcon("icons/rightArrow.png"))
        #/Calendar Arrow Customization

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        # LABELS
        listZileSaptamana = ['Luni', 'Marti', 'Miercuri' , 'Joi', 'Vineri', 'Sambata', 'Duminica']
        listLuni = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie']
        
        now = datetime.datetime.now()
        
        self.label.setText(_translate("Dialog", str(now.day)))
        self.label_2.setText(_translate("Dialog", listZileSaptamana[now.weekday()]))
        self.label_3.setText(_translate("Dialog", listLuni[now.month - 1] + ' ' + str(now.year)))
        
        date = self.calendarWidget.selectedDate()
        currentSelection = date.toPyDate()
        self.listWidget = ClasaDB.BazaDate.CheckAndAddToListCurrentAppointment(self, self.listWidget, currentSelection)

        # /CALENDAR SELECTION
        self.calendarWidget.clicked.connect(self.SelectDate)
        # CALENDAR SELECTION/

        # /BUTTON ACTIONS
        self.pushButton.clicked.connect(self.EditButtonClicked)
        self.pushButton_2.clicked.connect(self.StergeProgramare)
        self.pushButton_3.clicked.connect(self.StartPacientiGui)
        self.listWidget.doubleClicked.connect(lambda: self.ListDoubleClickCallback2())
        # BUTTON ACTIONS/ 

        Dialog.setWindowTitle(_translate("Dialog", "Aplicatie Medicala"))
        #self.label_3.setText(_translate("Dialog", "februarie 2020"))
        #self.label_2.setText(_translate("Dialog", "sambata"))
        
        #self.label.setText(_translate("Dialog", "25"))
        
        

# DISPLAY THE SELECTED DATE FROM CALENDAR
    def SelectDate(self):

        # LIST ITEMS -> make them show current day
        
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)


        _translate = QtCore.QCoreApplication.translate
        
        date = self.calendarWidget.selectedDate()
        self.fullDate = str(date.day()) + " / " + str(date.month()) + " / " + str(date.year())
        print("full date: %s" % self.fullDate)

        list = ['Luni', 'Marti', 'Miercuri' , 'Joi', 'Vineri', 'Sambata', 'Duminica']
        currentSelection = date.toPyDate()
        self.label.setText(_translate("Dialog", str(date.day())))
        self.label_2.setText(_translate("Dialog", list[currentSelection.weekday()]))
        self.label_3.setText(_translate("Dialog", calendar.month_name[date.month()] + "  "+ str(date.year())))


        self.listWidget = ClasaDB.BazaDate.CheckAndAddToListCurrentAppointment(self, self.listWidget, currentSelection)
        
        #self.pushButton_6.clicked.connect(lambda: self.ListDoubleClickCallback2())

    def StartPacientiGui(self):
        self.Form = QtWidgets.QWidget()
        self.pacientUI = PacientGui.Pacient()
        
        self.pacientUI.setupUi(self.Form, self)
        self.Form.show()
        Dialog.hide()

    def StergeProgramare(self):
        #verifica sa fie selectat un element din lista -> confirma stergerea
        row = self.listWidget.currentRow()

        if(row >= 0):
            item = self.listWidget.item(row)
            numePacientSelectat = str(item.text())

            vectorProgramarePacient = numePacientSelectat.split()

            prenumePacient = vectorProgramarePacient[0]
            numePacient = vectorProgramarePacient[1]
            oraProgramare = vectorProgramarePacient[2]
            
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Aplicatie Medicala')
            box.setText("Sunteti sigur ca doriti sa stergeti programarea pentru, " + prenumePacient + ' ' + numePacient + ' de la ora: ' + oraProgramare + '?')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            box.setDefaultButton(QMessageBox.No)
            buttonYes = box.button(QMessageBox.Yes)
            box.exec()


            if(box.clickedButton() == buttonYes):
                # apelare stergere
                dataProgramare = self.calendarWidget.selectedDate()
                infoProgramare = ClasaDB.InfoProgramare(self, prenumePacient, numePacient, dataProgramare, oraProgramare)
                indexProgramare = ClasaDB.IndexProgramare(self, infoProgramare)
                ClasaDB.StergeProgramare(self, indexProgramare)

                date = self.calendarWidget.selectedDate()
                currentSelection = date.toPyDate()
                self.listWidget = ClasaDB.BazaDate.CheckAndAddToListCurrentAppointment(self, self.listWidget, currentSelection)
            else:
                print('Revenire Meniu Principal')
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("Nu ati selectat niciun pacient.")
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()  

        #update lista 

    def EditButtonClicked(self):
        self.Form = QtWidgets.QWidget()
        self.editProgramareUI = EditProgramareGui.EditProgramare()

        #Nume Pacient + ora
        row = self.listWidget.currentRow()

        if(row >= 0):
            item = self.listWidget.item(row)
            numePacientSelectat = str(item.text())

            #Data
            dataProgramare = self.calendarWidget.selectedDate()


            self.editProgramareUI.setupUi(self.Form, numePacientSelectat, dataProgramare, self)
            self.Form.show()
            Dialog.hide()
        else:
            dialog = QMessageBox()
            #dialog.setIcon(QMessageBox.Question)
            #QMessageBox.Information
            dialog.setWindowTitle("Programare pacient")
            dialog.setText("Nu ati selectat nici o programare.")
            dialog.setIcon(QMessageBox.Information)
            dialog.exec_()

    def  ListDoubleClickCallback2(self):
        '''print('2-1')
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        
        if item != None:
            numePacientSelectat = str(item.text())
            self.Form = QtWidgets.QWidget()
            self.viewPacientUI = ViewPacientGui.ViewPacient()
            dataProgramare = self.calendarWidget.selectedDate()
            self.viewPacientUI.setupUi(self.Form, numePacientSelectat, self, dataProgramare)
            self.Form.setWindowTitle('Aplicatie Medicala')
            self.Form.show()
            Dialog.hide()'''
        print('Afisare Pacienti')
        self.Form = QtWidgets.QWidget()
        self.viewPacientUI = ViewPacientGui.ViewPacient()

        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        numePacient = selection

        self.viewPacientUI.setupUi(self.Form, numePacient, self)
        self.Form.setWindowTitle('Aplicatie Medicala')
        self.Form.show()

def ShowMainGuiCallback():
    Dialog.show()

def HideMainGuiCallback():
    Dialog.hide()


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icons/Tooth256.png'))

# print existing gui styles and set it to FUSION
print(QtWidgets.QStyleFactory.keys())
app.setStyle('Fusion')

Dialog = QtWidgets.QWidget()

# creaza bazele de date daca acestea nu exista
databaseInit = ClasaDB.BazaDate()
databaseInit.create_table()

ui = Main()
ui.setupUi(Dialog)

if __name__ == "__main__":
    Dialog.show()
    sys.exit(app.exec_())
