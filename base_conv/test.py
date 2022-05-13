import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

# from views import BaseConvUI
# import models
# from controllers import BaseConvCtrl

class TestWindow(QMainWindow):
    """
    Constructs a QMainWindow to create and append to it's window a BaseConvUI
    widget for testing purposes

    Inherits all methods and attributes from QMainWindow

    Attributes
    ----------
    generalLayout : QVBoxLayout
        stores the layout of the main
    _centralWidget : QWidget
        Contains central widget bound to self
    metricConvUI : BaseConvGenUI
        initializes and stores BaseConvGenUI

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
        
        self.setWindowTitle("Base Conversion")
        self.setFixedSize(400, 400)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.baseConvUI = BaseConvUI()
        self.generalLayout.addWidget(self.baseConvUI)

def main():
    """
    Main drivers that initializes PyQt5 application, creates a TestWindow widget,
    and BaseConvCtrl object to connect to signals.

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
    BaseConvCtrl(view=view.baseConvUI, model=models)
    sys.exit(baseconv.exec())

if __name__ == '__main__':
    main()
