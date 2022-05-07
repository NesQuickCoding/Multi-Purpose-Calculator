from PyQt5.QtWidgets import QWidget, QLineEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QComboBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class MetricConvWidget(QWidget):
    def __init__(self, stringLabel, unitOptions):
        super().__init__()   
        mainLayout = QVBoxLayout()
        
        label = QLabel(stringLabel)
        label.setFont(QFont('Arial', 12))
        mainLayout.addWidget(label)

        convLayout = QHBoxLayout()

        self.leftTextEdit = QLineEdit()
        self.leftComboBox = QComboBox()
        convLayout.addLayout(self._createOptionLayout(self.leftTextEdit, self.leftComboBox, unitOptions))
        
        equalSign = QLabel('=')
        equalSign.setFont(QFont('Arial', 12))
        convLayout.addWidget(equalSign)

        self.rightTextEdit = QLineEdit()
        self.rightComboBox = QComboBox()
        convLayout.addLayout(self._createOptionLayout(self.rightTextEdit, self.rightComboBox, unitOptions))
        
        mainLayout.addLayout(convLayout)

        self.setLayout(mainLayout)

    def _createOptionLayout(self, QLineEditObj, QComboBoxObj, items):
        layout = QVBoxLayout()
        
        QLineEditObj.setValidator(QDoubleValidator())

        QLineEditObj.setFont(QFont('Arial', 12))

        QComboBoxObj.addItems(items)
        QComboBoxObj.setFont(QFont('Arial', 12))
        QComboBoxObj.setFixedHeight(20)
        
        layout.addWidget(QLineEditObj)
        layout.addWidget(QComboBoxObj)
        layout.setAlignment(Qt.AlignHCenter)
        
        return layout

class MetricConvUI(QWidget):
    def __init__(self):
        super().__init__()

        lengthUnitOptions = [
            "Inches", "Feet", "Yards", "Miles",
            "Millimeter", "Centimeter", "Meter", "Kilometer"
        ]

        weightUnitOptions = [
            "Ounces", "Pounds", "Stone", "Tons",
            "Milligram", "Gram", "Kilogram"
        ]

        timeUnitOptions = [
            "Milliseconds", "Seconds", "Minutes", "Hours",
            "Days", "Months", "Years"
        ]

        digitalStorageOptions = [
            "just a test"
        ]

        layout = QVBoxLayout()

        self.lengthView = MetricConvWidget("Length", lengthUnitOptions)
        layout.addWidget(self.lengthView)

        self.weightView = MetricConvWidget("Weight", weightUnitOptions)
        layout.addWidget(self.weightView)

        self.timeView = MetricConvWidget("Time", timeUnitOptions)
        layout.addWidget(self.timeView)

        self.digitalStorageView = MetricConvWidget("Digital Storage", digitalStorageOptions)
        layout.addWidget(self.digitalStorageView)

        self.setLayout(layout)


        
