# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspace\oops\oops.ui',
# licensing of 'c:\workspace\oops\oops.ui' applies.
#
# Created: Tue Jan 29 17:50:11 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OopsProject(object):
    def setupUi(self, OopsProject):
        OopsProject.setObjectName("OopsProject")
        OopsProject.resize(259, 409)
        self.centralwidget = QtWidgets.QWidget(OopsProject)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(13, 39, 81, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, 170, 70, 19))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 241, 101))
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 241, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        OopsProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OopsProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        OopsProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OopsProject)
        self.statusbar.setObjectName("statusbar")
        OopsProject.setStatusBar(self.statusbar)
        self.actionLoad_Data = QtWidgets.QAction(OopsProject)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionExit = QtWidgets.QAction(OopsProject)
        self.actionExit.setShortcut("")
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionLoad_Data)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(OopsProject)
        QtCore.QMetaObject.connectSlotsByName(OopsProject)
        OopsProject.setTabOrder(self.lineEdit, self.listWidget)

    def retranslateUi(self, OopsProject):
        OopsProject.setWindowTitle(QtWidgets.QApplication.translate("OopsProject", "OOPS 판매점정보", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("OopsProject", "검색된 판매처", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("OopsProject", "판매처 정보", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("OopsProject", "파일", None, -1))
        self.actionLoad_Data.setText(QtWidgets.QApplication.translate("OopsProject", "판매점 전체 읽어오기", None, -1))
        self.actionLoad_Data.setShortcut(QtWidgets.QApplication.translate("OopsProject", "Ctrl+L", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("OopsProject", "종료", None, -1))

