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
]

class SecCalc(QStackedWidget):
    """
    Secondary calc widget display and handler. Controls which widget to render based 
    on MainCalcUI's combobox current index value.

    Inhereits all methods and attributes from QStackedWidget

    Attributes
    ----------
    option : {"QWidget's Name", QWidget}
        Stores QWidget options for secondary display, including their name and
        reference to their class.
    
    Methods
    -------
    secCalcDisplay(i):
        Sets the index for the corresponding widget to display
    """
    def __init__(self):
        """
        Initializes the widget, and list from DROPBOX_MENU

        Parameters
        ----------
        None

        Returns
        -------
        SecCalc
            Newly constructed widget
        """
        super().__init__()
        self.setFixedSize(425, 400)
        self.option = {}
        for QWidgetObject in DROPBOX_MENU:
            self.option[QWidgetObject[1].__name__] = QWidgetObject[1]()
            self.addWidget(self.option[QWidgetObject[1].__name__])
    
    def secCalcDisplay(self, i):
        """
        Changes which Widget to render

        Parameters
        ----------
        i : int
            index of selected widget

        Returns
        -------
        None
        """
        self.setCurrentIndex(i)

class MultiCalcWindow(QMainWindow):
    """
    Primary Widget for App. Initializes Window and Main and Sec Calc Widgets.
    Loads stylesheet for entire app. 

    Inhereits all methods and attributes from QMainWindow

    Attributes
    ----------
    generalLayout : QHBoxWidget
        stores the layout of the main
    _centralWidget : QWidget
        Contains central widget bound to self
    mainCalc : MainCalcUI
        Main Calc Widget
    secCalc : SecCalc
        Sec Calc Widget
    
    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initilizer for App. Sets window size, title, loads style sheet,
        and initializes Main Calc and Sec Calc widgets

        Parameters
        ----------
        None

        Returns
        -------
        MultiCalcWindow
            Main application
        """
        super().__init__()
        
        # Main Window setup properties
        self.setWindowTitle("Multi-Purpose Calculator")
        self.setFixedSize(850, 400)
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
    """
    Main drivers that initializes PyQt5 application, creates a the calculator,
    as well as controllers for specific widgets.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    multicalc = QApplication(sys.argv)
    # Add font to QFontDatabase
    QtGui.QFontDatabase.addApplicationFont("assets/CascadiaCode.ttf")
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
