from PyQt5.QtWidgets import QWidget, QLineEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QComboBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class MetricConvUI(QWidget):
    def __init__(self):
        super().__init__()
        unitOptions = [
            "Inches", "Feet", "Yards", "Miles",
            "Millimeters", "Centimeters", "Meters", "Kilometers"
        ]
        
        mainLayout = QHBoxLayout()
        
        self.leftTextEdit = QLineEdit()
        self.leftComboBox = QComboBox()
        mainLayout.addLayout(self._createOptionLayout(self.leftTextEdit, self.leftComboBox, unitOptions))
        
        equalSign = QLabel('=')
        equalSign.setFont(QFont('Arial', 12))
        mainLayout.addWidget(equalSign)

        self.rightTextEdit = QLineEdit()
        self.rightComboBox = QComboBox()
        mainLayout.addLayout(self._createOptionLayout(self.rightTextEdit, self.rightComboBox, unitOptions))
        
        self.setLayout(mainLayout)

    def _createOptionLayout(self, QLineEditObj, QComboBoxObj, items):
        layout = QVBoxLayout()
        
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)
        QLineEditObj.setValidator(validator)

        QLineEditObj.setFont(QFont('Arial', 12))

        QComboBoxObj.addItems(items)
        QComboBoxObj.setFont(QFont('Arial', 12))
        QComboBoxObj.setFixedHeight(20)
        
        layout.addWidget(QLineEditObj)
        layout.addWidget(QComboBoxObj)
        layout.setAlignment(Qt.AlignHCenter)
        
        return layout
        
