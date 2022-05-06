from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

class temp_Ui(QtWidgets.QWidget):
    """ Load in the temperature conversion UI, then connect the logic for the conversion.

    Args:
        QtWidgets (module): base class for user interface objects.
    """
    def __init__(self):
        """Load in the UI file from Qt creator, then find the UI components we need to connect logic to.
        """
        super(temp_Ui, self).__init__()
        uic.loadUi('../Graphical-App/temp_conversion/temp_conv.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton') # Find the enter button 
        self.button.clicked.connect(self.enterButtonPressed)
        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        validator = QDoubleValidator(decimals=2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.input.setValidator(validator)
        self.radioButtons = self.findChildren(QtWidgets.QRadioButton)

        # Set default radio buttons to prevent IndexError; toggleButtons would return en empty list otherwise
        self.radioButtons[0].setChecked(True)
        self.radioButtons[3].setChecked(True)

        self.show()

    def enterButtonPressed(self):
        """Connect the UI to process the temperature conversion when hitting the enter button. Display the answer
        in the text box. 
        """
        # checks to see if input is not empty to prevent ValueError
        if self.input.text():
            toggledButtons = [rb.text() for rb in self.radioButtons if rb.isChecked()]
            answer = self.convert_temp(float(self.input.text()), toggledButtons[0][0], toggledButtons[1][0])
            format_answer = "{:.2f}".format(answer)
            self.input.setText(format_answer)
        

    def convert_temp(self, val, original_unit, unit_to_convert_to):
        """Convert the temperature given by the user.

        Args:
            val (float): the temperature value to convert
            original_unit (str): original temperature unit
            unit_to_convert_to (str): temperature unit to convert to

        Returns:
            float: converted temperature value
        """
        fahren_to_celcius = (val - 32)/1.8
        celcius_to_fahren = (val * 1.8) + 32
        fahren_to_kelvin = (val - 32) / 1.8 + 273.15
        kelvin_to_farhen = val * 1.8 - 459.67
        celcius_to_kelvin = val + 273.15 
        kelvin_to_celcius = val - 273.15 
        
        if unit_to_convert_to == 'K':
            if original_unit =='C':
                return celcius_to_kelvin
            elif original_unit == 'F':
                return fahren_to_kelvin
            else: return val
        elif unit_to_convert_to == 'C':
            if original_unit == 'F':
                return fahren_to_celcius
            elif original_unit == 'K':
                return kelvin_to_celcius
            else: return val
        elif unit_to_convert_to == 'F':
            if original_unit == 'K':
                return kelvin_to_farhen
            elif original_unit == 'C':
                return celcius_to_fahren
            else: return val

    # You can use this to test out the tempconv window without running the other UI components. 

    # app = QtWidgets.QApplication(sys.argv)
    # window = temp_Ui()
    # app.exec_()
