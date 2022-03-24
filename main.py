import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

from tkinter import *
from tkinter import filedialog

# import tkinter as tk
# import tkinter.filedialog as fd



# class MyApp(QWidget) :
class MyApp(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.initUI()
        global DATA

    def initUI(self) :

        # 하단 툴바 관련 설정
        self.statusBar().showMessage('Ready')

        # clearMessage - 텍스트가 사라짐
        # currentMessage - 현재 상태바에 표시되는 메세지 텍스트를 가져온다
        # QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때 마다 messageChanged 시그널을 발생시킨다.


        # 창 내부에 있는 버튼 관한 설정
    
        btn_quit = QPushButton('Quit', self)
        # 푸시 버튼을 만든다
        # 첫번째 파라미터는 표시될 텍스트, 두번째 파라미터에는 버튼이 위치할 부모 위젯
        btn_quit.move(400, 10)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.clicked.connect(QCoreApplication.instance().quit)
        # 버튼을 클리하면 clicked시그널이 만들어진다

        btn_browser = QPushButton('Browser', self)
        # 파일 가져오는 버튼
        btn_browser.move(320, 10)
        btn_browser.resize(btn_browser.sizeHint())
        btn_browser.clicked.connect(self.browseFiles)



        # 전체적인 창 틀에 관한 설정

        self.setWindowTitle('Test First Application')
        # setWindowTitle - 타이틀바에 나타나는 제목

        # self.move(300, 300)
        # move - 위젯을 스크린의 x, y 의 위치로 이동

        # self.resize(400, 200)
        # resize - 크기를 너비, 높이 조절

        # self.setWindowIcon(QIcon('test.png'))
        # setWindowIcon - 어플리케이션 아이콘을 설정

        self.setGeometry(300, 300, 500, 500)
        # setGeometry - 창의 위치와 크기를 설정 x, y, 너비, 높이

        self.show()
        # show - 위젯을 스크린에 보여줌



    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        print("file name : " + filename)

        f = open(filename, 'r', encoding = "UTF-8")
        lines = f.readlines()
        print(lines)
        for len in lines :
            print(len.split('\n'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





