# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oops.ui',
# licensing of 'oops.ui' applies.
#
# Created: Mon Jan 28 10:40:43 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import os,PySide2,sys,sqlite3,json
import numpy as np
from Ui_oops import Ui_OopsProject
from Ui_environment import Ui_Dialog
from openpyxl import load_workbook

from requests import get

from PySide2 import QtCore, QtGui, QtWidgets
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()        
        self.ui.setupUi(self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OopsProject()
        
        self.ui.setupUi(self)
        self.creater()
        self.download("http://haeam.zz.am/rex.xlsx","rex.xlsx")
        # super(MainWindow, self).__init__(parent=parent)
        
        # self.tableFields = ["검색어","광고진행여부","검색카테고리"]
        # self.ui.tableWidget.setColumnCount(len(self.tableFields))
        # self.ui.tableWidget.setHorizontalHeaderLabels(self.tableFields)
        # self.ui.tableWidget.horizontalHeader().resizeSection(1, 330)
        # self.ui.tableWidget.horizontalHeader().resizeSection(2, 10)
        self.ui.tableWidget.setStyleSheet("font: 12px \"맑은 고딕\";")
        
        # self.ui.tableWidget.setFrameShape(QFrame.StyledPanel)
        # self.ui.tableWidget.setFrameShadow(QFrame.Plain)
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        
        # self.ui.tableWidget.setLineWidth(200)
        # self.ui.tableWidget.setMidLineWidth(0)
        self.ui.tableWidget.setDragEnabled(True)
        self.ui.tableWidget.setAlternatingRowColors(True)
        # self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.tableWidget.setTextElideMode(Qt.ElideRight)
        # self.ui.tableWidget.setShowGrid(True)
        # self.ui.tableWidget.setGridStyle(Qt.CustomDashLine)
        # self.ui.tableWidget.setWordWrap(True)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.statusbar.setStyleSheet("font: 10px \"맑은 고딕\";")
        self.ui.lineEdit.setStyleSheet("weight : bold; font: 14px \"맑은 고딕\";background:#defcbc;")
        # r = self.ui.tableWidget.rowCount()
        # c = self.ui.tableWidget.columnCount()
        # print(r, c)
        title = ['영업그룹','판매처','PCODE','핸드폰번호','핸드폰번호2','전화번호','전일미수','수납가능여부']
        title_count = len(title)
        self.ui.tableWidget.setRowCount(title_count)
        for x in range(title_count):
            self.ui.tableWidget.setRowHeight(x,20)
            self.ui.tableWidget.setColumnWidth(0, 79)
            self.ui.tableWidget.setColumnWidth(1, 170)
            self.ui.tableWidget.setItem( x,0,QTableWidgetItem(title[x]))
        
        QtCore.QObject.connect(self.ui.actionLoad_Data, QtCore.SIGNAL("triggered(bool)"), self.loadData)
        QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("triggered(bool)"), self.close)
        QtCore.QObject.connect(self.ui.action, QtCore.SIGNAL("triggered(bool)"), self.open_environment)
        # QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("textChanged(QString)"), self.realtime)
        QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.search)
        QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.deep_search)
        
        
        # QtCore.QObject.connect(self.ui.actionExit, QtCore.SIGNAL("toggled(bool)"), OopsProject.close)
        # msg.setText("This is a message box")
    
    def download(self, url, file_name):
        self.ui.statusbar.showMessage("데이터를 다운로드 중입니다.")
        # open in binary mode
        with open(file_name, "wb") as file:
            # get request
            response = get(url)
            # write to file
            file.write(response.content)
        self.ui.statusbar.showMessage("원격 데이터가져오기 완료")
        # print("원격 데이터가져오기 완료")
        self.dataProcess("rex.xlsx","")

    def creater(self):
        self.ui.statusbar.showMessage("데이터 구성중입니다.")
        self.con = sqlite3.connect(':memory:')
        # self.con.row_factory = lambda cursor, row: row[0]
        self.cur = self.con.cursor()
        # self.cur.execute("DROP TABLE oops")
        query = "CREATE TABLE oops(영업그룹 TEXT,판매처 TEXT,PCODE TEXT,핸드폰번호 TEXT,핸드폰번호2 TEXT,전화번호 TEXT, 전일미수 INT);" # 테이블 생성 쿼리
        self.cur.execute(query)              # 쿼리 실행
        # self.cur.execute("PRAGMA table_info(oops)")
        self.con.commit()
        

        # print(data)
        # self.con.commit()
        # self.cur.execute("PRAGMA table_info(oops)")

    def realtime(self,text):
        self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%'")
        result = [row[0] for row in self.cur]
            # print (row[0])
        # result = self.cur.fetchall()
        # print(result)
        self.model = QtCore.QStringListModel()
        self.model.setStringList(result)        
        completer = QtWidgets.QCompleter()
        completer.setModel(self.model)
        self.ui.lineEdit.setCompleter(completer)

    def search(self):   

        self.ui.listWidget.clear()
        text = self.ui.lineEdit.text()
        print(text)
        # self.ui.lineEdit.selectAll()
        # print("SELECT * FROM oops where 판매처 like '%"+text+"%'")
        self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%' or PCODE like '%"+text+"%'")
        
        result = [row[0] for row in self.cur]
        # print(result)
        
        for x in result:
            self.ui.listWidget.addItem(x)
        self.ui.listWidget.setCurrentRow(0)
        # print(result)
    
    def deep_search(self):
        판매처 = self.ui.listWidget.currentItem().text()   

        self.cur.execute("SELECT * FROM oops where 판매처='"+판매처+"'")
        x=0
        # print(self.cur.fetchall()[0])
        for row in self.cur.fetchall()[0]:
            # print(x, row)
            xrow = str(row)
            if xrow == "None":
                xrow = ""
            try:
                self.ui.tableWidget.setItem( x,1,QTableWidgetItem(xrow))
            except:
                self.ui.tableWidget.setItem( x,1,QTableWidgetItem(""))
            x=x+1
        if int(xrow) > 0:
            acceptence = "수납불가"
            acceptence_color = QColor(252,0,0)
            acceptence_bcolor = QColor(252,226,254)
        else:
            acceptence = "수납가능"
            acceptence_color = QColor(0,0,0)
            acceptence_bcolor = QColor(224,254,254)
        
        self.ui.tableWidget.setItem( x,1,QTableWidgetItem(acceptence))
        self.ui.tableWidget.item(x,1).setForeground(acceptence_color)
        self.ui.tableWidget.item(x,1).setBackground(acceptence_bcolor)

    def loadData(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, '엑셀파일 선택', "*.xlsx")
        self.dataProcess(fname[0], "데이터가 저장되었습니다")
        print(fname[0])
        
    def dataProcess(self,fname, message):
        angelEx=load_workbook(filename=fname)
        # print(angelEx)
        #불러온 엑셀 파일 중 데이터를 찾을 sheet의 이름을 입력합니다.
        렉스거래처 = angelEx['렉스거래처']
        #Sheet1의 D4의 값을 출력합니다.

        #루프문을 이용해 sheet의 여러 행에 있는 데이터를 불러옵니다.\
        x1 = (3,4,6,14,15,24)
        for i in 렉스거래처.rows:
            # print(len(i),i[1].value,i[10].value,i[15].value)
            angel = []
            for c in x1:
                # print(c)
                a = i[c].value
                angel.append(a)
            angel.append(0)
            
            self.cur.execute("""insert into oops values(?,?,?,?,?,?,?)""", angel)
        
        미수금 = angelEx['Sheet1']
        for i in 미수금.rows:
            # print(i[14].value, i[3].value)
            self.cur.execute("update oops set 전일미수='"+str(i[14].value)+"' where 판매처='"+i[3].value+"'")
        
        self.con.commit()
        # x2 = (14)
        print("데이터 입력완료.")
        # print(angels)
        if message:
            QtWidgets.QMessageBox.about(None, "완료", message)
        # self.cur.execute("""SELECT * FROM oops""")
        # all_rows = self.cur.fetchall()
        # for i in all_rows:
        #     print(i)
    
    def open_environment(self):
        popui = Ui_Dialog()
        popui.setModal(true)   
        # popui.setupUi(self)
        popui.exec()

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    w = MainWindow()
    w.show()
    
    sys.exit(app.exec_())
