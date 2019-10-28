from PyQt5 import QtCore, QtGui, QtWidgets

class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton {background-color:#dadada;}")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.ArrowType.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

    @QtCore.pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(QtCore.Qt.ArrowType.DownArrow if not checked else QtCore.Qt.ArrowType.RightArrow)
        self.toggle_animation.setDirection(QtCore.QAbstractAnimation.Forward if not checked else QtCore.QAbstractAnimation.Backward)
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)










if __name__ == '__main__':
    import sys
    import random

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QMainWindow()
    w.setCentralWidget(QtWidgets.QWidget())
    dock = QtWidgets.QDockWidget("Collapsible Demo")
    w.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
    scroll = QtWidgets.QScrollArea()
    dock.setWidget(scroll)
    content = QtWidgets.QWidget()
    content.setStyleSheet("background-color:white")
    scroll.setWidget(content)
    scroll.setWidgetResizable(True)
    vlay = QtWidgets.QVBoxLayout(content)

    towerGeometry = CollapsibleBox("Tower Geometry")

    vlay.addWidget(towerGeometry)
    layoutForTowerGeometry = QtWidgets.QVBoxLayout()
    section = QtWidgets.QPushButton("Sections")


    section.setStyleSheet("background-color: #dadada ;")
    layoutForTowerGeometry.addWidget(section)
    towerGeometry.setContentLayout(layoutForTowerGeometry)


    #Header for Input

    flanges = CollapsibleBox("Flanges")
    layoutForGeometryParameters = QtWidgets.QVBoxLayout()
    geometryParameters = QtWidgets.QPushButton("Geometry Parameters")


    geometryParameters.setStyleSheet("background-color: #dadada ;")
    layoutForGeometryParameters.addWidget(geometryParameters)
    flanges.setContentLayout(layoutForGeometryParameters)



    guidanceInfo = QtWidgets.QPushButton("Guidance Info")


    guidanceInfo.setStyleSheet("background-color: #dadada ;")
    layoutForGeometryParameters.addWidget(guidanceInfo)
    flanges.setContentLayout(layoutForGeometryParameters)
    layoutForTowerGeometry.addWidget(flanges)
    towerGeometry.setContentLayout(layoutForTowerGeometry)

    cans = QtWidgets.QPushButton("Cans")


    cans.setStyleSheet("background-color: #dadada ;")
    layoutForTowerGeometry.addWidget(cans)
    towerGeometry.setContentLayout(layoutForTowerGeometry)

    vlay.addStretch()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())