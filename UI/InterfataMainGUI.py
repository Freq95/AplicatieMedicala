# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FromQt.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 650)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(850, 510, 81, 101))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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
        self.pushButton.setText(_translate("Dialog", "2"))
        self.pushButton_2.setText(_translate("Dialog", "3"))
        self.pushButton_3.setText(_translate("Dialog", "1"))

        # LIST ITEMS
        listFont = QtGui.QFont()
        listFont.setPointSize(10)
        listFont.setBold(True)
        listFont.setWeight(35)

        self.listWidget.addItem('Marian Parcalab' + '\n12:00')
        self.listWidget.addItem('Sorin Gheba 13:00')
        self.listWidget.addItem('Cristian Porcaru 14:00')
        self.listWidget.setFont(listFont)


        #self.listWidget.addItem(ls)
        #ls = ['test', 'test2', 'test3']


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Dialog = QtWidgets.QDialog()
#    ui = Ui_Dialog()
#    ui.setupUi(Dialog)
#    Dialog.show()
#    sys.exit(app.exec_())
