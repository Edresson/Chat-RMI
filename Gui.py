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
        MainWindow.resize(706, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 691, 371))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.grupos = QtWidgets.QComboBox(self.page)
        self.grupos.setGeometry(QtCore.QRect(560, 320, 101, 41))
        self.grupos.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.grupos.setFont(font)
        self.grupos.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.grupos.setObjectName("grupos")
        self.chatlist = QtWidgets.QListWidget(self.page)
        self.chatlist.setGeometry(QtCore.QRect(160, 70, 391, 231))
        self.chatlist.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"background-color: rgba(85, 170, 255, 100);")
        self.chatlist.setObjectName("chatlist")
        self.listconectados = QtWidgets.QListWidget(self.page)
        self.listconectados.setGeometry(QtCore.QRect(560, 70, 101, 231))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listconectados.setFont(font)
        self.listconectados.setObjectName("listconectados")
        self.linesend = QtWidgets.QLineEdit(self.page)
        self.linesend.setGeometry(QtCore.QRect(160, 320, 301, 41))
        self.linesend.setObjectName("linesend")
        self.sendbtn = QtWidgets.QPushButton(self.page)
        self.sendbtn.setGeometry(QtCore.QRect(470, 320, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sendbtn.setFont(font)
        self.sendbtn.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.sendbtn.setObjectName("sendbtn")
        self.bt_logout = QtWidgets.QPushButton(self.page)
        self.bt_logout.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.bt_logout.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bt_logout.setFont(font)
        self.bt_logout.setStyleSheet("background-color: rgb(192, 193, 255,0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.bt_logout.setObjectName("bt_logout")
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setGeometry(QtCore.QRect(0, 130, 144, 61))
        self.label_15.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_15.setObjectName("label_15")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 144, 361))
        self.label_11.setMaximumSize(QtCore.QSize(144, 400))
        self.label_11.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(140, 10, 531, 361))
        self.label_16.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 214), stop:1 rgba(179, 179, 179, 216));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(50, 92, 128, 228), stop:1 rgba(117, 176, 179, 165));")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 144, 61))
        self.label_17.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_17.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(0, 190, 144, 61))
        self.label_18.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_18.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.label_20.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(0, 250, 144, 61))
        self.label_21.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_21.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(0, 70, 144, 61))
        self.label_19.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.label_19.setObjectName("label_19")
        self.enviararquivo = QtWidgets.QPushButton(self.page)
        self.enviararquivo.setGeometry(QtCore.QRect(0, 250, 141, 61))
        self.enviararquivo.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enviararquivo.setFont(font)
        self.enviararquivo.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-left-color: rgba(255, 255, 255, 0);\n"
