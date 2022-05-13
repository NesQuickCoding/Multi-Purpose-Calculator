from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class ascii_Ui(QtWidgets.QWidget):
    """
    Creates a QWidget that converts between a decimal, hexidecimal, and ASCII character value
    Also creates signals, and conversion calculations

    Inhereits all methods and attributes from QWidget

    Attributes
    ----------
    button : QPushButton
        Submit button to initiate conversion
    input : QLineEdit
        Input text field
    validators : [QValidators]
        Used to determine which validations to apply on input, based on the
        radioButtons selection
    output : QLineEdit
        Output text field
    radioButtons : [QRadioButtons]
        A list containing all the radiobuttons in the widget.
        0 - Char (Input)
        1 - Decimal (Input)
        2 - Hexadecimal (Input)
        3 - Char (Output)
        4 - Decimal (Output)
        5 - Hexadecimal (Output)
    
    Methods
    -------
    _createValidators():
        Creates a list of three different validators for chr, int, and hex input
    _rangeValidator():
        Sets roof range input for dec and hex. Changes to the input text if input value
        exceeds the range for chr() (1,114,111). Called every time input changes.
    _setValidators():
        Signal handler to change validation method when radiobuttons input selection changes
    printButtonPressed():
        Sends input to convert_ascii then sets the results to output
    convert_ascii(val, input_unit, output_unit):
        Take the string of val and converts from input_unit to output_unit
    """
    def __init__(self):
        """
        Initializes the ascii_Ui, including it's layout from basic.ui, attributes, and
        signal connections

        Parameters
        ----------
        None

        Returns
        -------
        ascii_Ui
            Newly constructed widget
        """
        super(ascii_Ui, self).__init__()
        uic.loadUi('../Graphical-App/ascii_conversion/basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton')
        self.button.clicked.connect(self.printButtonPressed)

        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Input')
        
        self.input.textChanged.connect(self._rangeValidator)
        
        self.validators = self._createValidators()
        # initial input is chr input
        self.input.setValidator(self.validators[0])
        
        self.output = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Output')
        
        self.radioButtons = self.findChildren(QtWidgets.QRadioButton)
        # Set toggled connectors for only the first three radiobuttons
        # as those dictate input
        for i in range(0, 3):
            self.radioButtons[i].toggled.connect(self._setValidators)
        
        self.show()

    def _createValidators(self):
        """
        Creates a list of three different validators for chr, int, and hex input

        Parameters
        ----------
        None

        Returns
        -------
        [QRegExpValidator, QIntValidator, QRegValidator]
            Three different validators for chr, int, and hex input
        """
        # Allow any character, but only 1 at most
        chrValidator = QRegExpValidator(QRegExp(".{1}"))
        # Valid range for chr() is 0 to 1,114,111
        # This doesn't entirely prevent values above 1114111 alone
        intValidator = QIntValidator(0, 1114111)
        # Hex validator can accept 0x as initial input or not, followed by 0-9a-fA-F
        hexValidator = QRegExpValidator(QRegExp("(0x)?[\da-fA-F]+"))

        return [chrValidator, intValidator, hexValidator]

    def _rangeValidator(self):
        """
        Sets roof range input for dec and hex. Changes to the input text if input value
        exceeds the range for chr() (1,114,111). Called every time input changes.

        Parameters
        ----------
        None

        Raises
        ------
        ValueError
            If during type conversion to Int (usually an empty string) raises a ValueError

        Returns
        -------
        None
        """
        try:
            if [rb.text() for rb in self.radioButtons if rb.isChecked()][0][0] == 'D':
                if int(self.input.text()) == 0:
                    self.input.setText('0')
                # Automatically sets the max limit for chr
                elif int(self.input.text()) > 1114111:
                    self.input.setText('1114111')
            elif [rb.text() for rb in self.radioButtons if rb.isChecked()][0][0] == 'H':
                if int(self.input.text(), 16) > 1114111:
                    self.input.setText('0x10ffff')
        except ValueError:
            pass

    def _setValidators(self):
        """
        Signal handler to change validation method when radiobuttons input selection changes

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # Clears input field when text changes for a clean state
        self.input.setText('')
        isChecked = [rb.text() for rb in self.radioButtons if rb.isChecked()][0][0]
        if isChecked == "C":
            self.input.setValidator(self.validators[0])
        elif isChecked == "D":
            self.input.setValidator(self.validators[1])
        else:
            self.input.setValidator(self.validators[2])

    def printButtonPressed(self):
        """
        Sends input to convert_ascii then sets the results to output

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        toggledButtons = [rb.text() for rb in self.radioButtons if rb.isChecked()]
        answer = self.convert_ascii(self.input.text(), toggledButtons[0][0], toggledButtons[1][0])
        self.output.setText(str(answer))

    def convert_ascii(self, val, input_unit, output_unit):
        """
        Take the string of val and converts from input_unit to output_unit

        Parameters
        ----------
        val : int, str
            Input value to convert
        input_unit : str
            The input value input
        output_unit : str
            The desired converted output
        
        Raises
        ------
        ValueError
            If at any point during the type conversions fail, usually casting empty strings

        Returns
        -------
        int, str
            Final conversion results.
            Type depends if converting to decimal or hexadecimal/char.
        """
        try:
            if input_unit == 'C':
                if output_unit == 'D':
                    return ord(val)
                elif output_unit == 'H':
                    return hex(ord(val))
                else:
                    return val

            elif input_unit == 'D':
                if output_unit == 'C':
                    val = int(val)
                    return chr(val)

                elif output_unit == 'H':
                    return hex(int(val))
                else:
                    return val

            elif input_unit == 'H':
                if output_unit == 'D':
                    return int(val,16)
                elif output_unit == 'C':
                    return chr(int(val, 16))
                else:
                    return val

        except ValueError:
            return "Invalid Input"

# Char Test

#ans1 = convert_ascii('A','C','D')
#print(ans1)
#ans2 = convert_ascii('A','C','H')
#print(ans2)
#ans3 = convert_ascii('A','C','C')
#print(ans3)


# Dec Test
#ans1 = convert_ascii(69,'D','C')
#print(ans1)
#ans2 = convert_ascii(69, 'D','H')
#print(ans2)
#ans3 = convert_ascii(69,'D','D')
#print(ans3)


# Hex Test
#ans1 = convert_ascii("0x45",'H','D')
#print(ans1)
#ans2 = convert_ascii("0x45", 'H','C')
#print(ans2)
#ans3 = convert_ascii("0x45",'H','H')
#print(ans3)
