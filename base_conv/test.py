import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

from views import BaseConvUI
import models
# from controllers import PrimeGenCtrl

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
        
        self.primeGenUI = BaseConvUI()
        self.generalLayout.addWidget(self.primeGenUI)

def main():
    baseconv = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    # PrimeGenCtrl(view=view.primeGenUI, model=models)
    sys.exit(baseconv.exec())

if __name__ == '__main__':
    main()
