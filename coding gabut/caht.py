import sys

import openai

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class EnglishChat(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        
        hb = QHBoxLayout()
        vb.addLayout(hb)
        
        hb1 = QHBoxLayout()
        vb.addLayout(hb1)
        
        vb1 = QVBoxLayout()
        hb1.addLayout(vb1)
        
        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)
        hb1.addWidget(self.splitter)
        
        self.vsplitter1 = QSplitter()
        self.vsplitter1.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.vsplitter1)
        
        self.vsplitter2 = QSplitter()
        self.vsplitter2.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.vsplitter2)
        
        self.prompt_box = QTextEdit()
        self.vsplitter1.addWidget(self.prompt_box)
        
        self.response_box = QTextBrowser()
        self.vsplitter2.addWidget(self.response_box)
        
    def main():
        app = QApplication(sys.argv)
        gui = EnglishChat()
        gui.show
        app.exec()
        
    if __name__ == '__main__':
        main()        
        