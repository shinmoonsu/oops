# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\workspace\python\ui\oops.ui',
# licensing of 'c:\workspace\python\ui\oops.ui' applies.
#
# Created: Fri Jan 25 11:56:19 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_OopsProject(object):
    def setupUi(self, OopsProject):
        OopsProject.setObjectName("OopsProject")
        OopsProject.resize(311, 412)
        self.centralwidget = QtWidgets.QWidget(OopsProject)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(237, 10, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 60, 121, 311))
        self.columnView.setObjectName("columnView")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(140, 60, 161, 311))
        self.columnView_2.setObjectName("columnView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 42, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 71, 20))
        self.label_2.setObjectName("label_2")
        OopsProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OopsProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 21))
        self.menubar.setObjectName("menubar")
        OopsProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OopsProject)
        self.statusbar.setObjectName("statusbar")
        OopsProject.setStatusBar(self.statusbar)

        self.retranslateUi(OopsProject)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged(QString)"), OopsProject.search)
        QtCore.QMetaObject.connectSlotsByName(OopsProject)
        OopsProject.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self, OopsProject):
        OopsProject.setWindowTitle(QtWidgets.QApplication.translate("OopsProject", "OOPS 판매점정보", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("OopsProject", "검색", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("OopsProject", "검색된 판매처", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("OopsProject", "판매처 정보", None, -1))

