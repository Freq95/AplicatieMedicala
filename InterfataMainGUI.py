# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FromQt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox

from shutil import copyfile, copy, copy2
import sys
import os
import datetime

import sys
import calendar
import ClasaDB, ClasaPacienti, ClasaProgramari, ClasaDocuments


class MainGui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        
        
        
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        


        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(850, 510, 81, 101))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel) #|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(330, 60, 471, 481))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setPalette(palette)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(15)
        self.calendarWidget.setFont(font)
        
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
        '''
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(830, 110, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        '''
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 70, 70, 70))
        self.pushButton_3.setObjectName("pushButton_3")        
        self.pushButton_3.setIcon(QtGui.QIcon('icons/add.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(64, 64))


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #ARROWS
        self.calendarWidget.setStyleSheet("""
            #qt_calendar_prevmonth, #qt_calendar_nextmonth{
                qproperty-iconSize: 35px
            }
        """
        ) # 35px is the arrow size

        prev_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
        next_button = self.calendarWidget.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")
        prev_button.setIcon(QtGui.QIcon("leftArrow.png"))
        next_button.setIcon(QtGui.QIcon("rightArrow.png"))
        #/ARROWS

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aplicatie Medicala"))

        # LABELS
        list = ['Luni', 'Marti', 'Miercuri' , 'Joi', 'Vineri', 'Sambata', 'Duminica']
        now = datetime.datetime.now()
        self.label.setText(_translate("Dialog", str(now.day)))
        self.label_2.setText(_translate("Dialog", list[now.weekday()]))
        self.label_3.setText(_translate("Dialog", str(now.month) + ' ' + str(now.year)))

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
        #self.pushButton.setText(_translate("Dialog", "Programare Noua"))
        #self.pushButton_2.setText(_translate("Dialog", "Vizualizare"))
        # self.pushButton_3.setText(_translate("Dialog", "Adauga"))

        

        # /CALENDAR SELECTION
        self.calendarWidget.clicked.connect(self.selectDate)
        # CALENDAR SELECTION/

        # /BUTTON ACTIONS
        self.pushButton_3.clicked.connect(self.on_pushButton_clicked)
        #self.pushButton.clicked.connect(self.on_pushButton_clicked2)
        # BUTTON ACTIONS/   


    # DISPLAY THE SELECTED DATE FROM CALENDAR
    def selectDate(self):

        # LIST ITEMS -> make them show current day
        
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)




        # add to the list all the appointments from that day

        
        '''self.listWidget.addItem('Marian Parcalab' + '\n12:00')
        self.listWidget.addItem('Sorin Gheba 13:00')
        self.listWidget.addItem('Cristian Porcaru 14:00')
        self.listWidget.setFont(listFont) '''


        _translate = QtCore.QCoreApplication.translate
        
        date = self.calendarWidget.selectedDate()
        self.fullDate = str(date.day()) + " / " + str(date.month()) + " / " + str(date.year())
        print("full date: %s" % self.fullDate)

        list = ['Luni', 'Marti', 'Miercuri' , 'Joi', 'Vineri', 'Sambata', 'Duminica']
        currentSelection = date.toPyDate()
        self.label.setText(_translate("Dialog", str(date.day())))
        self.label_2.setText(_translate("Dialog", list[currentSelection.weekday()]))
        self.label_3.setText(_translate("Dialog", calendar.month_name[date.month()] + "  "+ str(date.year())))

        #ClasaDB.CheckAndAddToListCurrentAppointment(self.listWidget, currentSelection)
        ClasaDB.BazaDate.CheckAndAddToListCurrentAppointment(self, self.listWidget, currentSelection)

    # START PACIENT GUI
    def on_pushButton_clicked(self):
        self.Form = QtWidgets.QWidget()
        self.ui = PacientGui()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Dialog.hide()



 

class PacientGui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(480, 790)

        # TABS FONT
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)

        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")

        # TAB WIDGET
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(40, 200, 400, 550))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(64, 64))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        # First TAB
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 160, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")


        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 190, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 220, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 250, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/DentistIcon2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 53, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 160, 47, 13))
        self.label_6.setObjectName("label_6")


        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(140, 190, 47, 13))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(140, 220, 47, 13))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(140, 250, 47, 13))
        self.label_9.setObjectName("label_9")


        
        # /BUTTON ACTIONS LINK
        self.AdaugarePacietnBtn = QtWidgets.QPushButton(self.tab)
        self.AdaugarePacietnBtn.setGeometry(QtCore.QRect(150, 290, 100, 23))
        self.AdaugarePacietnBtn.setObjectName("AdaugarePacietnBtn")

        self.AdaugarePacietnBtn.clicked.connect(lambda: self.AdaugarePacietnBtnClicked(Form))
        # BUTTON ACTIONS LINK/

        self.tabWidget.addTab(self.tab, "")

        # Second TAB
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 150, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(190, 30, 80, 20))
        self.label.setObjectName("label")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(136, 50, 128, 128))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/Tooth.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_5")

        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 230, 350))
        self.listWidget.setObjectName("listWidget")

        # /LIST ITEMS -> make them show current day
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)

        ClasaDB.BazaDate.afisare_pacienti_in_lista(self, self.listWidget)

        ## Campul cautare pacient s-a modificat BIND
        inputNume = self.lineEdit

        self.lineEdit.textChanged.connect(lambda: self.sync_lineEdit(self.listWidget, inputNume))
        ## Campul cautare pacient s-a modificat BIND

        #self.listWidget.addItem('Cristian Porcaru 14:00')
        #self.listWidget.setFont(listFont)

        #item = QListWidgetItem(self.listWidget)
        #item_widget = CustomQWidget()
        #item.setSizeHint(item_widget.sizeHint())
        #self.listWidget.addItem(item)
        #self.listWidget.setItemWidget(item, item_widget)
        # LIST ITEMS/

        # /BUTTON ACTIONS LINK
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 120, 80))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton2.setGeometry(QtCore.QRect(270, 357, 120, 80))
        self.pushButton2.setObjectName("pushButton2")

        # return the selected item
        #selection = self.listWidget.itemSelectionChanged.connect(self.SelectionChanged)

        # should input the selected item
        self.pushButton.clicked.connect(lambda: self.AdaugareProgramareBtnClicked(Form, self.listWidget))
        self.pushButton2.clicked.connect(lambda: self.AdaugareDocumentBtnClicked(self.listWidget))
        
        # BUTTON ACTIONS LINK/
        
        self.tabWidget.addTab(self.tab_2, "")

        # End Third TAB
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Prenume"))
        self.label_3.setText(_translate("Form", "Nume"))
        self.label_4.setText(_translate("Form", "Anul"))
        self.label_5.setText(_translate("Form", "Luna"))
        self.label_6.setText(_translate("Form", "Ziua"))
        self.label_7.setText(_translate("Form", "Telefon"))
        self.label_8.setText(_translate("Form", "CNP"))
        self.label_9.setText(_translate("Form", "Sex"))

        self.pushButton.setText(_translate("Form", "Adauga Programare"))
        self.pushButton2.setText(_translate("Form", "Adauga Document"))
        self.AdaugarePacietnBtn.setText(_translate("Form", "Adauga Pacient"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "PACIENTI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "PROGRAMARI"))

    
    # /BUTTON ACTIONS
    def AdaugarePacietnBtnClicked(self, Form):
        Form.hide()
        Dialog.show()


        Pacient = ClasaPacienti.Pacient(self.lineEdit_11.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text())
        ClasaDB.AdaugarePacientDB(self,Pacient)
        #!!!! GET ALL GUI's OPENED AND CLOSE WHICH ONE YOU LIKE

    def AdaugareProgramareBtnClicked(self, Form, selection): 
        print("Gui Programare")
        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        #print(selection)

        numePacient = selection
        self.Form = QtWidgets.QWidget()
        self.programareUI = ProgramareGUI()

        self.programareUI.setupUi(self.Form, numePacient)
        self.Form.show()
        Form.hide()
        Dialog.hide()


    def AdaugareDocumentBtnClicked(self, selection): 
        print("Gui Documents")
        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        # printeaza numele persoanei selectate
        #print(selection)

        numePacient = selection
        
        #ex = Example()
        #ex.show()

        self.Form = QtWidgets.QWidget()
        self.documentsUI = DocumentsGUI()

        self.documentsUI.setupUi(self.Form, numePacient)

        self.Form.show()
        Dialog.hide()


    # functia care este apelata pentru a face update listei de pacienti
    def sync_lineEdit(self, listWidget, inputNume):
        print("")
        ## Update lista pacienti
        numeCautat = inputNume.text()
        ClasaDB.BazaDate.afisare_pacienti_in_lista_dupa_nume(self, listWidget, numeCautat)

    # BUTTON ACTIONS/



class ProgramareGUI(object):
    def setupUi(self, Form, numeCompletPacient):
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
        
        now = datetime.datetime.now()

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

        self.pushButton_2.clicked.connect(lambda: self.Back)


    def retranslateUi(self, Form, numeCompletPacient):
        _translate = QtCore.QCoreApplication.translate

        numePacient = numeCompletPacient.split(' ')[0]
        prenumePacient = numeCompletPacient.split(' ')[1]

        Form.setWindowTitle(_translate("Form", "Programare"))
        self.groupBox.setTitle(_translate("Form", "Date Pacient"))
        self.label.setText(_translate("Form", numePacient))
        self.label_2.setText(_translate("Form", prenumePacient))
        self.pushButton.setText(_translate("Form", "Adauga Pogramare"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label_3.setText(_translate("Form", "Interventie"))

    def AdaugareProgramarePacientBtnClicked(self, Form, interventie, data, ora):
        print('Adauga Programare Pacient')
        Form.hide()
        Dialog.show()

        nume = self.label.text()
        prenume = self.label_2.text()
        data = data.toPyDate()
        Programare = ClasaProgramari.Programare(interventie, data, ora, prenume, nume)
        ClasaDB.AdaugareProgramareDB(Programare)

    def Back(self):
        print('Back')



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
        button.clicked.connect(self.CustomWidgetBtnCallback)

    def CustomWidgetBtnCallback(self):
        print('12121')



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
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            pacient = self.text()
            path, fileName = os.path.split(filepath)
            path = os.getcwd() # current path
            rootDirectory = path  + "\\DocumentePacienti"
            pacientDirectory  = rootDirectory +  "\\" +  pacient
            copiedFile = pacientDirectory  + "\\" + fileName

            #check if the file format is correct
            if (filepath[-4:].upper() == ".PDF" or filepath[-4:].upper() == ".JPG" or filepath[-4:].upper() == ".PNG" or filepath[-4:].upper() == ".JPEG"):
                
                AdaugaDocumente(filepath, pacient)                    

                (nume, prenume) = pacient.split(maxsplit=1)
                document = copiedFile

                # prenume, nume, document
                Document = ClasaDocuments.Documents(prenume, nume, document)
                ClasaDB.AdaugaDocumentInDB(Document)                        
                
                if os.path.isfile(copiedFile):
                    dialog1 = QMessageBox()
                    #dialog.setIcon(QMessageBox.Question)
                    #QMessageBox.Information
                    dialog1.setWindowTitle("Fisier Valid")
                    dialog1.setText("Fisierul a fost adaugat cu succes.")
                    dialog1.setIcon(QMessageBox.Information)
                    dialog1.exec_()
                else:
                    dialog2 = QMessageBox()
                    #dialog.setIcon(QMessageBox.Question)
                    #QMessageBox.Information
                    dialog2.setWindowTitle("Fisier Invalid")
                    dialog2.setText("Fisierul NU a fost adaugat!")
                    dialog2.setIcon(QMessageBox.Critical)
                    dialog2.exec_()
            else:
                dialog3 = QMessageBox()
                dialog3.setWindowTitle("Fisier Invalid")
                dialog3.setText("Incearca fisiere PDF sau imagini!")
                dialog3.setIcon(QMessageBox.Critical)
                dialog3.exec_()



class DocumentsGUI(object):
    def setupUi(self, Form, numePacient):
        
        Form.setObjectName("Form")
        Form.resize(398, 619)
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
      
        Form.setWindowTitle('Documente')
        button.setGeometry(QtCore.QRect(0, 210, 401, 411))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Documente"))



def AdaugaDocumente(fileSource, numePacient):    
    #TODO
    # # add to Docs Database

    path = os.getcwd() # current path
    rootDirectory = path  + "\\DocumentePacienti"
    pacientDirectory  = rootDirectory +  "\\" +  numePacient
    
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
    copy(fileSource, pacientDirectory)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainGui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())