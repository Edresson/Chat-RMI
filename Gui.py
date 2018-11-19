# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grupos = QtWidgets.QComboBox(self.centralwidget)
        self.grupos.setGeometry(QtCore.QRect(20, 40, 81, 31))
        self.grupos.setObjectName("grupos")
        self.linesend = QtWidgets.QLineEdit(self.centralwidget)
        self.linesend.setGeometry(QtCore.QRect(110, 230, 421, 25))
        self.linesend.setObjectName("linesend")
        self.sendbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendbtn.setGeometry(QtCore.QRect(290, 280, 80, 25))
        self.sendbtn.setObjectName("sendbtn")
        self.chatlist = QtWidgets.QListWidget(self.centralwidget)
        self.chatlist.setGeometry(QtCore.QRect(110, 40, 421, 161))
        self.chatlist.setObjectName("chatlist")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 17))
        self.label.setObjectName("label")
        self.listconectados = QtWidgets.QListWidget(self.centralwidget)
        self.listconectados.setGeometry(QtCore.QRect(550, 40, 111, 121))
        self.listconectados.setObjectName("listconectados")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 20, 71, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendbtn.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Grupos"))
        self.label_2.setText(_translate("MainWindow", "Conectados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

