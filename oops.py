# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oops.ui',
# licensing of 'oops.ui' applies.
#
# Created: Mon Jan 28 17:19:30 2019
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
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 291, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(140, 70, 161, 301))
        self.columnView_2.setObjectName("columnView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 49, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 71, 20))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 121, 301))
        self.listWidget.setObjectName("listWidget")
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
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(OopsProject)
        QtCore.QObject.connect(self.actionLoad_Data, QtCore.SIGNAL("toggled(bool)"), OopsProject.loadData)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("toggled(bool)"), OopsProject.close)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textEdited(QString)"), OopsProject.realtime)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), OopsProject.search)
        QtCore.QMetaObject.connectSlotsByName(OopsProject)
        OopsProject.setTabOrder(self.lineEdit, self.listWidget)
        OopsProject.setTabOrder(self.listWidget, self.columnView_2)

    def retranslateUi(self, OopsProject):
        OopsProject.setWindowTitle(QtWidgets.QApplication.translate("OopsProject", "OOPS 판매점정보", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("OopsProject", "검색된 판매처", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("OopsProject", "판매처 정보", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("OopsProject", "파일", None, -1))
        self.actionLoad_Data.setText(QtWidgets.QApplication.translate("OopsProject", "판매점 전체 읽어오기", None, -1))
        self.actionLoad_Data.setShortcut(QtWidgets.QApplication.translate("OopsProject", "Ctrl+L", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("OopsProject", "종료", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("OopsProject", "Ctrl+Q", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OopsProject = QtWidgets.QMainWindow()
    ui = Ui_OopsProject()
    ui.setupUi(OopsProject)
    OopsProject.show()
    sys.exit(app.exec_())

