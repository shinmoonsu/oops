# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oops.ui',
# licensing of 'oops.ui' applies.
#
# Created: Mon Jan 28 10:10:39 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

import os,PySide2,sys

from PySide2 import QtCore, QtGui, QtWidgets
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

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
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        OopsProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OopsProject)
        self.statusbar.setObjectName("statusbar")
        OopsProject.setStatusBar(self.statusbar)
        self.actionLoad_Data = QtWidgets.QAction(OopsProject)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionExit = QtWidgets.QAction(OopsProject)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionLoad_Data)
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(OopsProject)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged(QString)"), self.search)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered(QAction *)"), self.ex)
        QtCore.QMetaObject.connectSlotsByName(OopsProject)
        OopsProject.setTabOrder(self.lineEdit, self.pushButton)

    def ex(self):
        print("exit clicked")
        # app.exec_()

    def search(self):
        print("ddddddsearch")
        self.model = QtCore.QStringListModel()
        self.model.setStringList(["사랑", "사물", "참사랑", "Good", "Seoul"])
        
        completer = QtWidgets.QCompleter()
        completer.setModel(self.model)
        
        self.lineEdit.setCompleter(completer)
    def retranslateUi(self, OopsProject):
        OopsProject.setWindowTitle(QtWidgets.QApplication.translate("OopsProject", "OOPS 판매점정보", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("OopsProject", "검색", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("OopsProject", "검색된 판매처", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("OopsProject", "판매처 정보", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("OopsProject", "파일", None, -1))
        self.actionLoad_Data.setText(QtWidgets.QApplication.translate("OopsProject", "Load Data", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("OopsProject", "Exit", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OopsProject = QtWidgets.QMainWindow()
    ui = Ui_OopsProject()
    ui.setupUi(OopsProject)
    OopsProject.show()
    sys.exit(app.exec_())

