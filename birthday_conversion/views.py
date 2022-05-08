from PyQt5 import QtWidgets, uic
import sys
from datetime import date
from PyQt5.QtCore import QDate

"""
References:
https://pererapm.medium.com/find-out-how-many-seconds-old-you-are-using-python-and-explanation-of-code-ab2a48b9be3c
https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/amp/
https://stackoverflow.com/questions/68997443/calculate-age-in-day-month-and-year-from-birth-date-and-a-specific-day-using-py
"""

class birthday_Ui(QtWidgets.QWidget):
    def __init__(self):
        super(birthday_Ui, self).__init__()
        uic.loadUi('../Graphical-App/birthday_conversion/basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'enterButton')
        self.button.clicked.connect(self.printButtonPressed)
        self.input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Output')

        self.show()

    def printButtonPressed(self):
        #radioButtons = self.findChildren(QtWidgets.QRadioButton)
        #toggledButtons = [rb.text() for rb in radioButtons if rb.isChecked()]
        self.clicked.connect(self.convert_birthday)
        val = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Output')
        answer = convert_birthday(self)
        #format_answer = "{:.2f}".format(answer)
        self.input.setText(str(answer))

def getYears(self, born):
    today = date.today()

    # Try Catch to check if we have a leap year
    # Make sure current year is not leap year
    try:
        b_day = born.replace(year = today.year)
    except ValueError:
            b_day = born.replace(year = today.year, month = born.month + 1, day = 1)
    if b_day > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


def getDays(self, born):
    today = date.today()
    time_diff = today - born
    c_days = time_diff.days
    return c_days


def getMonths(self,born):
    c_days = getDays(born)
    c_months = int((c_days/365) * 12)