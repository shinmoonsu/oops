# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oops.ui',
# licensing of 'oops.ui' applies.
#
# Created: Mon Jan 28 10:40:43 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import os,PySide2,sys,sqlite3,json,shutil
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

class MainWindow2(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow2, self).__init__(parent)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OopsProject()        
        self.ui.setupUi(self)
        self.db = "oops.db"
        self.version = "version"
        self.config = "config"
        # self.creater()
        #환경설정을 읽어온다.
        rt = self.loadEnvironment()
        # print(self.info)
        
        if rt:
            #버전체크를 한다.
            self.versionCheck()

        self.ui.tableWidget.setStyleSheet("font: 12px \"맑은 고딕\";")
        
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.setDragEnabled(True)
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.statusbar.setStyleSheet("font: 10px \"맑은 고딕\";")
        self.ui.lineEdit.setStyleSheet("weight : bold; font: 14px \"맑은 고딕\";background:#defcbc;")

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
    
    #환경설정을 읽어온다.
    def loadEnvironment(self):
        try:
            f = open(self.config, "r")
            fr = f.read()
            self.info = fr.split("\n")
            return True
        except:
            QtWidgets.QMessageBox.warning(None, "데이터 로딩실패", "환경설정 서버경로를 확인하여 주십시오.")

    def versionCheck(self):
        try:
            f = open(self.version, "r")
            local_version = f.read()
            f.close()
        except:
            local_version = "0"
            pass
        try:
            f = open(self.info[0]+"/"+self.version, "r")
            remote_version = f.read()
            f.close()
            print(local_version, remote_version)
            if local_version != remote_version:
                
                shutil.copy(self.info[0]+"/"+self.db, self.db)
                shutil.copy(self.info[0]+"/"+self.version, self.version)
                QtWidgets.QMessageBox.about(None, "데이터갱신", "서버 데이터가 갱신되었습니다")
                #로컬데이터베이스를 연결한다.
            self.loadDb()

        except:
            QtWidgets.QMessageBox.warning(None, "버전체크실패", "서버에 데이터가 없습니다. 서버에 데이터를 업로드해야 합니다.")
            return False

    def realtime(self,text):
        self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%'")
        result = [row[0] for row in self.cur]
        self.model = QtCore.QStringListModel()
        self.model.setStringList(result)        
        completer = QtWidgets.QCompleter()
        completer.setModel(self.model)
        self.ui.lineEdit.setCompleter(completer)

    def search(self):
        try:
            self.versionCheck()
            self.ui.listWidget.clear()
            text = self.ui.lineEdit.text()
            print(text)
            self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%' or PCODE like '%"+text+"%'")
            
            result = [row[0] for row in self.cur]
            # print(result)
            
            for x in result:
                self.ui.listWidget.addItem(x)
            self.ui.listWidget.setCurrentRow(0)
        except:
            pass
    
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
        try:
            ck = self.info[1]
        except:
            pass
        if self.info[1] == "anna":
            fname = QtWidgets.QFileDialog.getOpenFileName(self, '엑셀파일 선택', "*.xlsx")
            print(fname)
            if fname[0]=='':
                return 
        # try:            
        
            self.loadDb()
            print("1")
            self.creater()
            print("2")
            self.excelToData(fname)
            print("3")
            
            shutil.copy(self.db, self.info[0]+"/"+self.db)
            shutil.copy(self.version, self.info[0]+"/"+self.version)
        else:
            QtWidgets.QMessageBox.warning(None, "경고", "관리자만 데이터읽어오기가 가능합니다.")
        # except:
        #     QtWidgets.QMessageBox.warning(None, "경고", "환경설정에서 관리자 비밀번호가 필요합니다.")
    
    def versionUpdate(self):
        try:
            f = open(self.version, "r")
            version = int(f.read())+1
        except:
            version = 1

        f = open(self.version,"w")
        f.write(str(version))

    def excelToData(self, fname):

        angelEx=load_workbook(filename=fname[0])

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
            try:
                money = int(i[14].value)
            except:
                money = 0
            if i[3].value != None:
                print(money, type(money), i[14].value, i[3].value)
                self.cur.execute("update oops set 전일미수='"+str(money)+"' where 판매처='"+i[3].value+"'")
  
        self.con.commit()
        self.versionUpdate()

        QtWidgets.QMessageBox.about(None, "완료", "데이터가 갱신되었습니다.")
            

    def creater(self):
        self.ui.statusbar.showMessage("데이터 구성중입니다.")

        self.cur.execute("DROP TABLE IF EXISTS oops")
        query = "CREATE TABLE oops(영업그룹 TEXT,판매처 TEXT,PCODE TEXT,핸드폰번호 TEXT,핸드폰번호2 TEXT,전화번호 TEXT, 전일미수 INT);" # 테이블 생성 쿼리
        self.cur.execute(query)              # 쿼리 실행
        self.con.commit()

    def loadDb(self):
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()
    
    
    def open_environment(self):
        self.nw = MainWindow2()
        try:
            self.nw.lineEdit.setText(self.info[0])
            self.nw.lineEdit_2.setText(self.info[1])
        except:
            pass
        QtCore.QObject.connect(self.nw.buttonBox, QtCore.SIGNAL("rejected()"), self.nw.close)
        QtCore.QObject.connect(self.nw.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        self.nw.show()
    
    def accept(self):
        src = self.nw.lineEdit.text()
        adminPassword = self.nw.lineEdit_2.text()
        f = open(self.config, "w")
        f.write(src+"\n"+adminPassword)
        self.nw.close()
        self.info = [src, adminPassword]
        self.ui.statusbar.showMessage("환경설정이 저장되었습니다.")
        print(self.info)
        self.versionCheck()


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    w = MainWindow()
    w.show()
    
    sys.exit(app.exec_())
