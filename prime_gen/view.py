from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator, QRegExpValidator

from PyQt5.QtSvg import QSvgWidget, QSvgRenderer

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

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

class PrimeGenUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prime Number Generator')
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout((self.generalLayout))

        self._CreateRangeHeader()
        self._CreateRangeInput()
        self._CreateRangeButtons()
        self.primeRangeOutput = ScrollLabel()
        self.generalLayout.addWidget(self.primeRangeOutput)

        self._CreateRandomHeader()
        self._CreateRandomInput()
        self._CreateRandomButtons()
        self.randomNumOutput = ScrollLabel()
        self.generalLayout.addWidget(self.randomNumOutput)

        self._CreateIsPrimeHeader()
        isPrimeLayout = QHBoxLayout()
        isPrimeLayout.addLayout(self._CreateIsPrimeInput())
        isPrimeLayout.addLayout(self._CreateIsPrimeOutput())
        self.generalLayout.addLayout(isPrimeLayout)

# ------------- Range ---------------------------   
    def _CreateRangeHeader(self):
        self.rangeHeader = QLabel("Enter a number from 1 to 1000000")
        self.rangeHeader.setAlignment(Qt.AlignCenter)
        self.rangeHeader.setFont(QFont('Arial', 14))
        self.generalLayout.addWidget(self.rangeHeader)

    def _CreateRangeInput(self):
        self.rangeInput = QLineEdit()
        self.rangeInput.setFont(QFont('Arial', 14))
        self.rangeInput.setValidator(QIntValidator(1, 1000000))
        self.rangeInput.setFixedHeight(26)
        self.rangeInput.setAlignment(Qt.AlignLeft)
        self.rangeInput.setReadOnly(False)
        self.rangeInput.setClearButtonEnabled(True)
        self.rangeInput.setMaxLength(7)
        self.generalLayout.addWidget(self.rangeInput)

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
    
        self.generalLayout.addLayout(buttonLayout)

    def setRangeOutput(self, text):
        self.primeRangeOutput.setText(text)
        self.primeRangeOutput.setFocus()

    def getRangeOutput(self):
        return self.primeRangeOutput.text()

    def clearRangeOutput(self):
        self.setRangeOutput("")
# ------------------------------------------------------

# ------------- Random Nums ---------------------------   
    def _CreateRandomHeader(self):
        self.randomHeader = QLabel("Random Prime Numbers with Digit Length")
        self.randomHeader.setAlignment(Qt.AlignCenter)
        self.randomHeader.setFont(QFont('Arial', 14))
        self.generalLayout.addWidget(self.randomHeader)

    def _CreateRandomInput(self):
        randomLayout = QHBoxLayout()
        
        self.randomDigitLabel = QLabel("Amount of Digits (1-12)")
        self.randomDigitInput = QLineEdit()
        self.randomAmountLabel = QLabel("Amount of Numbers (1-50)")
        self.randomAmountInput = QLineEdit()

        self.randomDigitInput.setValidator(QIntValidator(1, 12))
        self.randomDigitInput.setFixedWidth(50)
        self.randomDigitInput.setClearButtonEnabled(True)
        self.randomDigitInput.setMaxLength(2)

        self.randomAmountInput.setValidator(QIntValidator(1, 12))
        self.randomAmountInput.setFixedWidth(50)
        self.randomAmountInput.setClearButtonEnabled(True)
        self.randomAmountInput.setMaxLength(2)

        randomLayout.addWidget(self.randomDigitLabel)
        randomLayout.addWidget(self.randomDigitInput)
        randomLayout.addWidget(self.randomAmountLabel)
        randomLayout.addWidget(self.randomAmountInput)

        self.generalLayout.addLayout(randomLayout)

    def _CreateRandomButtons(self):
        buttonLayout = QHBoxLayout()
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.randomGenButton = QPushButton("Generate")
        self.randomGenButton.setFixedSize(80, 26)
        buttonLayout.addWidget(self.randomGenButton, alignment=Qt.AlignCenter)

        self.randomGenCopy = QPushButton("Copy All")
        self.randomGenCopy.setFixedSize(70, 26)
        buttonLayout.addWidget(self.randomGenCopy, alignment=Qt.AlignCenter)

        self.randomGenClear = QPushButton("Clear")
        self.randomGenClear.setFixedSize(70, 26)
        buttonLayout.addWidget(self.randomGenClear, alignment=Qt.AlignCenter)
    
        self.generalLayout.addLayout(buttonLayout)

    def setRandomOutput(self, text):
        self.randomNumOutput.setText(text)
        self.randomNumOutput.setFocus()

    def getRandomOutput(self):
        return self.randomNumOutput.text()

    def clearRandomOutput(self):
        self.setRandomOutput("")
# ------------------------------------------------------
# ----------------- Is Prime ---------------------------  

    def _CreateIsPrimeHeader(self):
        self.isPrimeHeader = QLabel("Prime Number Validator")
        self.isPrimeHeader.setAlignment(Qt.AlignCenter)
        self.isPrimeHeader.setFont(QFont('Arial', 14))
        self.generalLayout.addWidget(self.isPrimeHeader)
    
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
        layout.addWidget(self.isPrimeLabel)
        layout.addWidget(self.isPrimeInput)
        layout.addWidget(self.isPrimeButton)
        return layout
    
    def _CreateIsPrimeOutput(self):
        layout = QHBoxLayout()
        self.isPrimeIcon = QSvgWidget()
        self.isPrimeText = QLabel()
        layout.addWidget(self.isPrimeIcon)
        layout.addWidget(self.isPrimeText)
        return layout
