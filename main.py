import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
# test용


class MyApp(QWidget) :

    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :

        # 창 내부에 있는 버튼 관한 설정
    
        btn = QPushButton('Quit', self)
        # 푸시 버튼을 만든다
        # 첫번째 파라미터는 표시될 텍스트, 두번째 파라미터에는 버튼이 위치할 부모 위젯
        btn.move(400, 10)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        # 버튼을 클리하면 clicked시그널이 만들어진다



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





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())





