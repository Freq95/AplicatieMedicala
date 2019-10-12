from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    cal = QtWidgets.QCalendarWidget()
    fn = cal.font()
    fn.setPointSize(10)
    cal.setFont(fn)

    cal.setStyleSheet("""
        #qt_calendar_prevmonth, #qt_calendar_nextmonth{
            qproperty-iconSize: 40px
        }
    """
    )
    

    prev_button = cal.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
    next_button = cal.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")

    prev_button.setIcon(QtGui.QIcon("leftArrow.png"))
    next_button.setIcon(QtGui.QIcon("rightArrow.png"))




    cal.resize(280, 450)
    cal.show()
    sys.exit(app.exec_())