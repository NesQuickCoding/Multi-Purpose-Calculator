from PyQt5 import QtWidgets, uic
import sys
import datetime
from PyQt5.QtCore import QDate



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




def convert_birthday(self):

    b_List = dateToList(getDate("birthday"))
    c_List = dateToList(getDate("current"))

    user_age = dateDifference(convertDates(b_List,c_List))

    ans = f"Approximate Age: {user_age}"
    return ans


def getDate(self,user_choice):

    if user_choice == "current":
        # Current date today
        # Current month, day, year

        current_date = QDate.currentDate()

        u_month = current_date.month()
        u_day = current_date.day()
        u_year = current_date.year()
    else:
        # We assume it's birthday
        # Users Birthday
        birthday = self.calendar.selectedDate()

        # Birth month, day, year
        u_month = birthday.month()
        u_day = birthday.day()
        u_year = birthday.year()

    return u_month, u_day, u_year

def convertDates(b_list: list, c_list: list):
    b_date = datetime.date(b_list[2], b_list[1], b_list[0])
    c_date = datetime.date(c_list[2], c_list[1], c_list[0])

    return b_date, c_date


def dateDifference(b_date, c_date):
    diff = c_date - b_date

    # Get difference by days
    diff = diff.days

    # Get Differences by years
    # 365 days is equal to 365.2422 days
    years = diff / 365.2422

    # round our years value
    years = round(years)

    ans = str(years)

    # rounding our year values
    years = round(years)


def dateToList(a_month, a_day, a_year):
    dateList = [a_month, a_day, a_year]
    return dateList






#def fixValue(c):
#    return 1


