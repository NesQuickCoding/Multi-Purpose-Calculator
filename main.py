import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QMainWindow, QStackedWidget
from PyQt5 import QtCore, QtGui
import os

from main_calc.views import MainCalcUI
from main_calc.models import evaluateExpression
from main_calc.controllers import MainCalcCtrl
from prime_gen.views import PrimeGenUI
import prime_gen.models
from temp_conversion.views import temp_Ui
from prime_gen.controllers import PrimeGenCtrl

from ascii_conversion.views import ascii_Ui
from birthday_conversion.views import birthday_Ui


from PyQt5.QtWidgets import QLabel

DROPBOX_MENU = [
    ("ASCII Conversion", ascii_Ui),
    ("Metric Conversion", QLabel),
    ("Temperature Conversion", temp_Ui),
    ("Birthday Conversion", birthday_Ui),
    ("Prime Number Generator/Validator", PrimeGenUI)

]

class SecCalc(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(480, 400)
        self.option = {}
        for QWidgetObject in DROPBOX_MENU:
            self.option[QWidgetObject[1].__name__] = QWidgetObject[1]()
            self.addWidget(self.option[QWidgetObject[1].__name__])
    
    def secCalcDisplay(self, i):
        self.setCurrentIndex(i)

class MultiCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Main Window setup properties
        self.setWindowTitle("Multi-Purpose Calculator")
        self.setFixedSize(960, 400)
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget()
        self._centralWidget = QWidget(self)
        self._centralWidget.setStyleSheet(open('Ext_Stylesheet.css').read())
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create MainCalcUI and secCalc
        self.mainCalc = MainCalcUI(DROPBOX_MENU)
        self.secCalc = SecCalc()
        self.generalLayout.addWidget(self.mainCalc)
        self.generalLayout.addWidget(self.secCalc)

def main():
    multicalc = QApplication(sys.argv)
    view = MultiCalcWindow()
    # Setting application icon
    app_Icon = QtGui.QIcon('graphics/mpc_logo.png')

    view.setWindowIcon(app_Icon)
    view.show()
    # Main Calc Model and Signal Connection
    MainCalcCtrl(model=evaluateExpression, view=view)
    # Prime Gen Model and Signal Connection
    PrimeGenCtrl(model = prime_gen.models, view=view.secCalc.option["PrimeGenUI"])
    # Execute program loop
    sys.exit(multicalc.exec_())

if __name__ == "__main__":
    main()
