from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QPoint, Qt
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy

import sys, datetime, calendar
import ClasaDB, ClasaPacienti, ClasaProgramari, ClasaDocuments
import PacientGui, EditProgramareGui, ViewPacientGui
import cssStyle
import time

class CalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent,
            verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
            gridVisible=False)

    def paintCell(self, painter, rect, date):
        appointmentsList, dateOccurence = ClasaDB.GetAppiontmentsFromDB(self)
        qtDate = []

        for appoint in appointmentsList:
            qtDate.append(QtCore.QDate.fromString(appoint, 'yyyy-MM-dd'))

        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("#141414")) # current selection background color
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QColor("#626262")) # current selection circle color #EEB5E5
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            
            painter.drawEllipse(rect.center() + QPoint(1, 2), 20, 20)
            painter.setPen(QtGui.QPen(QtGui.QColor("#141414"))) # current selection calendar number
            
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))

            painter.restore()
        else:
            super(CalendarWidget, self).paintCell(painter, rect, date)
        
        if date == QDate.currentDate():
            painter.setPen(QtCore.Qt.yellow)
            painter.setOpacity(0.65)
            painter.drawEllipse(rect.center() + QPoint(1, 2), 25, 25)
            painter.setOpacity(1)

        # draw days with appoints
        if qtDate.__contains__(date):
            occurance = dateOccurence[date.toString('yyyy-MM-dd')]
            if occurance > 6:
                painter.setBrush(Qt.red)
                painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)
            elif occurance > 3:
                painter.setBrush(QtGui.QColor("orange"))
                painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)
            elif occurance > 0:
                painter.setBrush(Qt.yellow)
                painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)

class Main(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowOpacity(0.99)
        Dialog.setStyleSheet("")
        Dialog.setStyleSheet(cssStyle.css)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel \n"
"{\n"
"color: rgb(20, 15, 10);  \n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel \n"
"{\n"
"color: rgb(20, 15, 10);  \n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(52, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(52, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 0, 1, 1)
        self.calendarWidget = CalendarWidget()
        #self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setMinimumSize(QtCore.QSize(400, 550))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(52, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 1, 1, 1)

        

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
        self.pushButton.clicked.connect(self.StergeProgramare)
        self.pushButton_2.clicked.connect(self.EditButtonClicked)
        self.pushButton_3.clicked.connect(self.StartPacientiGui)
        self.listWidget.doubleClicked.connect(lambda: self.ListDoubleClickCallback2())
        # BUTTON ACTIONS/ 

        self.pushButton_2.setText(_translate("Form", "Edit"))
        self.pushButton.setText(_translate("Form", "Delete"))
        self.pushButton_3.setText(_translate("Form", "+"))

        Dialog.setWindowTitle(_translate("Dialog", "Aplicatie Medicala"))

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

    def StartPacientiGui(self):
        self.Dialog = QtWidgets.QWidget()
        self.pacientUI = PacientGui.Pacient()
        
        self.pacientUI.setupUi(self.Dialog, self)
        self.Dialog.show()
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
        self.Dialog = QtWidgets.QWidget()
        self.editProgramareUI = EditProgramareGui.EditProgramare()

        #Nume Pacient + ora
        row = self.listWidget.currentRow()

        if(row >= 0):
            item = self.listWidget.item(row)
            numePacientSelectat = str(item.text())

            #Data
            dataProgramare = self.calendarWidget.selectedDate()


            self.editProgramareUI.setupUi(self.Dialog, numePacientSelectat, dataProgramare, self)
            self.Dialog.show()
            Dialog.hide()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Programare pacient")
            dialog.setText("Nu ati selectat nici o programare.")
            dialog.setIcons(QMessageBox.InDialogation)
            dialog.exec_()

    def  ListDoubleClickCallback2(self):
        print('Afisare Pacienti')
        self.Dialog = QtWidgets.QWidget()
        self.viewPacientUI = ViewPacientGui.ViewPacient()

        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        numePacient = selection

        self.viewPacientUI.setupUi(self.Dialog, numePacient, self)
        self.Dialog.setWindowTitle('Aplicatie Medicala')
        self.Dialog.show()

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
