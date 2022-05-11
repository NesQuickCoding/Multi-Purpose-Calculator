from PyQt5.QtWidgets import QWidget, QScrollArea, QLabel, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QRegExp

class ScrollLabel(QScrollArea):
    """
    Custom setup of a QScrollArea to create a read-only Scroll Label for Prime Gen Output

    Inherits all methods and attributes from QScrollArea

    Attributes
    ----------
    label : QLabel
        Stores the text content of the object
    
    Methods
    -------
    setText(text):
        Changes label's text with text
    text()
        Returns label's text
    """
    def __init__(self):
        """
        Construct A ScrollLabel with certain properties

        Parameters
        ----------
        label : QLabel
            Used to store text for the ScrollArea
        
        Returns
        -------
        ScrollArea
            Newly constructed widget
        """
        super().__init__()
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        layout = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setObjectName("scrollLabel")
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(self.label)
    
    def setText(self, text):
        """
        Sets the text of label

        Parameters
        ----------
        text : str
            Input for the label to change to
        
        Returns
        -------
        None
        """
        self.label.setText(text)
    
    def text(self):
        """
        Returns the string of label's text

        Parameters
        ----------
        None

        Returns
        -------
        str
            Label's text
        """
        return self.label.text()

class PrimeRangeGen(QWidget):
    """
    Creates a Prime Number Generator QWidget that generates based on the range
    from 1 to a user inputted positive integer

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    rangeHeader : QLabel
        Text header
    rangeInput : QLineEdit
        Text input field
    rangeGenButton : QPushButton
        Submit button to generate input
    rangeGenCopy : QPushButton
        Copys results to clipboard
    rangeGenClear : QPushButton
        Clears output text
    primeRangeOutput : ScrollLabel
        Scroll label for output
    
    Methods
    -------
    _CreateRangeHeader():
        Creates a QLabel object for the rangeHeader
    _CreateRangeInput():
        Creates a QLineEdit object with validators and other settings
    _CreateRangeButtons(self):
        Creates a layout of QPushButtons for input
    setRangeOutput(text):
        Changes the output text of primeRangeOutput
    getRangeOutput():
        Returns the output text of primeRangeOutput
    clearRangeOutput():
        Clears the output text of primeRangeOutput
    """
    def __init__(self):
        """
        Initilizer for PrimeRangeGen

        Parameters
        ----------
        None
        
        Returns
        -------
        PrimeRangeGen
            Newly constructed widget
        """
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
        """
        Creates a QLabel text with instruction limits

        Parameters
        ----------
        None

        Returns
        -------
        QLabel
            Header/instructional text
        """
        header = QLabel("Generate prime numbers from 1 to n (limit 1000000)")
        header.setObjectName("primeHeader")
        header.setWordWrap(True)
        header.setAlignment(Qt.AlignCenter)
        return header

    def _CreateRangeInput(self):
        """
        Creates a QLineEdit input field

        Parameters
        ----------
        None

        Returns
        -------
        QLineEdit
            primeRangeInput field
        """
        inputWidget = QLineEdit()
        inputWidget.setValidator(QIntValidator(1, 1000000))
        inputWidget.setAlignment(Qt.AlignLeft)
        inputWidget.setReadOnly(False)
        inputWidget.setClearButtonEnabled(True)
        inputWidget.setMaxLength(7)
        return inputWidget

    def _CreateRangeButtons(self):
        """
        Creates a QHBoxLayout of various QPushButtons

        Parameters
        ----------
        None

        Returns
        -------
        QHBoxLayout
            Layout with Genereate, Copy All, and Clear buttons
        """
        buttonLayout = QHBoxLayout()
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.rangeGenButton = QPushButton("Generate")
        self.rangeGenButton.setObjectName("primeGenButton")
        buttonLayout.addWidget(self.rangeGenButton, alignment=Qt.AlignCenter)

        self.rangeGenCopy = QPushButton("Copy All")
        self.rangeGenCopy.setObjectName("primeCopyButton")
        buttonLayout.addWidget(self.rangeGenCopy, alignment=Qt.AlignCenter)

        self.rangeGenClear = QPushButton("Clear")
        self.rangeGenClear.setObjectName("primeClearButton")
        buttonLayout.addWidget(self.rangeGenClear, alignment=Qt.AlignCenter)
    
        return buttonLayout

    def setRangeOutput(self, text):
        """
        Changes the text of primeRangeGenOutput

        Parameters
        ----------
        text : str
            input of new text

        Returns
        -------
        None
        """
        self.primeRangeOutput.setText(text)
        self.primeRangeOutput.setFocus()

    def getRangeOutput(self):
        """
        Returns primeRangeGenOutput's text

        Parameters
        ----------
        None

        Returns
        -------
        str
            primeRangeOutput's text
        """
        return self.primeRangeOutput.text()

    def clearRangeOutput(self):
        """
        Changes the text of primeRangeGenOutput to an empty string

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.setRangeOutput("")

class PrimeRandomGen(QWidget):
    """
    Creates a Prime Number Generator QWidget that generates a specificied amount of
    random prime numbers with a specificied number of digits from user input

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    randomHeader : QLabel
        Text header
    randomDigitLabel : QLabel
        label for Digit Input
    randomAmountLabel : QLabel
        label for Amount of numbers input
    randomDigitInput : QLineEdit
        text input for number of digits
    randomAmountInput : QLineEdit
        text input for how many random numbers
    randomGenButton : QPushButton
        Submit button
    randomGenCopy : QPushButton
        Copies output to clipboard
    randomGenClear : QPushButton
        Clears output text
    randomNumOutput : ScrollLabel
        Scroll label for output
    
    Methods
    -------
    _CreateRandomHeader():
        Creates a QLabel object for the randomHeader
    _CreateRandpomInput():
        Creates a various QLineEdit object with validators and other settings
    _CreateRandomButtons():
        Creates a layout of QPushButtons for input
    setRandomOutput(text):
        Changes the output text of randomNumOutput
    getRandomOutput():
        Returns the output text of randomNumOutput
    clearRandomOutput():
        Clears the output text of randomNumOutput
    """
    def __init__(self):
        """
        Initilizer for PrimeRandomGen

        Parameters
        ----------
        None
        
        Returns
        -------
        PrimeRandomGen
            Newly constructed widget
        """
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
        """
        Creates a QLabel text header

        Parameters
        ----------
        None

        Returns
        -------
        QLabel
            Header text
        """
        header = QLabel("Random Prime Numbers with Digit Length")
        header.setWordWrap(True)
        header.setObjectName("primeHeader")
        header.setAlignment(Qt.AlignCenter)
        return header

    def _CreateRandomInput(self):
        """
        Creates a layout with QLineEdit input text fields with instructions

        Parameters
        ----------
        None

        Returns
        -------
        QHBoxLayout
            Layout of text input fields
        """
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
        self.randomDigitInput.setClearButtonEnabled(True)
        self.randomDigitInput.setMaxLength(2)

        self.randomAmountInput.setValidator(QIntValidator(1, 12))
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
        """
        Creates a QHBoxLayout of various QPushButtons

        Parameters
        ----------
        None

        Returns
        -------
        QHBoxLayout
            Layout with Genereate, Copy All, and Clear buttons
        """
        buttonLayout = QHBoxLayout()
        buttonLayout.setAlignment(Qt.AlignCenter)

        self.randomGenButton = QPushButton("Generate")
        self.randomGenButton.setObjectName("primeGenButton")
        buttonLayout.addWidget(self.randomGenButton, alignment=Qt.AlignCenter)

        self.randomGenCopy = QPushButton("Copy All")
        self.randomGenCopy.setObjectName("primeCopyButton")
        buttonLayout.addWidget(self.randomGenCopy, alignment=Qt.AlignCenter)

        self.randomGenClear = QPushButton("Clear")
        self.randomGenClear.setObjectName("primeClearButton")
        buttonLayout.addWidget(self.randomGenClear, alignment=Qt.AlignCenter)
    
        return buttonLayout

    def setRandomOutput(self, text):
        """
        Changes the text of randomNumOutput

        Parameters
        ----------
        text : str
            input of new text

        Returns
        -------
        None
        """
        self.randomNumOutput.setText(text)
        self.randomNumOutput.setFocus()

    def getRandomOutput(self):
        """
        Returns randomNumOutput's text

        Parameters
        ----------
        None

        Returns
        -------
        str
            randomNumOutput's text
        """
        return self.randomNumOutput.text()

    def clearRandomOutput(self):
        """
        Changes the text of randomNumOutput to an empty string

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.setRandomOutput("")

