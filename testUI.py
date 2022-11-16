# -*- coding: utf-8 -*-

#Just some UI random junk for practice. Run file for good time.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 651, 411))
        self.photo.setText("")
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.sexyBut = QtWidgets.QPushButton(self.centralwidget)
        self.sexyBut.setGeometry(QtCore.QRect(70, 420, 141, 31))
        self.sexyBut.setObjectName("sexyBut")
        self.momBut = QtWidgets.QPushButton(self.centralwidget)
        self.momBut.setGeometry(QtCore.QRect(410, 420, 171, 31))
        self.momBut.setObjectName("momBut")
        self.scareBut = QtWidgets.QPushButton(self.centralwidget)
        self.scareBut.setGeometry(QtCore.QRect(270, 420, 81, 23))
        self.scareBut.setObjectName("scareBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sexyBut.clicked.connect(self.showSexy)
        self.momBut.clicked.connect(self.showMom)
        self.scareBut.clicked.connect(self.showPopup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sexyBut.setText(_translate("MainWindow", "Click for sexy sexy time"))
        self.momBut.setText(_translate("MainWindow", "click here for a pic of your mom"))
        self.scareBut.setText(_translate("MainWindow", "click for scare"))

    def showSexy(self):
        self.photo.setPixmap(QtGui.QPixmap("qt/sexy.PNG"))
    
    def showMom(self):
        self.photo.setPixmap(QtGui.QPixmap("qt/twoll-kun.PNG"))

    def showPopup(self):
        msg = QMessageBox(MainWindow)
        msg.setWindowTitle("ghost")
        msg.setText("boo!")

        msg.setDetailedText("cummy yummy")

        msg.buttonClicked.connect(self.popupButton)

        x = msg.exec_()

    def popupButton(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
