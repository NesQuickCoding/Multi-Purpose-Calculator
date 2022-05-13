import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

from views import MetricConvUI
import models
from controllers import MetricConvCtrl

class TestWindow(QMainWindow):
    """
    Constructs a QMainWindow to create and append to it's window a MetricConvUI
    widget for testing purposes

    Inherits all methods and attributes from QMainWindow

    Attributes
    ----------
    generalLayout : QVBoxLayout
        stores the layout of the main
    _centralWidget : QWidget
        Contains central widget bound to self
    metricConvUI : MetricConvGenUI
        initializes and stores MetricConvGenUI

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initilizer for TestWindow

        Parameters
        ----------
        None

        Returns
        -------
        TestWindow
            the central widget for main application
        """
        super().__init__()
        
        self.setWindowTitle("Metric Conversion")
        self.setFixedSize(400, 400)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.metricConvUI = MetricConvUI()
        self.generalLayout.addWidget(self.metricConvUI)

def main():
    """
    Main drivers that initializes PyQt5 application, creates a TestWindow widget,
    and 4 MetricConvCtrl objects to connect to four different MetricConvWidgets within
    MetricConvUI, as well as the appropriate conversion functions from models.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    baseconv = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    MetricConvCtrl(view=view.metricConvUI.lengthView, model=models.length_conversion)
    MetricConvCtrl(view=view.metricConvUI.weightView, model=models.weight_conversion)
    MetricConvCtrl(view=view.metricConvUI.timeView, model=models.time_conversion)
    MetricConvCtrl(view=view.metricConvUI.digitalStorageView, model=models.digital_space_conversion)
    sys.exit(baseconv.exec())

if __name__ == '__main__':
    main()
