from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QDate, Qt, QSize

QSS = '''
QCalendarWidget QAbstractItemView
{ 
    selection-background-color: #EE2944; 
    selection-color: yellow;
}
QCalendarWidget QWidget 
{
  color:black;
}
QCalendarWidget QTableView
{
    border-width:0px;
    background-color:white;
}
'''
#white     -> calendar background
#black     -> calendar write
#yellow    -> nothing
#EE2944    -> nothing

class CalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent,
            verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
            gridVisible=False)

        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtCore.Qt.darkGray)
            self.setWeekdayTextFormat(d, fmt)

    def paintCell(self, painter, rect, date):
        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("white")) # current selection background color
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QColor("#EEB5E5")) # current selection circle color
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            painter.setPen(QtGui.QPen(QtGui.QColor("black"))) # current selection calendar number
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))

            painter.restore()
        else:
            super(CalendarWidget, self).paintCell(painter, rect, date)
        
        if date == QDate(2020, 3, 3):
            painter.setBrush(Qt.red)
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 2, 2)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(QSS)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())