class IsPrime(QWidget):
    """
    Creates a QWidget that determines if a number is prime or now

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    isPrimeHeader : QLabel
        Text header
    isPrimeLabel : QLabel
        Instructional text for isPrime widget
    isPrimeInput : QLineEdit
        input box for isPrime
    isPrimeButton : QPushButton
        Text input field
    isPrimeIcon : QSvgWidget
        SVG Image to show if a number is prime or not
    isPrimeText : QLabel
        Text confirming if a number is prime or not
    primeRangeOutput : ScrollLabel
        Scroll label for output
    
    Methods
    -------
    _CreateIsPrimeHeader():
        Creates a QLabel object for the isPrimeHeader
    _CreateIsPrimeInput():
        Creates a a layout and isPrimeLabel, isPrimeInput, and isPrimeButton
    _CreateIsPrimeOutput()):
        Creates a layout of QPushButtons for input
    """
    def __init__(self):
        """
        Initilizer for isPrime

        Parameters
        ----------
        None
        
        Returns
        -------
        isPrime
            Newly constructed widget
        """
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
        """
        Creates a QLabel text header

        Parameters
        ----------
        None

        Returns
        -------
        QLabel
            Header text
        """
        header = QLabel("Prime Number Validator")
        header.setAlignment(Qt.AlignCenter)
        return header
    
    def _CreateIsPrimeInput(self):
        """
        Creates a layout with QLabel, QLineEdit, and QPushButton for isPrime

        Parameters
        ----------
        None

        Returns
        -------
        QVBoxLayout
            Layout of input and submit widgets
        """
        layout = QVBoxLayout()
        self.isPrimeLabel = QLabel("Enter a number")
        self.isPrimeInput = QLineEdit()
        self.isPrimeInput.setAlignment(Qt.AlignLeft)
        self.isPrimeInput.setClearButtonEnabled(True)
        self.isPrimeInput.setValidator(QRegExpValidator(QRegExp("[0-9]{16}")))
        self.isPrimeButton = QPushButton("Check")
        layout.addWidget(self.isPrimeLabel)
        layout.addWidget(self.isPrimeInput)
        layout.addWidget(self.isPrimeButton)
        return layout
    
    def _CreateIsPrimeOutput(self):
        """
        Creates a QVBoxLayout with widgets for output results

        Parameters
        ----------
        None

        Returns
        -------
        QVBoxLayout
            Layout with Icon and Text
        """
        layout = QVBoxLayout()
        self.isPrimeIcon = QSvgWidget()
        self.isPrimeIcon.setStyleSheet("text-align: center;")
        self.isPrimeText = QLabel()
        self.isPrimeText.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.isPrimeIcon, 0, Qt.AlignCenter)
        layout.addWidget(self.isPrimeText, 0, Qt.AlignCenter)
        return layout

class PrimeGenUI(QWidget):
    """
    Creates the core Prime Gen UI. Creates a tabs window, with each item being a
    PrimeRangeGen widget, PrimeRandomGen widget, and IsPrime widget.

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    tabs : QTabWidget
        Tabs containing all the widgets
    primeRangeGen : PrimeRangeGen
        Creates PrimeRangeGen View
    primeRandomGen : PrimeRandomGen
        Creates PrimeRandomGen view
    isPrime : IsPrime
        Creates IsPrime view
    
    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initilizer for PrimeGenUI. Creates Tab window with all three prime gen widgets

        Parameters
        ----------
        None
        
        Returns
        -------
        IsPrime
            Newly constructed widget
        """
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
