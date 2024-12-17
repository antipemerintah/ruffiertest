from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from inst import *
from secon_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()# sets what the window will look like
        self.initUI() # creating and configuring graphic elements
        self.connects() # establishes connections between elements
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw=TestWin()
        
app = QApplication([])
app.setStyleSheet("QLabel{font-size: 10pt;}")
mw = MainWin()
app.exec_()