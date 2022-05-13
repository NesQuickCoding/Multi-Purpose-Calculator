from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect

class MainCalcUI(QWidget):
    """
    A QWidget that creates the interface widget of a standard calculator that performs
    basic functions, such as add, subtract, divide, multiply, floor division, etc.

    Aside from the main calculator, also has a dropbox for a secondary calculator widget.

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    calcOutput : QLineEdit
        Main calc display for expression building and evaluation output
    calcDropBox : QComboBox
        Secondary calc option menu
    buttons : [QPushButton]
        A list of QPushButton objects, each one a button for the calculator

    Methods
    -------
    _createCalcOutput():
        Creates QLineEdit object for calc output display
    _createDropBox(dropMenu):
        Creates QComboBox with list of dropMenu options
    _createButtons():
        Creates buttons in QGridLayout
    setCalcOutput(text):
        Changes calcOutput to text argument
    getCalcOutput():
        Returns calcOutput text value
    backSpaceCalcOutput():
        Removes last input character in expression
    clearCalcOutput():
        Sets calcOutput to "0"
    """
    def __init__(self, dropMenu):
        """
        Initializer for MainCalcUI. Creates all QWidgets and layouts.

        Parameters
        ----------
        dropMenu : [str]
            List of different widgets for the secondary calc display

        Returns
        -------
        MainCalcUI
            Initalized MainCalcUI
        """
        super().__init__()
        self.setFixedSize(400, 450)
        layout = QVBoxLayout()
        self.calcOutput = self._createCalcOutput()
        layout.addWidget(self.calcOutput)
        self.calcDropBox = self._createDropBox(dropMenu)
        layout.addWidget(self.calcDropBox)
        buttonLayout = self._createButtons()
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def _createCalcOutput(self):
        """
        Creates a QLineEdit object for calcOutput

        Parameters
        ----------
        None

        Returns
        -------
        QLineEdit
            calcOutput with alignment defaults
        """
        output = QLineEdit("0")
        output.setAlignment(Qt.AlignRight)
        output.setReadOnly(True)
        output.setObjectName("calcOutput")
        return output       

    def _createDropBox(self, dropMenu):
        """
        Creates a QComboBox for calcDropBox

        Parameters
        ----------
        dropMenu: [str]
            List of possible secondary calc widgets to display

        Returns
        -------
        QComboBox
            Initialized and set up QComboBox for calcDropBox
        """
        comboBox = QComboBox()
        comboBox.setObjectName("calcDropBox")
        for item in dropMenu:
            comboBox.addItem(item[0])
        return comboBox

    def _createButtons(self):
        """
        Creates a all the QPushButtons for the calculator for expression
        building

        Parameters
        ----------
        None

        Returns
        -------
        QGridLayout
            Initialized placement setup for QPushButtons
        """
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        buttons = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3), "BS": (0, 4), "C": (0, 5),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3), "//": (1, 4), "(": (1, 5),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3), "**": (2, 4), ")": (2, 5),
            "0": (3, 0), "00": (3, 1), ".": (3, 2), "+": (3, 3), "%": (3, 4), "=": (3, 5),
        }

        for buttonText, pos in buttons.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(55, 55)
            self.buttons[buttonText].setObjectName("calcButton")
            buttonsLayout.addWidget(self.buttons[buttonText], pos[0], pos[1])

        return buttonsLayout

    def setCalcOutput(self, text):
        """
        Sets calcOutput text display

        Parameters
        ----------
        text : str
            New text to change to

        Returns
        -------
        None
        """
        self.calcOutput.setText(text)

    def getCalcOutput(self):
        """
        Returns calcOutput's text value

        Parameters
        ----------
        None

        Returns
        -------
        str
            Current calcOutput's text value
        """
        return self.calcOutput.text()

    def backSpaceCalcOutput(self):
        """
        Reset calcOutput's text to "0" when output is empty.
        Else removes the last character from the str.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # if back space would clear output, reset to zero
        if len(self.getCalcOutput()[0:-1]) == 0:
            self.clearCalcOutput()
        # else remove last character from calcOutput string
        else:
            self.setCalcOutput(str(self.getCalcOutput())[0:-1])

    def clearCalcOutput(self):
        """
        Reset calcOutput's text to "0" when output is empty.
        Else removes the last character from the str.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.setCalcOutput("0")
