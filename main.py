import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QMainWindow, QStackedWidget
from PyQt5 import QtGui

from birthday_conversion.views import birthday_Ui
from main_calc.views import MainCalcUI
from main_calc.models import evaluateExpression
from main_calc.controllers import MainCalcCtrl

from prime_gen.views import PrimeGenUI
import prime_gen.models
from prime_gen.controllers import PrimeGenCtrl

from temp_conversion.temp_conv_logic import temp_Ui

from base_conv.views import BaseConvUI
import base_conv.models
from base_conv.controllers import BaseConvCtrl

from metric_conv.views import MetricConvUI
import metric_conv.models
from metric_conv.controllers import MetricConvCtrl

from ascii_conversion.views import ascii_Ui

DROPBOX_MENU = [
    ("ASCII Conversion", ascii_Ui),
    ("Base Conversion", BaseConvUI),
    ("Prime Number Generator/Validator", PrimeGenUI),
    ("Metric Conversion", MetricConvUI),
    ("Temperature Conversion", temp_Ui),
    ("Birthday Conversion", birthday_Ui),
    ("Prime Number Generator/Validator", PrimeGenUI)
]

class SecCalc(QStackedWidget):
    """Initialize the secondary calculator and use a layout manager.
     Set the secondary calc windows(right-side calc) and choose window with a dropdown menu.

    Args:
        QStackedWidget (Widget): layout manager for secondary calc window
    """
    def __init__(self):
        """Initialize all of extra views from the drop down menu.
         These are the extra views shown on the right hand side.
        """
        super().__init__()
        self.setFixedSize(400, 400)
        self.option = {}
        for QWidgetObject in DROPBOX_MENU:
            self.option[QWidgetObject[1].__name__] = QWidgetObject[1]()
            self.addWidget(self.option[QWidgetObject[1].__name__])
    
    def secCalcDisplay(self, i):
        """Set currently displayed view on the right from the drop down menu.

        Args:
            i (int): Index in the dropdown for which view should show on the right.
        """
        self.setCurrentIndex(i)

class MultiCalcWindow(QMainWindow):
    """Create alleither <property name="styleSheet">
       <string notr="true">QPushButton{
    background-color: black;
	color: lime;
    border-style: outset;
    border-width: 1px;
    border-radius: 4px;
    border-color: lime;
}

QPushButton:pressed{
   background-color : green;
}</string>
      </property>

    Args:
        QMainWindow (_type_): _description_
    """
    def __init__(self):
        """Set up properties for the main PyQt5 window.
        """
        super().__init__()
        
        # Main Window setup properties
        self.setWindowTitle("Multi-Purpose Calculator")
        self.setFixedSize(800, 400)
        self.generalLayout = QHBoxLayout()
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

    # Base Conversion Model and Signal Connection
    BaseConvCtrl(model = base_conv.models, view=view.secCalc.option["BaseConvUI"])

    # Metric Conversion Models and Signal Connections
    MetricConvCtrl(view=view.secCalc.option["MetricConvUI"].lengthView, model=metric_conv.models.length_conversion)
    MetricConvCtrl(view=view.secCalc.option["MetricConvUI"].weightView, model=metric_conv.models.weight_conversion)
    MetricConvCtrl(view=view.secCalc.option["MetricConvUI"].timeView, model=metric_conv.models.time_conversion)
    MetricConvCtrl(view=view.secCalc.option["MetricConvUI"].digitalStorageView, model=metric_conv.models.digital_space_conversion)
    
    # Execute program loop
    sys.exit(multicalc.exec_())

if __name__ == "__main__":
    main()
