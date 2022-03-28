import os
import sys, time, random, threading as th
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLabel, QTextEdit, QVBoxLayout, QLineEdit
from PyQt5.QtCore import QCoreApplication
from tkinter import filedialog
from pynput.keyboard import Key, Controller
from pynput import keyboard

class MyApp(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.initUI()


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


        btn_start = QPushButton('start', self)
        btn_start.move(240, 10)
        btn_start.resize(btn_start.sizeHint())
        btn_start.clicked.connect(self.start)


        # Time setting section
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('시간 설정 후 Confirm (기본값 5초) : ')
        self.line = QLineEdit(self)

        self.line.move(240, 45)
        self.line.resize(self.line.sizeHint())
        self.nameLabel.move(20, 50)
        self.nameLabel.resize(self.nameLabel.sizeHint())

        btn_confirm = QPushButton('confirm', self)
        btn_confirm.move(400, 45)
        btn_confirm.resize(btn_confirm.sizeHint())
        btn_confirm.clicked.connect(self.text_changed)


        # 전체적인 창 틀에 관한 설정

        self.setWindowTitle('Test First Application')
        # setWindowTitle - 타이틀바에 나타나는 제목

        # self.move(300, 300)
        # move - 위젯을 스크린의 x, y 의 위치로 이동

        # self.resize(400, 200)
        # resize - 크기를 너비, 높이 조절

        # self.setWindowIcon(QIcon('test.png'))
        # setWindowIcon - 어플리케이션 아이콘을 설정

        self.setGeometry(300, 300, 500, 250)
        # setGeometry - 창의 위치와 크기를 설정 x, y, 너비, 높이

        self.show()
        # show - 위젯을 스크린에 보여줌


    def text_changed(self):
        global connection_time
        connection_time = self.line.text()
        print(connection_time)




    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        if(filename == ''):
            return

        f = open(filename, 'r', encoding="UTF-8")
        global lines
        lines = f.readlines()
        self.statusBar().showMessage('File Connect : ' + filename)

    let_bool = True
    def going_thread(self):
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.esc:
                    global let_bool
                    let_bool = False
                    QCoreApplication.instance().quit()

                elif event.key == keyboard.Key.space:
                    print('pause')
                    os.system("pause")

    def start(self):
        if 'lines' in globals():
            th.Thread(target=self.going_thread, args=(), name='going_thread', daemon=True).start()
            arr_len = len(lines)
            random.shuffle(lines)
            kbController = Controller()
            global let_bool
            let_bool = True
            cnt = 0

            while let_bool:
                time.sleep(1)
                if let_bool is False:
                    break
                if cnt is arr_len - 1:
                    let_bool = False

                data = lines[cnt].split('\n')[0]
                kbController.type(data)
                kbController.press(Key.enter)
                kbController.release(Key.enter)
                cnt += 1
                time.sleep(1)
            QCoreApplication.instance().quit()

        else :
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





