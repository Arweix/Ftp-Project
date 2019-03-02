# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTP_interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(388, 644)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.grey = QtGui.QLabel(self.centralwidget)
        self.grey.setGeometry(QtCore.QRect(0, -20, 401, 661))
        self.grey.setStyleSheet(_fromUtf8("background-image: url(:/images/background.png);"))
        self.grey.setText(_fromUtf8(""))
        self.grey.setObjectName(_fromUtf8("grey"))
        self.blue = QtGui.QLabel(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(0, 0, 391, 71))
        self.blue.setStyleSheet(_fromUtf8("background-image: url(:/images/top.png);"))
        self.blue.setText(_fromUtf8(""))
        self.blue.setObjectName(_fromUtf8("blue"))
        self.download = QtGui.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(210, 560, 161, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        self.download.setFont(font)
        self.download.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(40, 40, 40);"))
        self.download.setObjectName(_fromUtf8("download"))
        self.up = QtGui.QPushButton(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(20, 560, 161, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.up.setFont(font)
        self.up.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(40, 40, 40);"))
        self.up.setObjectName(_fromUtf8("up"))
        self.ftpserver = QtGui.QTextEdit(self.centralwidget)
        self.ftpserver.setGeometry(QtCore.QRect(20, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ftpserver.setFont(font)
        self.ftpserver.setObjectName(_fromUtf8("ftpserver"))
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(20, 620, 351, 16))
        self.status.setObjectName(_fromUtf8("status"))
        self.con = QtGui.QPushButton(self.centralwidget)
        self.con.setGeometry(QtCore.QRect(240, 5, 131, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        self.con.setFont(font)
        self.con.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(40, 40, 40);\n"
""))
        self.con.setObjectName(_fromUtf8("con"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 70, 391, 481))
        self.treeWidget.setStyleSheet("background-image: url(:/images/background.png);")
        self.treeWidget.setObjectName("allfiles")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.download.setText(_translate("MainWindow", "Download", None))
        self.up.setText(_translate("MainWindow", "Up", None))
        self.con.setText(_translate("MainWindow", "Connect", None))

import resources
