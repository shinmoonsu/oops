# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oops.ui',
# licensing of 'oops.ui' applies.
#
# Created: Mon Jan 28 10:40:43 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import os,PySide2,sys,sqlite3,json
from oops import Ui_OopsProject
from openpyxl import load_workbook
from requests import get

from PySide2 import QtCore, QtGui, QtWidgets
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.creater()
        self.download("http://haeam.zz.am/rex.xlsx","rex.xlsx")
        # super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_OopsProject()
        self.ui.setupUi(self)
        
        # msg.setText("This is a message box")
    
    def download(self, url, file_name):
        # open in binary mode
        with open(file_name, "wb") as file:
            # get request
            response = get(url)
            # write to file
            file.write(response.content)
        self.dataProcess("rex.xlsx","")

    def creater(self):
        self.con = sqlite3.connect(':memory:')
        self.con.row_factory = lambda cursor, row: row[0]
        self.cur = self.con.cursor()
        
        query = "CREATE TABLE oops(영업그룹 TEXT,판매처 TEXT,PCODE TEXT,핸드폰번호 TEXT,핸드폰번호2 TEXT,전화번호 TEXT, 전일미수 FLOAT);" # 테이블 생성 쿼리
        self.cur.execute(query)              # 쿼리 실행
        # self.cur.execute("PRAGMA table_info(oops)")
        self.cur.execute("select * from oops")
        # print(self.cur.fetchall())
        

        # print(data)
        # self.con.commit()
        # self.cur.execute("PRAGMA table_info(oops)")

    def realtime(self,text):
        self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%'")
        result = self.cur.fetchall()
        print(result)
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
        self.cur.execute("SELECT 판매처 FROM oops where 판매처 like '%"+text+"%'")
        
        result = self.cur.fetchall()
        # print(result)
        
        for x in result:
            self.ui.listWidget.addItem(x)
        self.ui.listWidget.setCurrentRow(0)
        # print(result)
    
    def loadData(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, '엑셀파일 선택', "*.xlsx")
        self.deataProcess(fname[0], "데이터가 저장되었습니다")
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
            
            # print(angel, type(angel))
            # print("insert into oops values(?,?,?,?,?,?,?)", angel)
            self.cur.execute("insert into oops values(?,?,?,?,?,?,?)", angel)
            
        # x2 = (14)

        # print(angels)
        if message:
            QtWidgets.QMessageBox.about(None, "완료", message)
        # self.cur.execute("SELECT * FROM oops")
        # print(self.cur.fetchall())

    def exit(self):
        self.quit()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    
    sys.exit(app.exec_())
