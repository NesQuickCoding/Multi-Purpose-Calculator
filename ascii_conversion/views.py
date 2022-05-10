from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class ascii_Ui(QtWidgets.QWidget):
    def __init__(self):
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
        # Allow any character, but only 1 at most
        chrValidator = QRegExpValidator(QRegExp(".{1}"))
        # Valid range for chr() is 0 to 1,114,111
        # This doesn't entirely prevent values above 1114111 alone
        intValidator = QIntValidator(0, 1114111)
        # Hex validator can accept 0x as initial input or not, followed by 0-9a-fA-F
        hexValidator = QRegExpValidator(QRegExp("(0x)?[\da-fA-F]+"))

        return [chrValidator, intValidator, hexValidator]

    def _rangeValidator(self):
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
        toggledButtons = [rb.text() for rb in self.radioButtons if rb.isChecked()]
        answer = self.convert_ascii(self.input.text(), toggledButtons[0][0], toggledButtons[1][0])
        self.output.setText(str(answer))

    def convert_ascii(self, val, input_unit, output_unit):
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
