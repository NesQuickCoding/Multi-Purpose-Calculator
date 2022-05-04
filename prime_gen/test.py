import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

from views import PrimeGenUI
import models
from controllers import PrimeGenCtrl

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Prime Number Tools")
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.primeGenUI = PrimeGenUI()
        self.generalLayout.addWidget(self.primeGenUI)

def main():
    primegen = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    PrimeGenCtrl(view=view.primeGenUI, model=models)
    sys.exit(primegen.exec())

if __name__ == '__main__':
    main()