"border-top-color: rgba(255, 255, 255, 0);\n"
"gridline-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgba(255, 255, 255, 0);\n"
"border-bottom-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.enviararquivo.setObjectName("enviararquivo")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(160, 70, 391, 231))
        self.label_14.setStyleSheet("background-image: url(:/fundos/whats.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setGeometry(QtCore.QRect(310, -10, 191, 91))
        self.label_23.setStyleSheet("background-image: url(:/fundos/logoanao.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_11.raise_()
        self.label_16.raise_()
        self.label_20.raise_()
        self.label_15.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.grupos.raise_()
        self.listconectados.raise_()
        self.linesend.raise_()
        self.sendbtn.raise_()
        self.bt_logout.raise_()
        self.label_21.raise_()
        self.label_19.raise_()
        self.enviararquivo.raise_()
        self.label_14.raise_()
        self.chatlist.raise_()
        self.label_23.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.RSenha = QtWidgets.QLineEdit(self.page_3)
        self.RSenha.setGeometry(QtCore.QRect(310, 240, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RSenha.setFont(font)
        self.RSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RSenha.setObjectName("RSenha")
        self.Registrar = QtWidgets.QPushButton(self.page_3)
        self.Registrar.setGeometry(QtCore.QRect(310, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Registrar.setFont(font)
        self.Registrar.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.Registrar.setObjectName("Registrar")
        self.confSenha = QtWidgets.QLineEdit(self.page_3)
        self.confSenha.setGeometry(QtCore.QRect(310, 290, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.confSenha.setFont(font)
        self.confSenha.setText("")
        self.confSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confSenha.setObjectName("confSenha")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(280, 170, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.RUsuario = QtWidgets.QLineEdit(self.page_3)
        self.RUsuario.setGeometry(QtCore.QRect(310, 190, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RUsuario.setFont(font)
        self.RUsuario.setText("")
        self.RUsuario.setObjectName("RUsuario")
        self.label_warning_create = QtWidgets.QLabel(self.page_3)
        self.label_warning_create.setGeometry(QtCore.QRect(280, 310, 271, 20))
        self.label_warning_create.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_warning_create.setText("")
        self.label_warning_create.setObjectName("label_warning_create")
        self.bt_voltar = QtWidgets.QPushButton(self.page_3)
        self.bt_voltar.setGeometry(QtCore.QRect(410, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_voltar.setFont(font)
        self.bt_voltar.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"background-color: rgba(255, 0, 0, 100);\n"
"color: rgb(230, 230, 230);")
        self.bt_voltar.setObjectName("bt_voltar")
        self.label_45 = QtWidgets.QLabel(self.page_3)
        self.label_45.setGeometry(QtCore.QRect(0, 10, 144, 61))
        self.label_45.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_45.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.page_3)
        self.label_46.setGeometry(QtCore.QRect(0, 130, 144, 61))
        self.label_46.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_46.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.page_3)
        self.label_47.setGeometry(QtCore.QRect(0, 250, 144, 61))
        self.label_47.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_47.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.page_3)
        self.label_48.setGeometry(QtCore.QRect(0, 190, 144, 61))
        self.label_48.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_48.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.page_3)
        self.label_49.setGeometry(QtCore.QRect(140, 10, 531, 361))
        self.label_49.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(50, 92, 128, 228), stop:1 rgba(117, 176, 179, 165));")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.label_51 = QtWidgets.QLabel(self.page_3)
        self.label_51.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.label_51.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_51.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.label_50 = QtWidgets.QLabel(self.page_3)
        self.label_50.setGeometry(QtCore.QRect(0, 70, 144, 61))
        self.label_50.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_50.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_50.setObjectName("label_50")
        self.label_24 = QtWidgets.QLabel(self.page_3)
        self.label_24.setGeometry(QtCore.QRect(280, 220, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.page_3)
        self.label_25.setGeometry(QtCore.QRect(280, 270, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_3)
        self.label_26.setGeometry(QtCore.QRect(230, 10, 391, 121))
        self.label_26.setStyleSheet("background-image: url(:/fundos/logomenor.png);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.RUsuario_2 = QtWidgets.QLineEdit(self.page_3)
        self.RUsuario_2.setGeometry(QtCore.QRect(310, 150, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RUsuario_2.setFont(font)
        self.RUsuario_2.setText("")
        self.RUsuario_2.setObjectName("RUsuario_2")
        self.label_29 = QtWidgets.QLabel(self.page_3)
        self.label_29.setGeometry(QtCore.QRect(280, 130, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_49.raise_()
        self.label_45.raise_()
        self.label_51.raise_()
        self.label_48.raise_()
        self.label_47.raise_()
        self.label_46.raise_()
        self.RSenha.raise_()
        self.Registrar.raise_()
        self.confSenha.raise_()
        self.label_5.raise_()
        self.RUsuario.raise_()
        self.bt_voltar.raise_()
        self.label_50.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_warning_create.raise_()
        self.RUsuario_2.raise_()
        self.label_29.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_28 = QtWidgets.QLabel(self.page_4)
        self.label_28.setGeometry(QtCore.QRect(0, 0, 671, 361))
        self.label_28.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(50, 92, 128, 228), stop:1 rgba(117, 176, 179, 165));")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.server_edt = QtWidgets.QLineEdit(self.page_4)
        self.server_edt.setGeometry(QtCore.QRect(230, 240, 101, 25))
        self.server_edt.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.server_edt.setFont(font)
        self.server_edt.setStyleSheet("background-color: rgb(204, 204, 153);")
        self.server_edt.setObjectName("server_edt")
        self.label_27 = QtWidgets.QLabel(self.page_4)
        self.label_27.setGeometry(QtCore.QRect(140, 90, 391, 121))
        self.label_27.setStyleSheet("background-image: url(:/fundos/logomenor.png);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label = QtWidgets.QLabel(self.page_4)
        self.label.setGeometry(QtCore.QRect(230, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_4)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 311, 81))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.Conectar = QtWidgets.QPushButton(self.page_4)
        self.Conectar.setGeometry(QtCore.QRect(260, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Conectar.setFont(font)
        self.Conectar.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.Conectar.setObjectName("Conectar")
        self.porta_edt = QtWidgets.QLineEdit(self.page_4)
        self.porta_edt.setGeometry(QtCore.QRect(350, 240, 101, 25))
        self.porta_edt.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.porta_edt.setFont(font)
        self.porta_edt.setStyleSheet("background-color: rgb(204, 204, 153);")
        self.porta_edt.setObjectName("porta_edt")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(260, 20, 331, 301))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:1, stop:0 rgba(50, 92, 128, 255), stop:1 rgba(179, 179, 179, 247));")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(260, 50, 331, 281))
        self.label_7.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 144, 361))
        self.label_8.setMaximumSize(QtCore.QSize(144, 400))
        self.label_8.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(140, 10, 531, 361))
        self.label_9.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(50, 92, 128, 228), stop:1 rgba(117, 176, 179, 165));")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 144, 61))
        self.label_10.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_10.setStyleSheet("background-color: rgba(32, 234, 49, 100);\n"
"color: rgb(230, 230, 230);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(0, 130, 144, 61))
        self.label_12.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(0, 70, 144, 61))
        self.label_13.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_13.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_13.setObjectName("label_13")
        self.label_42 = QtWidgets.QLabel(self.page_2)
        self.label_42.setGeometry(QtCore.QRect(0, 250, 144, 61))
        self.label_42.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_42.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(0, 190, 144, 61))
        self.label_43.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_43.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_2)
        self.label_44.setGeometry(QtCore.QRect(0, 310, 144, 61))
        self.label_44.setMaximumSize(QtCore.QSize(144, 400))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_44.setStyleSheet("background-color: rgb(192, 193, 255);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 140, 221, 89))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Usuario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Usuario.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Usuario.setFont(font)
        self.Usuario.setStyleSheet("background-color: rgb(204, 204, 153);")
        self.Usuario.setObjectName("Usuario")
        self.gridLayout.addWidget(self.Usuario, 0, 0, 1, 1)
        self.Senha = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Senha.setMaximumSize(QtCore.QSize(200, 25))
        self.Senha.setStyleSheet("background-color: rgb(204, 204, 153);")
        self.Senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Senha.setObjectName("Senha")
        self.gridLayout.addWidget(self.Senha, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(320, 230, 90, 25))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(280, 260, 291, 69))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setMaximumSize(QtCore.QSize(191, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_warning = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_warning.setMaximumSize(QtCore.QSize(350, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning.setFont(font)
        self.label_warning.setStyleSheet("color: rgb(255, 1, 1);")
        self.label_warning.setText("")
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_3.addWidget(self.label_warning, 0, 0, 1, 1)
        self.Registrarse = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.Registrarse.setMaximumSize(QtCore.QSize(145, 100))
        self.Registrarse.setObjectName("Registrarse")
        self.gridLayout_3.addWidget(self.Registrarse, 2, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(440, 230, 91, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Login = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.Login.setMaximumSize(QtCore.QSize(80, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 198, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Login.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        font.setItalic(True)
        self.Login.setFont(font)
        self.Login.setStyleSheet("background-color: rgb(28, 198, 25);")
        self.Login.setObjectName("Login")
        self.gridLayout_4.addWidget(self.Login, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(330, 50, 191, 91))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_22.setStyleSheet("background-image: url(:/fundos/logoanao.png);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.gridLayoutWidget_5.raise_()
        self.label_10.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.label_43.raise_()
        self.label_42.raise_()
        self.label_44.raise_()
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendbtn.setText(_translate("MainWindow", "Send"))
        self.bt_logout.setText(_translate("MainWindow", "LogOut"))
        self.label_15.setText(_translate("MainWindow", "      Register"))
        self.label_17.setText(_translate("MainWindow", "        Login"))
        self.label_19.setText(_translate("MainWindow", "       Chat"))
        self.enviararquivo.setText(_translate("MainWindow", "Enviar Arquivo"))
        self.label_14.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/fundos/whats.png\"/></p></body></html>"))
        self.label_23.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/fundos/logochat.png\"/></p></body></html>"))
        self.Registrar.setText(_translate("MainWindow", "Registrar"))
        self.label_5.setText(_translate("MainWindow", "Usuario:"))
        self.bt_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_45.setText(_translate("MainWindow", "        Login"))
        self.label_46.setText(_translate("MainWindow", "    Register"))
        self.label_50.setText(_translate("MainWindow", "        Chat"))
        self.label_24.setText(_translate("MainWindow", "Senha:"))
        self.label_25.setText(_translate("MainWindow", "Confirma:"))
        self.label_26.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/fundos/logochat.png\"/></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "Email:"))
        self.server_edt.setAccessibleDescription(_translate("MainWindow", "User"))
        self.server_edt.setText(_translate("MainWindow", "127.0.0.1"))
        self.server_edt.setPlaceholderText(_translate("MainWindow", "user"))
        self.label_27.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/fundos/logochat.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Escolha o IP e porta do Servidor"))
        self.label_2.setText(_translate("MainWindow", "Seja Bem Vindo "))
        self.Conectar.setText(_translate("MainWindow", "Conectar"))
        self.porta_edt.setAccessibleDescription(_translate("MainWindow", "User"))
        self.porta_edt.setText(_translate("MainWindow", "25500"))
        self.porta_edt.setPlaceholderText(_translate("MainWindow", "user"))
        self.label_4.setText(_translate("MainWindow", "Please login"))
        self.label_10.setText(_translate("MainWindow", "       Login"))
        self.label_12.setText(_translate("MainWindow", "      Register"))
        self.label_13.setText(_translate("MainWindow", "        Chat"))
        self.Usuario.setAccessibleDescription(_translate("MainWindow", "User"))
        self.Usuario.setText(_translate("MainWindow", "user"))
        self.Usuario.setPlaceholderText(_translate("MainWindow", "user"))
        self.Senha.setText(_translate("MainWindow", "user"))
        self.checkBox.setText(_translate("MainWindow", "Remember"))
        self.label_3.setText(_translate("MainWindow", "Não possui conta ?  Registre-se"))
        self.Registrarse.setText(_translate("MainWindow", "Registrar-se "))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.label_22.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/fundos/logochat.png\"/></p></body></html>"))

import background_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

