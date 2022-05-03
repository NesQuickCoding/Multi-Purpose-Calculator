 
"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys
sys.path.insert(0, "./prime_gen/")
from views import PrimeGenTabs
from functools import partial

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget

__version__ = "0.1"
__author__ = "Python Calcuator"

ERROR_MSG = "ERROR"

class CalcMain(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.calcOutput = self._createCalcOutput()
        layout.addWidget(self.calcOutput)
        self.calcDropBox = self._createDropBox()
        layout.addWidget(self.calcDropBox)
        buttonLayout = self._createButtons()
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def _createCalcOutput(self):
        output = QLineEdit()
        output.setFixedHeight(50)
        output.setAlignment(Qt.AlignRight)
        output.setReadOnly(True)
        return output       

    def _createDropBox(self):
        comboBox = QComboBox()
        comboBox.setObjectName("CalcDropBox")
        comboBox.setGeometry(QtCore.QRect(130, 190, 291, 31))
        comboBox.addItem("ASCII Conversion")
        comboBox.addItem("Prime Number Generator/Validator")
        comboBox.addItem("Metric Conversion")
        comboBox.addItem("Temperature Conversion")
        comboBox.addItem("Generate Numbers")
        return comboBox

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }

        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(55, 55)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        return buttonsLayout

    def setDisplayText(self, text):
        """Set display's text."""
        self.calcOutput.setText(text)
        self.calcOutput.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.calcOutput.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("Multi-Purpose Calculator")
        self.setFixedSize(800, 400)
        # Set the central widget and the general layout
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.calcMain = CalcMain()
        self.placeHolder = QLabel("Nothing yet")
        self.primeGenTabs = PrimeGenTabs()
        self.generalLayout.addWidget(self.calcMain)
        self.generalLayout.addWidget(self.primeGenTabs)
        self.generalLayout.addWidget(self.placeHolder)


# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc's Controller."""

    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.calcMain.displayText())
        self._view.calcMain.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.calcMain.displayText() == ERROR_MSG:
            self._view.calcMain.clearDisplay()

        expression = self._view.calcMain.displayText() + sub_exp
        self._view.calcMain.setDisplayText(expression)

    def _changeSide(self):
        print("it changed")

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.calcMain.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.calcMain.buttons["="].clicked.connect(self._calculateResult)
        self._view.calcMain.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.calcMain.buttons["C"].clicked.connect(self._view.calcMain.clearDisplay)
        self._view.calcMain.calcDropBox.currentIndexChanged.connect(self._changeSide)


# Client code
def main():
    """Main function."""
    # Create an instance of `QApplication`
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    controller = PyCalcCtrl(model=model, view=view)
    # Execute calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()
