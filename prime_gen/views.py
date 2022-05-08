from PyQt5.QtWidgets import QWidget, QScrollArea, QLabel, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QRegExp

# Helper Label
class ScrollLabel(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        layout = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(self.label)
    
    def setText(self, text):
        self.label.setText(text)
    
    def text(self):
        return self.label.text()

class PrimeRangeGen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.rangeHeader = self._CreateRangeHeader()
        layout.addWidget(self.rangeHeader)
        self.rangeInput = self._CreateRangeInput()
        layout.addWidget(self.rangeInput)
        rangeButtons = self._CreateRangeButtons()
        layout.addLayout(rangeButtons)
        self.primeRangeOutput = ScrollLabel()
        layout.addWidget(self.primeRangeOutput)
        self.setLayout(layout)

    def _CreateRangeHeader(self):
        header = QLabel("Enter a number from 1 to 1000000")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont('Arial', 14))
        return header

    def _CreateRangeInput(self):
        inputWidget = QLineEdit()
        inputWidget.setFont(QFont('Arial', 14))
        inputWidget.setValidator(QIntValidator(1, 1000000))
        inputWidget.setFixedHeight(26)
        inputWidget.setAlignment(Qt.AlignLeft)
        inputWidget.setReadOnly(False)
        inputWidget.setClearButtonEnabled(True)
        inputWidget.setMaxLength(7)
        return inputWidget

    def _CreateRangeButtons(self):
        buttonLayout = QHBoxLayout()
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.rangeGenButton = QPushButton("Generate")
        self.rangeGenButton.setFixedSize(80, 26)
        buttonLayout.addWidget(self.rangeGenButton, alignment=Qt.AlignCenter)

        self.rangeGenCopy = QPushButton("Copy All")
        self.rangeGenCopy.setFixedSize(70, 26)
        buttonLayout.addWidget(self.rangeGenCopy, alignment=Qt.AlignCenter)

        self.rangeGenClear = QPushButton("Clear")
        self.rangeGenClear.setFixedSize(70, 26)
        buttonLayout.addWidget(self.rangeGenClear, alignment=Qt.AlignCenter)
    
        return buttonLayout

    def setRangeOutput(self, text):
        self.primeRangeOutput.setText(text)
        self.primeRangeOutput.setFocus()

    def getRangeOutput(self):
        return self.primeRangeOutput.text()

    def clearRangeOutput(self):
        self.setRangeOutput("")

class PrimeRandomGen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.randomHeader = self._CreateRandomHeader()
        layout.addWidget(self.randomHeader)
        randomInput = self._CreateRandomInput()
        layout.addLayout(randomInput)
        randomButtons = self._CreateRandomButtons()
        layout.addLayout(randomButtons)
        self.randomNumOutput = ScrollLabel()
        layout.addWidget(self.randomNumOutput)
        self.setLayout(layout)

    def _CreateRandomHeader(self):
        header = QLabel("Random Prime Numbers with Digit Length")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont('Arial', 14))
        return header

    def _CreateRandomInput(self):
        digitLayout = QHBoxLayout()
        numberLayout = QHBoxLayout()
        
        self.randomDigitLabel = QLabel("Amount of Digits (1-12)")
        self.randomDigitInput = QLineEdit()
        self.randomDigitLabel.setAlignment(Qt.AlignLeft)
        self.randomDigitInput.setAlignment(Qt.AlignLeft)
        self.randomAmountLabel = QLabel("Amount of Numbers (1-50)")
        self.randomAmountInput = QLineEdit()
        self.randomAmountLabel.setAlignment(Qt.AlignRight)
        self.randomAmountInput.setAlignment(Qt.AlignCenter)

        self.randomDigitInput.setValidator(QIntValidator(1, 12))
        self.randomDigitInput.setFixedWidth(50)
        self.randomDigitInput.setClearButtonEnabled(True)
        self.randomDigitInput.setMaxLength(2)

        self.randomAmountInput.setValidator(QIntValidator(1, 12))
        self.randomAmountInput.setFixedWidth(50)
        self.randomAmountInput.setClearButtonEnabled(True)
        self.randomAmountInput.setMaxLength(2)

        digitLayout.addWidget(self.randomDigitLabel)
        digitLayout.addWidget(self.randomDigitInput)
        numberLayout.addWidget(self.randomAmountLabel)
        numberLayout.addWidget(self.randomAmountInput)

        randomLayout = QHBoxLayout()
        randomLayout.addLayout(digitLayout)
        randomLayout.addLayout(numberLayout)

        return randomLayout

    def _CreateRandomButtons(self):
        buttonLayout = QHBoxLayout()
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.randomGenButton = QPushButton("Generate")
        self.randomGenButton.setStyleSheet(open("Ext_Stylesheet.css").read())
        #self.randomGenButton.setFixedSize(80, 26)
        buttonLayout.addWidget(self.randomGenButton, alignment=Qt.AlignCenter)

        self.randomGenCopy = QPushButton("Copy All")
        #self.randomGenCopy = QPushButton(open("Ext_Stylesheet.css").read())
        #self.randomGenCopy.setFixedSize(70, 26)
        buttonLayout.addWidget(self.randomGenCopy, alignment=Qt.AlignCenter)

        self.randomGenClear = QPushButton("Clear")
        self.randomGenClear.setStyleSheet(open("Ext_Stylesheet.css").read())
        #self.randomGenClear.setFixedSize(70, 26)
        buttonLayout.addWidget(self.randomGenClear, alignment=Qt.AlignCenter)
    
        return buttonLayout

    def setRandomOutput(self, text):
        self.randomNumOutput.setText(text)
        self.randomNumOutput.setFocus()

    def getRandomOutput(self):
        return self.randomNumOutput.text()

    def clearRandomOutput(self):
        self.setRandomOutput("")

