from PyQt5 import QtWidgets, uic
from datetime import date
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator

"""
References:
https://codingshiksha.com/python/python-pyqt5-gui-birthday-age-calculator-with-calendar-widget-desktop-app-full-project-for-beginners/
https://pererapm.medium.com/find-out-how-many-seconds-old-you-are-using-python-and-explanation-of-code-ab2a48b9be3c
https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/amp/
https://stackoverflow.com/questions/68997443/calculate-age-in-day-month-and-year-from-birth-date-and-a-specific-day-using-py
"""

class birthday_Ui(QtWidgets.QWidget):
    """
        Creates a QWidget that converts a valid birthdate / date to years, days, or months
        based on users combo box choice.

        Inhereits all methods and attributes from QWidget

        Attributes
        ----------
         clearButton:
            clears input and output text fields.
         enterButton:
            button to initiate the converison.
        input : QLineEdit
            lineEdit_Day:
                for int input representing a calendar 1 or 2 digit day
                ranging from 1 to 31 based on months.

            lineEdit_Month:
                for int input representing a 1 or 2 digit number
                for months ranging from 1 to 12.

            lineEdit_Year:
                for int input having 4 digits representing years.

            Input text field
                QComboBox
            User input based on listed items (Years, Months, Days)

        validators : [QValidators]
            Used to determine which validations to apply to the input based
            on users input.
        output : QLineEdit
            Output text field
        comboBox = [QComboBox]
            A list of all the box options.
            0 - Years (Input)
            1 - Months (Input)
            2 - Days (Input)

        Methods
        -------

        enterButtonPressed():
            Sends a list input that contains [month,day,year] from user input
            to get_birthday then sets the text of output to the results

        def get_birthday(self, combo_input, calendar_input):
            Takes in  a list and a choice input from the combo box for the type of conversion the user wants
            Years, Months, Days and returns the conversion in text.

        def get_years(month,day,year):
            Takes in a tuple of int values that represents a birthdate and converts it to
            years based on present day.

        def get_days(month,day,year):
            Takes in a tuple of int values that represents a birthdate and converts it to
            days based on present day.

        def get_months(month,day,year):
            Takes in a tuple of int values that represents a birthdate and converts it to
            months based on present day.


        """
    def __init__(self):
        """
          Initializes the birthday_Ui, including it's layout from basic.ui and attributes

          Parameters
          ----------
          None

          Returns
          -------
          birthday_Ui
              Newly constructed widget
          """
        super(birthday_Ui, self).__init__()
        uic.loadUi('../Graphical-App/birthday_conversion/basic.ui', self)

        # Our Enter Button
        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton')
        self.button.clicked.connect(self.enterButtonPressed)

        # Valid Months
        self.inputMonth = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Month')
        month_validator = QIntValidator(1,12)
        self.inputMonth.setValidator(month_validator)

        # Valid Days
        self.inputDay = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Day')
        day_validator = QIntValidator(1,31)
        self.inputDay.setValidator(day_validator)

        # Valid Years
        self.inputYear = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Year')
        reg_exp = QRegExp("^[19|20][0-9]{3}$")
        year_validator = QRegExpValidator(reg_exp)
        self.inputYear.setValidator(year_validator)
        self.show()



    def enterButtonPressed(self):
        """
         Sends a list input that contains [month,day,year] from user input
         to get_birthday then sets the text of output to the results

         Parameters
         ----------
         None

         Returns
         -------
         None
         """
        self.lineEdit_Output.clear()
        current_choice = self.comboBox.currentText()
        month = int(self.inputMonth.text())
        day = int(self.inputDay.text())
        year = int(self.inputYear.text())
        dob_list = [month,day,year]
        answer = self.get_birthday(current_choice,dob_list)
        self.lineEdit_Output.setText(answer)


    def get_birthday(self, combo_input, calendar_input):
        """
        Takes in  a list and a choice input from the combo box for the type of conversion the user wants
        Years, Months, Days and returns the conversion in text.

        Parameters
        ----------

        combo_input: list, int
            Month, Day, and Year input value to convert
        calender_input:
            Input choice from the combo box depending on the conversion user picks.

        Raises
        ------
         ValueError
            If the user entered a date that is considered invalid.

        Returns
        -------
            str that represents the int converison

        """
        try:
            c_month = calendar_input[0]
            c_day = calendar_input[1]
            c_year = calendar_input[2]
            date(c_year, c_month, c_day)

            if combo_input == "Years":
                return str(get_years(c_month, c_day, c_year))
            elif combo_input == "Months":
                return str(get_months(c_month, c_day, c_year))
            elif combo_input == 'Days':
                return str(get_days(c_month, c_day, c_year))

        except ValueError:
            return "Invalid"



def get_years(month,day,year):
    """
    Takes in a tuple of int values that represents a birthdate and converts it to
    years based on present day.

    Parameters
    ----------
    month : int
        Input value to convert
    day:   int
        Input value to convert
    year: int
        Input value to convert

    Returns
    -------
        int value
    """
    today = date.today()
    dob = date(year, month, day)
    time_diff = today - dob
    a_days = time_diff.days
    a_years = int(a_days/365)
    return a_years


def get_days(month,day,year):
    """
    Takes in a tuple of int values that represents a birthdate and converts it to
    days based on present day.

    Parameters
    ----------
    month : int
        Input value to convert
    day:   int
        Input value to convert
    year: int
        Input value to convert

    Returns
    -------
        int value
    """
    dob = date(year, month, day)
    today = date.today()
    time_diff = today - dob
    a_days = time_diff.days
    return a_days


def get_months(month,day,year):
    """
    Takes in a tuple of int values that represents a birthdate and converts it to
    months based on present day.

    Parameters
    ----------
    month : int
        Input value to convert
    day:   int
        Input value to convert
    year: int
        Input value to convert

    Returns
    -------
        int value
    """
    dob = date(year, month, day)
    today = date.today()
    time_diff = today - dob
    c_days = time_diff.days
    a_months = int((c_days/365) * 12)
    return a_months