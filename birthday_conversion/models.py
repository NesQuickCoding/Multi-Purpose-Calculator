from datetime import date


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