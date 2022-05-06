from PyQt5.QtWidgets import QWidget, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QComboBox
from PyQt5.QtGui import QFont

class MetricConvUI(QWidget):
    def __init__(self):
        super().__init__()
        unitOptions = [
            "Inches", "Feet", "Yards", "Miles",
            "Millimeters", "Centimeters", "Meters", "Kilometers"
        ]
        
        mainLayout = QVBoxLayout()
        self.inputDropBox = None
        self.outputDropBox = None
        menuLayout = QHBoxLayout()
        menuLayout.addLayout(self._createSelectionMenuLayout("Convert From", self.inputDropBox, unitOptions))
        menuLayout.addLayout(self._createSelectionMenuLayout("Convert To", self.outputDropBox, unitOptions))
        mainLayout.addLayout(menuLayout)
        
        self.setLayout(mainLayout)

    def _createSelectionMenuLayout(self, labelString, QComboBoxObj, items):
        layout = QVBoxLayout()
        label = QLabel(labelString)
        QComboBoxObj = QComboBox()
        QComboBoxObj.addItems(items)
        
        layout.addWidget(label)
        layout.addWidget(QComboBoxObj)

        return layout
