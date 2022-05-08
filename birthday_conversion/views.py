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

        # Our Output Line
        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Output')

        # Our QComboBox
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')
    

        self.show()



    def enterButtonPressed(self):

        #toggledCombo = [cb.text() for cb in self.comboChoice]
        self.calendar_input = [int(self.inputYear.text()), int(self.inputMonth.text()), int(self.inputDay.text())]
        answer = self.getBirthday(self.comboChoice, self.calendar_input)
        #format_answer = "{:.2f}".format(answer)

        self.input.setText(answer)


    def getBirthday(self, combo_input, calendar_input):

        if combo_input == "Years":
            return getYears(self, calendar_input)
        elif combo_input == "Months":
            return getMonths(self, calendar_input)
        elif combo_input == 'Days':
            return getDays(self, calendar_input)


def getYears(self, born):
    c_month = born[0]
    c_day = born[1]
    c_year = born[2]

    today = date.today()
    dob = date(c_year, c_day, c_month)
    time_diff = today - dob
    a_days = time_diff.days
    a_year = int(a_days/365)

    return a_year


def getDays(self, born):
    today = date.today()
    time_diff = today - born
    c_days = time_diff.days
    return c_days


def getMonths(self,born):
    c_days = getDays(born)
    c_months = int((c_days/365) * 12)
        
