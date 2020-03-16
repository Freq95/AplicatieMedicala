from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QGridLayout, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QBoxLayout

import cssStyle
import ClasaDB, ClasaProgramari, InterfataMainGUI
import pathlib, os, PyPDF2

class ViewPacient(object):
    def setupUi(self, Form, numePacientSelectat, fereastraPrincipala, data = None):
        Form.setObjectName("Form")
        Form.setMinimumSize(QtCore.QSize(735, 510))
        Form.setMaximumSize(QtCore.QSize(748, 510))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        Form.setPalette(palette)
        Form.setStyleSheet(cssStyle.css)
        
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 55, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(175, 175))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Programare2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 4, 1)
        spacerItem5 = QtWidgets.QSpacerItem(37, 183, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 1, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 2, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_9.addWidget(self.tableWidget)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 2, 3, 3, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 200))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem9)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setMinimumSize(QtCore.QSize(200, 200))
        self.label_16.setMaximumSize(QtCore.QSize(200, 200))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("icons/Photo-icon.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 5, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ClasaDB.afisareInfoPacient(self, numePacientSelectat)
        self.listWidget = ClasaDB.BazaDate.UpdateListWithDocuments(self, self.listWidget, numePacientSelectat)
        self.tableWidget = ClasaDB.BazaDate.UpdateTable(self, self.tableWidget, numePacientSelectat)

        self.listWidget.doubleClicked.connect(lambda: self.OpenDocument(numePacientSelectat))
        self.listWidget.itemSelectionChanged.connect(lambda: self.ShowImage(numePacientSelectat))
        self.pushButton_2.clicked.connect(lambda: self.SalveazaNotaDB())
    
    def close(self):
        self.close() 

    def ShowImage(self, numePacientSelectat):
        validImgExtensions = ['.bmp', '.jpg', '.jpeg', '.png']
 
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        numeDocument = str(item.text())
        print('show ' + numeDocument)

        typeOfFile = pathlib.Path(numeDocument).suffix
        typeOfFile = typeOfFile.lower()
        if typeOfFile == ".pdf":
            self.label_16.setPixmap(QtGui.QPixmap("icons/pdfIcon.png"))
        
        elif validImgExtensions.__contains__(typeOfFile):
            prenume =  numePacientSelectat.split(' ')[0]
            nume = numePacientSelectat.split(' ')[1]

            #create path to file
            path = os.getcwd() # current path
            path = path + "\\DocumentePacienti\\" + prenume + '_' + nume + '\\' + numeDocument
            self.label_16.setPixmap(QtGui.QPixmap(path))
        
        else:
            self.label_16.setPixmap(QtGui.QPixmap("icons/file.png"))

    def OpenDocument(self, numePacientSelectat):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        numeDocument = str(item.text())
        print('open ' + numeDocument)

        typeOfFile = pathlib.Path(numeDocument).suffix

        prenume =  numePacientSelectat.split(' ')[0]
        nume = numePacientSelectat.split(' ')[1]

        #create path to file
        path = os.getcwd() # current path
        path = path + "\\DocumentePacienti\\" + prenume + '_' + nume + '\\' + numeDocument

        #dirname = os.path.dirname(__file__)
        #path = dirname + path

        if (typeOfFile == '.pdf'):
            ## deschidere pdf
            objPDF = open(path, 'rb')
            pdf = PyPDF2.PdfFileReader(objPDF)
            print(pdf.numPages)
            os.startfile(path)
        elif (typeOfFile == '.SL'):
            try:
                path = os.getcwd() # current path
                path = path + "\\DocumentePacienti\\" + prenume + '_' + nume + '\\' + '\\CT_' + numeDocument
                os.startfile(path)
            except:
                dialog = QMessageBox()
                dialog.setWindowTitle("Aplicatie Medicala")
                dialog.setText("Fisierul nu poate fi deschis.\nNu s-a gasit metoda de afisare a fisierului.\nExtensia fisierului este: " + typeOfFile + "\nECalea: " + path)
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()
        else:
            try:
                os.startfile(path)
            except:
                dialog = QMessageBox()
                dialog.setWindowTitle("Aplicatie Medicala")
                dialog.setText("Fisierul nu poate fi deschis.\nNu s-a gasit metoda de afisare a fisierului.\nExtensia fisierului este: " + typeOfFile + "\nECalea: " + path)
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()

    def BackToMainGUI(self, Form, fereastraPrincipala):
        Form.deleteLater()
        InterfataMainGUI.ShowMainGuiCallback()

    

    def SalveazaNotaDB(self):
        print("Salveaza in DB")
        # get nume, prenume, data + notaProgramare
        prenume = self.label_15.text()
        nume = self.label_3.text()

        listaData = []
        listaNotaProgramare = []
        listaInterventie = []
        listaOra = []
        columnCount = self.tableWidget.columnCount()
        rowCount = self.tableWidget.rowCount()
        for row in range(rowCount):
            for col in range(columnCount):
                if col == 0:
                    item = self.tableWidget.item(row, col)
                    itemText = item.text()
                    listaData.append(itemText)
                elif col == 3:
                    item = self.tableWidget.item(row, col)
                    itemText = item.text()
                    listaNotaProgramare.append(itemText)
                elif col == 2:
                    item = self.tableWidget.item(row, col)
                    itemText = item.text()
                    listaInterventie.append(itemText)
                elif col == 1:
                    item = self.tableWidget.item(row, col)
                    itemText = item.text()
                    listaOra.append(itemText)


        notaProgramare = ''
        for i in range(listaInterventie.__len__()):
            data = listaData[i]
            notaProgramare = listaNotaProgramare[i]
            interventie = listaInterventie[i]
            ora = listaOra[i]

            Programare = ClasaProgramari.Programare(
                                                    interventie,
                                                    data,
                                                    ora,
                                                    prenume,
                                                    nume,
                                                    notaProgramare
            )
            ClasaDB.updateNotaProgramareDB(self, Programare)

    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aplicatie Medicala"))
        self.label_17.setText(_translate("Form", "Istoric Pacient"))
        
        self.label_3.setText(_translate("Form", "__prenume"))
        
        self.label_11.setText(_translate("Form", "__sex"))
        self.label_13.setText(_translate("Form", "__telefn"))
        self.label_15.setText(_translate("Form", "__nume"))
        self.label_12.setText(_translate("Form", "__cnp"))
        self.label_14.setText(_translate("Form", "__nastere"))

        self.label_2.setText(_translate("Form", "Prenume:"))
        self.label_8.setText(_translate("Form", "Sex:"))
        self.label_6.setText(_translate("Form", "Telefon:"))
        self.label_4.setText(_translate("Form", "Nume:"))
        self.label_7.setText(_translate("Form", "CNP:"))
        self.label_5.setText(_translate("Form", "Data Nasterii:"))

        self.pushButton_2.setText(_translate("Form", "Adauga Nota"))