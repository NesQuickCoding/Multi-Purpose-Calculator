from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

class temp_Ui(QtWidgets.QWidget):
    def __init__(self):
        super(temp_Ui, self).__init__()
        uic.loadUi('../Graphical-App/temp_conversion/basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton') # Find the button
        self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.input.setValidator(QDoubleValidator(decimals=3))
        self.radioButtons = self.findChildren(QtWidgets.QRadioButton)

        # Set default radio buttons to prevent IndexError; toggleButtons would return en empty list otherwise
        self.radioButtons[0].setChecked(True)
        self.radioButtons[3].setChecked(True)

        self.show()

    def printButtonPressed(self):
        toggledButtons = [rb.text() for rb in self.radioButtons if rb.isChecked()]
        answer = self.convert_temp(float(self.input.text()), toggledButtons[0][0], toggledButtons[1][0])
        format_answer = "{:.3f}".format(answer)
        self.input.setText(str(format_answer))
        
    def convert_temp(self, val, original_unit, unit_to_convert_to):
        fahren_to_celcius = (val - 32)/1.8
        celcius_to_fahren = (val * 1.8) + 32
        fahren_to_kelvin = (val - 32) / 1.8 + 273.15
        kelvin_to_farhen = val * 1.8 - 459.67

        if original_unit == unit_to_convert_to:
            return val
        elif unit_to_convert_to == 'K':
            if original_unit =='C':
                return val + 273.15
            elif original_unit == 'F':
                return fahren_to_kelvin
        elif unit_to_convert_to == 'C':
            if original_unit == 'F':
                return fahren_to_celcius
            else:
                return val - 273.15
        elif unit_to_convert_to == 'F':
            if original_unit == 'K':
                return kelvin_to_farhen
            else:
                return celcius_to_fahren
