
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Aplicatie Medicala'
        # set app icon    
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/Tooth16.png', QtCore.QSize(16,16))
        app_icon.addFile('icons/Tooth24.png', QtCore.QSize(24,24))
        app_icon.addFile('icons/Tooth32.png', QtCore.QSize(32,32))
        app_icon.addFile('icons/Tooth48.png', QtCore.QSize(48,48))
        app_icon.addFile('icons/Tooth256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)


        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        import sys

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        
        # Create calendar
        self.calendar = QtWidgets.QCalendarWidget()
        self.calendar.move(100, 380)
        self.calendar.resize(280,480)

        fn = self.calendar.font()
        fn.setPointSize(10)
        self.calendar.setFont(fn)

        self.calendar.setStyleSheet("""
            #qt_calendar_prevmonth, #qt_calendar_nextmonth{
                qproperty-iconSize: 40px
            }
        """
        )
        

        prev_button = self.calendar.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
        next_button = self.calendar.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")

        prev_button.setIcon(QtGui.QIcon("leftArrow.png"))
        next_button.setIcon(QtGui.QIcon("rightArrow.png"))

        self.show()
        self.calendar.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())