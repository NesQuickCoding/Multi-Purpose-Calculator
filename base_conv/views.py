from PyQt5.QtWidgets import QWidget, QScrollArea, QLabel, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QRegExp

class NumBase(QWidget):
    def __init__(self):
        super().__init__()

    def _CreateNumHeader(self, headerText):
        header = QLabel(headerText)
        header.setFont(QFont('Arial', 14))
        return header
    
    def _CreateNumTextBox(self):
        textbox = QPlainTextEdit()
        textbox.setFont(QFont('Terminal', 10))
        return textbox

class DecBase(NumBase):
    def __init__(self):
        layout = QVBoxLayout()
        super().__init__()        
        self.decHeader = self._CreateNumHeader("Decimal")
        self.decTextBox = self._CreateNumTextBox()
        layout.addWidget(self.decHeader)
        layout.addWidget(self.decTextBox)
        self.setLayout(layout)

class HexBase(NumBase):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.hexHeader = self._CreateNumHeader("Hexidecimal")
        self.hexTextBox = self._CreateNumTextBox()
        layout.addWidget(self.hexHeader)
        layout.addWidget(self.hexTextBox)
        self.setLayout(layout)        

class BinBase(NumBase):
    def __init__(self):
        super().__init__()  
        layout = QVBoxLayout()
        self.binHeader = self._CreateNumHeader("Binary")
        self.binTextBox = self._CreateNumTextBox()
        layout.addWidget(self.binHeader)
        layout.addWidget(self.binTextBox)
        self.setLayout(layout)      

class BaseConvUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.dec = DecBase()
        layout.addWidget(self.dec)
        self.hex = HexBase()
        layout.addWidget(self.hex)
        self.bin = BinBase()
        layout.addWidget(self.bin)
        self.setLayout(layout)
