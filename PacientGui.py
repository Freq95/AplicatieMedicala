from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QHBoxLayout, QPushButton, QWidget, QMessageBox, QLineEdit, QApplication, QMessageBox, QSizePolicy

import ClasaDB, ClasaPacienti
import ViewPacientGui, ProgramareGui, DocumentGui
from InterfataMainGUI import ShowMainGuiCallback, HideMainGuiCallback

class Pacient(object):
    def setupUi(self, Form, fereastraPrincipala):
        Form.setObjectName("Form")
        Form.resize(350, 480)
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
        Form.setWindowOpacity(1.0)

        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(340, 460))
        self.tabWidget.setMaximumSize(QtCore.QSize(340, 460))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(70, 330, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 240, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 270, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 300, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 330, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(220, 380, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 30, 161, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/DentistIcon2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 360, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 360, 75, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 360, 75, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 40, 131, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(60, 40, 81, 20))
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(40, 80, 256, 261))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # /BUTTON ACTIONS LINK
        #self.AdaugarePacietnBtn = QtWidgets.QPushButton(self.tab)
        #self.AdaugarePacietnBtn.setGeometry(QtCore.QRect(150, 300, 100, 23))
        #self.AdaugarePacietnBtn.setObjectName("AdaugarePacietnBtn")
        self.pushButton.clicked.connect(lambda: self.AdaugarePacientBtnClicked(Form))
        self.listWidget.doubleClicked.connect(lambda: self.ListDoubleClickCallback2())

        ClasaDB.BazaDate.afisare_pacienti_in_lista(self, self.listWidget)

        ## Campul cautare pacient s-a modificat BIND
        inputNume = self.lineEdit_5

        self.lineEdit_5.textChanged.connect(lambda: self.sync_lineEdit(self.listWidget, inputNume))
        # LIST ITEMS/

        # should input the selected item
        self.pushButton.clicked.connect(lambda: self.AdaugarePacientBtnClicked(Form))
        self.pushButton_3.clicked.connect(lambda: self.AdaugareDocumentBtnClicked(self.listWidget))
        self.pushButton_2.clicked.connect(lambda: self.BackToMainGUI(Form, fereastraPrincipala))
        self.pushButton_4.clicked.connect(lambda: self.AdaugareProgramareBtnClicked(Form, self.listWidget))
        
        # BUTTON ACTIONS LINK/
        
        self.tabWidget.addTab(self.tab_2, "")

        # End Third TAB
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aplicatie Medicala"))
        self.label_2.setText(_translate("Form", "Prenume"))
        self.label_3.setText(_translate("Form", "Nume"))
        self.label_4.setText(_translate("Form", "Telefon"))
        self.label_5.setText(_translate("Form", "CNP"))
        self.pushButton.setText(_translate("Form", "+ Pacient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Pacienti"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.pushButton_3.setText(_translate("Form", "Docs"))
        self.pushButton_4.setText(_translate("Form", "Programare"))
        self.label_6.setText(_translate("Form", "Nume Pacient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Programari"))

    def BackToMainGUI(self, Form, fereastraPrincipala):
        print('backToMainGUI')
        Form.deleteLater()
        
        # ShowDialog Callback
        ShowMainGuiCallback()

    def AfisarePacientiClicked(self, Form):
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

    def AdaugarePacientBtnClicked(self, Form):
        Form.hide()
        ShowMainGuiCallback()

        prenume = self.lineEdit.text()
        if(prenume.find(' ') >= 0) or (prenume.find('-') >= 0):
            dialog = QMessageBox()
            dialog.setWindowTitle("Aplicatie Medicala")
            dialog.setText("Va rugam introduceti un singur prenume!")
            dialog.setIcon(QMessageBox.Information)
            dialog.exec_() 
            return None

        nume = self.lineEdit_2.text()
        telefon = self.lineEdit_3.text()
        cnp = self.lineEdit_4.text()

        telefonValid = (len(telefon) == 10 or len(telefon) == 0) and (telefon.isdigit() or len(telefon) == 0)
        cnpValid = (len(cnp) == 13 or len(cnp) == 0) and (cnp.isdigit() or len(cnp) == 0)

        if not (telefonValid or cnpValid):
            dialog = QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("CNP sau Telefon invalid.")
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()   
            return None


        if cnpValid and (len(cnp) != 0):
            an = cnp[1] + cnp[2]
            luna = cnp[3] + cnp[4]
            zi = cnp[5] + cnp[6]
            sex = cnp[0]
            
            if sex == '1' or sex == '5' or sex == '7':
                sexul = 'M'
            elif sex == '2' or sex == '6' or sex == '8':
                sexul = 'F'
            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("Warning")
                dialog.setText("CNP invalid.")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()   
                return None

            if sex == '1' or sex == '2':
                an = '19' + an
            elif sex == '5' or sex == '6':
                an = '20' + an
            elif (sex == '7' or sex == '8') and an > '25':
                an = '19' + an
            else:
                an = '20' + an
        else:
            an = ''
            luna = ''
            zi = ''
            sexul = ''
        
        Pacient = ClasaPacienti.Pacient(prenume, 
                                        nume, 
                                        an, 
                                        luna, 
                                        zi, 
                                        telefon, 
                                        cnp, 
                                        sexul)
                                        
        ClasaDB.AdaugarePacientDB(self,Pacient)

    def AdaugareProgramareBtnClicked(self, Form, selection): 
        print("Gui Programare")
        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        numePacient = selection
        if(numePacient == ''):
            print('Nu ati selectat nici un pacient')
            dialog1 = QMessageBox()
            #dialog.setIcon(QMessageBox.Question)
            #QMessageBox.Information
            dialog1.setWindowTitle("Warning")
            dialog1.setText("Nu ati selectat niciun pacient.")
            dialog1.setIcon(QMessageBox.Warning)
            dialog1.exec_()        
        else:
            self.Form = QtWidgets.QWidget()
            self.programareUI = ProgramareGui.Programare()

            self.programareUI.setupUi(self.Form, numePacient, self)
            self.Form.show()
            Form.hide()
            
    def AdaugareDocumentBtnClicked(self, selection): 
        print("Gui Documents")
        selection = ''
        for item in self.listWidget.selectedItems():
            selection = item.text()

        # printeaza numele persoanei selectate
        #print(selection)

        numePacient = selection
        if(selection == ''):
            print('Nu ati selectat nici un pacient')
            dialog1 = QMessageBox()
            #dialog.setIcon(QMessageBox.Question)
            #QMessageBox.Information
            dialog1.setWindowTitle("Warning")
            dialog1.setText("Nu ati selectat niciun pacient.")
            dialog1.setIcon(QMessageBox.Warning)
            dialog1.exec_()
        else:
            self.Form = QtWidgets.QWidget()
            self.documentsUI = DocumentGui.Document()

            self.documentsUI.setupUi(self.Form, numePacient)

            self.Form.show()
            #HideMainGuiCallback()

    def  ListDoubleClickCallback2(self):
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
    
    # functia care este apelata pentru a face update listei de pacienti
    def sync_lineEdit(self, listWidget, inputNume):
        ## Update lista pacienti
        numeCautat = inputNume.text()
        ClasaDB.BazaDate.afisare_pacienti_in_lista_dupa_nume(self, listWidget, numeCautat)