from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator

from PyQt5.QtCore import Qt
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

        self._CreateHeader()
        self._CreateRangeInput()
        self._CreateRangeButtons()
        self.primeRangeOutput = ScrollLabel()
        self.generalLayout.addWidget(self.primeRangeOutput)
    
    def _CreateHeader(self):
        self.header = QLabel("Enter a number from 1 to 1000000")
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setFont(QFont('Arial', 14))
        self.generalLayout.addWidget(self.header)

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

        self.rangeGenCopy = QPushButton("Copy")
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
