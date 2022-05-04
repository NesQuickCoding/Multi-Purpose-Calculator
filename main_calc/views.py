from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect

class MainCalcUI(QWidget):
    def __init__(self, dropMenu):
        super().__init__()
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()
        self.calcOutput = self._createCalcOutput()
        layout.addWidget(self.calcOutput)
        self.calcDropBox = self._createDropBox(dropMenu)
        layout.addWidget(self.calcDropBox)
        buttonLayout = self._createButtons()
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def _createCalcOutput(self):
        output = QLineEdit("0")
        output.setFixedHeight(50)
        output.setAlignment(Qt.AlignRight)
        output.setReadOnly(True)
        return output       

    def _createDropBox(self, dropMenu):
        comboBox = QComboBox()
        comboBox.setObjectName("CalcDropBox")
        comboBox.setGeometry(QRect(130, 190, 291, 31))
        for item in dropMenu:
            comboBox.addItem(item[0])
        return comboBox

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        buttons = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3), "BS": (0, 4), "C": (0, 5),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3), "//": (1, 4), "(": (1, 5),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3), "**": (2, 4), ")": (2, 5),
            "0": (3, 0), "00": (3, 1), ".": (3, 2), "+": (3, 3), "%": (3, 4), "=": (3, 5),
        }

        for buttonText, pos in buttons.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(55, 55)
            buttonsLayout.addWidget(self.buttons[buttonText], pos[0], pos[1])

        return buttonsLayout

    def setCalcOutput(self, text):
        self.calcOutput.setText(text)

    def getCalcOutput(self):
        return self.calcOutput.text()

    def backSpaceCalcOutput(self):
        # if back space would clear output, reset to zero
        if len(self.getCalcOutput()[0:-1]) == 0:
            self.clearCalcOutput()
        # else remove last character from calcOutput string
        else:
            self.setCalcOutput(str(self.getCalcOutput())[0:-1])

    def clearCalcOutput(self):
        self.setCalcOutput("0")
