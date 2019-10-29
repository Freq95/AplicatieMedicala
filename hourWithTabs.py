# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\03_Projects\AplicatieMedicala\UI\oraUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(350, 680)
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
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(40, 200, 269, 450))
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
        
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
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
        self.label_2.setGeometry(QtCore.QRect(140, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 270, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(140, 330, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 360, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(140, 390, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(140, 420, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(140, 450, 47, 13))
        self.label_9.setObjectName("label_9")

        # /BUTTON ACTIONS LINK
        self.AdaugarePacietnBtn = QtWidgets.QPushButton(self.tab)
        self.AdaugarePacietnBtn.setGeometry(QtCore.QRect(150, 300, 100, 23))
        self.AdaugarePacietnBtn.setObjectName("AdaugarePacietnBtn")
        self.AdaugarePacietnBtn.clicked.connect(self.AdaugarePacietnBtnClicked)
        self.tabWidget.addTab(self.tab, "")

        # Second TAB
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 121, 22))
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setObjectName("comboBox")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit.setGeometry(QtCore.QRect(60, 18, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setProperty("showGroupSeparator", True)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.tabWidget.addTab(self.tab_2, "")

        #Third TAB
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tabWidget, self.lineEdit)
        Form.setTabOrder(self.lineEdit, self.timeEdit)
        Form.setTabOrder(self.timeEdit, self.comboBox)

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "PACIENTI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "PROGRAMARI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "DOCUMENTE"))
        self.AdaugarePacietnBtn.setText(_translate("Form", "Adauga Pacient"))
    # /BUTTON ACTIONS
    def AdaugarePacietnBtnClicked(self):
        print("Buton Apasat")
        #Dialog.show()
        #Pacient = ClasaPacienti.Pacient(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(), self.lineEdit_8.text())
        #ClasaDB.AdaugarePacientDB(self,Pacient)
        #!!!! GET ALL GUI's OPENED AND CLOSE WHICH ONE YOU LIKE

    # BUTTON ACTIONS/

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
