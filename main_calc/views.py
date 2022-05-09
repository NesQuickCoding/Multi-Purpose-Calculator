from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect

class MainCalcUI(QWidget):
    """Initialize main calculator window.

    Args:
        QWidget (module): base class for user UI objects to build off of.
    """
    def __init__(self, dropMenu):
        """Initialize the calculator, set widgets for basic arithmetic, then connect
        the other views to the main window through a dropdown menu.

        Args:
            dropMenu (comboBox): drop down menu for switching windows on the right-hand side.
        """
        super().__init__()
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()
        self.calcOutput = self._createCalcOutput()
        layout.addWidget(self.calcOutput)
        self.calcDropBox = self._createDropBox(dropMenu)
        layout.addWidget(self.calcDropBox)
        buttonLayout = self._createButtons()
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def _createCalcOutput(self):
        """Create the output box for expression and answer to use.

        Returns:
            LineEdit: widget for writing and recieving text.
        """
        output = QLineEdit("0")
        output.setFixedHeight(50)
        output.setAlignment(Qt.AlignRight)
        output.setReadOnly(True)
        return output       

    def _createDropBox(self, dropMenu):
        """Add items from drop down menu to main calc window

        Args:
            dropMenu (list): List of menu items and widgets to connect for secondary calc.

        Returns:
            ComboBox: Drop down menu
        """
        comboBox = QComboBox()
        comboBox.setObjectName("CalcDropBox")
        comboBox.setGeometry(QRect(130, 190, 291, 31))
        for item in dropMenu:
            comboBox.addItem(item[0])
        return comboBox

    def _createButtons(self):
        """Create views for buttons of main calculator

        Returns:
            button_layout: grid containing all of the buttons necessary for the main calc.
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
            buttonsLayout.addWidget(self.buttons[buttonText], pos[0], pos[1])

        return buttonsLayout

    def setCalcOutput(self, text):
        """Set the textBox with the given answer from evaluating.

        Args:
            text (str): answer to calculation
        """
        self.calcOutput.setText(text)

    def getCalcOutput(self):
        """Return the given text inside of the textbox

        Returns:
            Str: answer to evaluated expression 
        """
        return self.calcOutput.text()

    def backSpaceCalcOutput(self):
        """Reset to zero when output is clear, or else remove the last character from the str.
        """
        # if back space would clear output, reset to zero
        if len(self.getCalcOutput()[0:-1]) == 0:
            self.clearCalcOutput()
        # else remove last character from calcOutput string
        else:
            self.setCalcOutput(str(self.getCalcOutput())[0:-1])

    def clearCalcOutput(self):
        """Clear calculator output box
        """
        self.setCalcOutput("0")
