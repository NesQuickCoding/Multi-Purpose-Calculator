import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

from views import BaseConvUI
import models
from controllers import BaseConvCtrl

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Base Conversion")
        self.setFixedSize(400, 400)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.baseConvUI = BaseConvUI()
        self.generalLayout.addWidget(self.baseConvUI)

def main():
    baseconv = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    BaseConvCtrl(view=view.baseConvUI, model=models)
    sys.exit(baseconv.exec())

if __name__ == '__main__':
    main()
