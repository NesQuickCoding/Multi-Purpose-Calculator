from PyQt5 import QtWidgets, uic
import sys
from datetime import date
from PyQt5.QtCore import QDate, QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QDialog, QLabel

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
        self.show()



    def enterButtonPressed(self):
        self.lineEdit_Output.clear()
        current_choice = self.comboBox.currentText()
        month = int(self.inputMonth.text())
        day = int(self.inputDay.text())
        year = int(self.inputYear.text())
        dob_list = [month,day,year]
        answer = self.get_birthday(current_choice,dob_list)
        self.lineEdit_Output.setText(answer)


    def get_birthday(self, combo_input, calendar_input):
        if combo_input == "Years":
            return str(get_years(calendar_input))
        elif combo_input == "Months":
            return str(get_months(calendar_input))
        elif combo_input == 'Days':
            return str(get_days(calendar_input))



def get_years(born):
    c_month = born[0]
    c_day = born[1]
    c_year = born[2]
    today = date.today()
    dob = date(c_year, c_month, c_day)
    time_diff = today - dob
    a_days = time_diff.days
    a_year = int(a_days/365)
    return a_year


def get_days(born):
    c_month = born[0]
    c_day = born[1]
    c_year = born[2]
    dob = date(c_year, c_month, c_day)
    today = date.today()
    time_diff = today - dob
    c_days = time_diff.days
    return c_days


def get_months(born):
    c_month = born[0]
    c_day = born[1]
    c_year = born[2]
    dob = date(c_year, c_month, c_day)
    today = date.today()
    time_diff = today - dob
    c_days = time_diff.days
    c_months = int((c_days/365) * 12)
    return c_months