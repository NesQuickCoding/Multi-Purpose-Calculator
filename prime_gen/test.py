import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow

# from views import PrimeGenUI
# import models
# from controllers import PrimeGenCtrl

class TestWindowPrimeGen(QMainWindow):
    """
    Constructs a QMainWindow to create and append to it's window a PrimeGenUI widget
    for testing purposes

    Inherits all methods and attributes from QMainWindow

    Attributes
    ----------
    generalLayout : QVBoxLayout
        stores the layout of the main
    _centralWidget : QWidget
        Contains central widget bound to self
    primeGenUI : PrimeGenUI
        initializes and stores PrimeGenUI

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
        
        self.setWindowTitle("Prime Number Tools")
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.primeGenUI = PrimeGenUI()
        self.generalLayout.addWidget(self.primeGenUI)

def main_test_prime_gen():
    """
    Main drivers that initializes PyQt5 application, creates a TestWindow widget,
    and PrimeGenCtrl to connect to the primeGenUI in the main view, as well as sending
    the models module.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    primegen = QApplication(sys.argv)
    view = TestWindow()
    view.show()
    PrimeGenCtrl(view=view.primeGenUI, model=models)
    sys.exit(primegen.exec())

if __name__ == '__main__':
    main_test_prime_gen()