class IsPrime(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.isPrimeHeader = self._CreateIsPrimeHeader()
        layout.addWidget(self.isPrimeHeader)
        hLayout = QHBoxLayout()
        isPrimeInput = self._CreateIsPrimeInput()
        hLayout.addLayout(isPrimeInput)
        isPrimeOutput = self._CreateIsPrimeOutput()
        hLayout.addLayout(isPrimeOutput)
        layout.addLayout(hLayout)
        self.setLayout(layout)

    def _CreateIsPrimeHeader(self):
        header = QLabel("Prime Number Validator")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont('Arial', 14))
        return header
    
    def _CreateIsPrimeInput(self):
        layout = QVBoxLayout()
        self.isPrimeLabel = QLabel("Enter a number")
        self.isPrimeInput = QLineEdit()
        self.isPrimeInput.setFont(QFont('Arial', 14))
        self.isPrimeInput.setFixedHeight(26)
        self.isPrimeInput.setAlignment(Qt.AlignLeft)
        self.isPrimeInput.setClearButtonEnabled(True)
        self.isPrimeInput.setValidator(QRegExpValidator(QRegExp("[0-9]{16}")))
        self.isPrimeButton = QPushButton("Check")
        self.isPrimeButton.setFont(QFont('Arial', 14))
        self.isPrimeButton.setFixedHeight(26)
        layout.addWidget(self.isPrimeLabel)
        layout.addWidget(self.isPrimeInput)
        layout.addWidget(self.isPrimeButton)
        return layout
    
    def _CreateIsPrimeOutput(self):
        layout = QVBoxLayout()
        self.isPrimeIcon = QSvgWidget()
        self.isPrimeIcon.setFixedSize(60, 60)
        self.isPrimeIcon.setStyleSheet("text-align: center;")
        self.isPrimeText = QLabel()
        self.isPrimeText.setFont(QFont('Arial', 14))
        self.isPrimeText.setFixedWidth(120)
        self.isPrimeText.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.isPrimeIcon, 0, Qt.AlignCenter)
        layout.addWidget(self.isPrimeText, 0, Qt.AlignCenter)
        return layout

class PrimeGenUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.primeRangeGen = PrimeRangeGen()
        self.primeRandomGen = PrimeRandomGen()
        self.isPrime = IsPrime()

        self.tabs.addTab(self.primeRangeGen, "Prime Range Gen")
        self.tabs.addTab(self.primeRandomGen, "Prime Random Gen")
        self.tabs.addTab(self.isPrime, "Prime Number Validator")

        layout.addWidget(self.tabs)
        self.setLayout(layout)
