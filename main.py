import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from main_calc.views import MainCalcUI
from main_calc.models import evaluateExpression
from main_calc.controllers import MainCalcCtrl
from prime_gen.views import PrimeGenUI
import prime_gen.models
from prime_gen.controllers import PrimeGenCtrl

__version__ = "0.1"
__author__ = "Python Calcuator"

class SecCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()
        self.primeGenUI = PrimeGenUI()
        layout.addWidget(self.primeGenUI)
        self.setLayout(layout)

class MultiCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Main Window setup properties
        self.setWindowTitle("Multi-Purpose Calculator")
        self.setFixedSize(800, 400)
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.mainCalc = MainCalcUI()
        self.generalLayout.addWidget(self.mainCalc)

        self.secCalc = SecCalc()
        self.generalLayout.addWidget(self.secCalc)
        

def main():
    multicalc = QApplication(sys.argv)
    view = MultiCalcWindow()
    view.show()
    # Main Calc Model and Signal Connection
    MainCalcCtrl(model=evaluateExpression, view=view.mainCalc)
    # Prime Gen Model and Signal Connection
    PrimeGenCtrl(model = prime_gen.models, view=view.secCalc.primeGenUI)
    
    # Execute calculator's main loop
    sys.exit(multicalc.exec_())

if __name__ == "__main__":
    main()
