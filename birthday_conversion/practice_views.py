# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Birthday Conversion ")

        # Geometry
        self.setGeometry(0, 0, 480, 400)
        self.setFixedSize(480,400)

        # Call UiComponents method
        self.UiComponents()

        # Show widgets
        self.show()

    # Method for all the widgets
    def UiComponents(self):
        # creating a combo box widget
        self.combo_box = QComboBox(self)

        # Geometry for combo box
        self.combo_box.setGeometry(100, 270, 141, 41)
        self.setFixedSize(480,400)

        # choice for our combo box
        age_list = ["Years", "Months", "Days"]

        # Making combo_box not editable
        self.combo_box.setEditable(False)

        # adding list of items to combo box
        self.combo_box.addItems(age_list)

        # Get the current
        self.combo_box.accessibleName()
        print(self.combo_box.textActivated)


        # QLabels
        label_Month = QLabel(self)
        label_Month.setText("Month")
        label_Month.move(110,70)

        label_Day = QLabel(self)
        label_Day.setText("Day")
        label_Day.move(110,130)

        label_Year = QLabel(self)
        label_Year.setText("Year")
        label_Year.move(110, 190)

        # QLines
        input_Month = QLineEdit(self)
        input_Month.move(260,70)
        input_Month.setGeometry(260, 70, 100, 41)

        input_Day = QLineEdit(self)
        input_Day.move(260,130)
        input_Day.setGeometry(260, 130, 100, 41)

        input_Year = QLineEdit(self)
        input_Year.move(260,190)
        input_Year.setGeometry(260,190,100,41)

        line_Output = QLineEdit(self)
        line_Output.move(260, 270)
        line_Output.setGeometry(260, 270, 100, 41)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())