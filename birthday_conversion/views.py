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
    def __init__(self):
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
        self.yearLimit = date.today().year

        # signal connectors for inputs
        self.inputDay.textChanged.connect(self._inputCheck)
        self.inputMonth.textChanged.connect(self._inputCheck)
        self.inputYear.textChanged.connect(self._inputCheck)

    def _inputCheck(self):
        # run checks only if there's a value for month
        if self.inputMonth.text():
            if int(self.inputMonth.text()) <= 0:
                self.inputMonth.setText("")
            elif int(self.inputMonth.text()) > 12:
                self.inputMonth.setText("12")
        
        # run checks only if there's a value for year
        if self.inputYear.text():
            if int(self.inputYear.text()) <= 0:
                self.inputYear.setText("")
            elif int(self.inputYear.text()) > self.yearLimit:
                self.inputYear.setText(str(self.yearLimit))
        
        # run checks only if there's a value for day
        if self.inputDay.text():
            if int(self.inputDay.text()) <= 0:
                self.inputDay.setText("")
            else:
                # since the limit of days depends on the month and year,
                # we'll run several different cases
                # using try/except value error in case month does not have input
                try:
                    # check limit if month as 31 days
                    if int(self.inputMonth.text()) in [1, 3, 5, 7, 8, 10, 12]:
                        if int(self.inputDay.text()) > 31:
                            self.inputDay.setText("31")
                    
                    # check for limit for feburary
                    elif int(self.inputMonth.text()) == 2:

                        # using try/except for value error in case year has no input
                        try:
                            # check for leap year
                            if int(self.inputYear.text()) % 4 == 0 and int(self.inputDay.text()) > 29:
                                self.inputDay.setText("29")
                            elif int(self.inputYear.text()) % 4 != 0 and int(self.inputDay.text()) > 28:
                                self.inputDay.setText("28")

                        except ValueError: 
                            # no year input, assume 28 days
                            if int(self.inputDay.text()) > 28:
                                self.inputDay.setText("28")
                    
                    # all other months have 30 days
                    else:
                        if int(self.inputDay.text()) > 30:
                            self.inputDay.setText("30")
                
                except ValueError:
                    # no month input, assume 31 days
                    if int(self.inputDay.text()) > 31:
                            self.inputDay.setText("31")
        
        # check to see if date is past today's date
        # only check if all three fields have input
        if self.inputDay.text() and self.inputMonth.text() and self.inputYear.text():
            if date(int(self.inputYear.text()), int(self.inputMonth.text()), int(self.inputDay.text())) > date.today():
                self.inputDay.setText(str(date.today().day))
                self.inputMonth.setText(str(date.today().month))
                self.inputYear.setText(str(date.today().year))
        
    def enterButtonPressed(self):
        # try/except to ignore missing input fields
        try:
            self.lineEdit_Output.clear()
            current_choice = self.comboBox.currentText()
            month = int(self.inputMonth.text())
            day = int(self.inputDay.text())
            year = int(self.inputYear.text())
            dob_list = [month,day,year]
            answer = self.get_birthday(current_choice,dob_list)
            self.lineEdit_Output.setText(answer)
        except ValueError:
            pass

    def get_birthday(self, combo_input, calendar_input):
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
    today = date.today()
    dob = date(year, month, day)
    time_diff = today - dob
    a_days = time_diff.days
    a_years = int(a_days/365)
    return a_years

def get_days(month,day,year):
    dob = date(year, month, day)
    today = date.today()
    time_diff = today - dob
    a_days = time_diff.days
    return a_days

def get_months(month,day,year):
    dob = date(year, month, day)
    today = date.today()
    time_diff = today - dob
    c_days = time_diff.days
    a_months = int((c_days/365) * 12)
    return a_months
