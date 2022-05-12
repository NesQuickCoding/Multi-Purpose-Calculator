from PyQt5.QtWidgets import QApplication
from functools import partial


class PrimeGenCtrl:
    """
    Handles the logic and signal connections for the PrimeGenUI
    
    Attributes
    ----------
    _view : PrimeGenUI
        Stores the reference to the QWidget of PrimeGenUI
    _rangeGen : function
        Stores the reference to the range_1_n function in prime_gen/models.py
    _randomGen : function
        Stores the reference to the digit_size function in prime_gen/models.py
    _isPrime : function
        Stores the reference to the is_prime function in prime_gen/models.py

    Methods
    -------
    _copyAll(getFunction):
        Copys the text provided from the passed funtion in getFunction
    _checkInputBounds(inputLabel, minValue, maxValue):
        Checks the range of inputLabel.text() and modifies based on the minValue and maxValue
    _generateRange():
        Generates range based on rangeInput.text()
    _generateRandom():
        Generates random number based on randomDigitiInput.text() and randomAmountInput.text()
    _IsPrimeCheck():
        Checks if a number is prime based on on isPrimeInput.text()
    _clearIcon():
        Clears the file path for the SVG icon
    _connectSignals():
        Connects the signals for the QLineEdit and QPushButtons for all three Prime Gen Modes
    """
    def __init__(self, view, model):
        """
        Constructs the PrimeGenCtrl, building signals for PrimeGenUI and connecting
        them to the correct model/function for conversion calculations

        Parameters
        ----------
        view : PrimeGenUI
            Used to reference and connect PrimeGenUI's attributes
        model : module
            Reference to prime_gen/models.py, containing the generation/validation functions

        Returns
        -------
        PrimeGenCtrl
            Connects PrimeGenUI to the appropriate signals
        """
        self._view = view
        self._rangeGen = model.range_1_n
        self._randomGen = model.digit_size
        self._isPrime = model.is_prime
        self._connectSignals()
        
    def _copyAll(self, getFunction):
        """
        Copys the text return by the passed getFunction for an output field

        Parameters
        ----------
        getFunction : function
            the function that will return its respective get for an output value
        
        Returns
        -------
        None
        """
        QApplication.clipboard().setText(getFunction())
    
    def _checkInputBounds(self, inputLabel, minValue, maxValue):
        """
        Checks to see if the value of int(inputLabel.text()) is between minValue and maxValue
        Changes to empty string if it's lower than min, and to maxValue if higher than maxValue
        Then sets inputLabel's text if it is out of those bounds

        Parameters
        ----------
        inputLabel : QLabel
            QLabel of the respective input field
        minValue : int
            minumum value to validate the range
        maxValue : int
            maximum value to validate the range
        
        Returns
        -------
        None
        """
        if inputLabel.text():
            if int(inputLabel.text()) == minValue:
                inputLabel.setText('')
            elif int(inputLabel.text()) > maxValue:
                inputLabel.setText(str(maxValue))
    
    def _generateRange(self):
        """
        Calculates the prime numbers in a range from rangeInput.text()
        Then sets rangeOutput's text to the results
        Sets to "Please enter a value" if rangeInput.text() is empty

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        if self._view.primeRangeGen.rangeInput.text():
            self._view.primeRangeGen.setRangeOutput("Calculating....")
            self._view.primeRangeGen.setRangeOutput(str(self._rangeGen(int(self._view.primeRangeGen.rangeInput.text())))[1:-1])
        else:
            self._view.primeRangeGen.setRangeOutput("Please enter a value")
    
    def _generateRandom(self):
        """
        Calculates random prime numbers from randomDigitInput and randomAmountInput
        Then sets randomOutput's text to the results
        Sets to "Please enter a value" if either input is empty

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        if self._view.primeRandomGen.randomDigitInput.text() and self._view.primeRandomGen.randomAmountInput.text():
            self._view.primeRandomGen.setRandomOutput("Calculating....")
            self._view.primeRandomGen.setRandomOutput(str(self._randomGen(int(self._view.primeRandomGen.randomDigitInput.text()), int(self._view.primeRandomGen.randomAmountInput.text())))[1:-1])
        else:
            self._view.primeRandomGen.setRandomOutput("Please enter a value for digit length and amount of numbers")
    
    def _IsPrimeCheck(self):
        """
        Validates if a isPrime.text() is in fact a prime number, then outputs the results
        with an SVG image and text
        If input is empty, then the text asks for you to input a number

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        if self._view.isPrime.isPrimeInput.text():
            if self._isPrime(int(self._view.isPrime.isPrimeInput.text())):
                self._view.isPrime.pixLabel.setPixmap(self._view.isPrime.isPrimeIcon)
                self._view.isPrime.pixLabel.resize(self._view.isPrime.isPrimeIcon.width(), self._view.isPrime.isPrimeIcon.height())
                self._view.isPrime.isPrimeText.setText("Is Prime!")
            else:
                self._view.isPrime.pixLabel.setPixmap(self._view.isPrime.isNotPrimeIcon)
                self._view.isPrime.pixLabel.resize(self._view.isPrime.isNotPrimeIcon.width(), self._view.isPrime.isNotPrimeIcon.height())
                self._view.isPrime.isPrimeText.setText("Is Not Prime!")
    
    def _clearIcon(self):
        """
        Clears the output results of isPrime, setting the image and text to empty

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self._view.isPrime.pixLabel.setPixmap(self._view.isPrime.isPrimeIcon.scaled(0, 0))
        self._view.isPrime.pixLabel.resize(0, 0)
        self._view.isPrime.isPrimeText.setText('')

    def _connectSignals(self):
        """
        Connects the various signals for primeRangeGen, primeRandomGen, and isPrime
        Performs checkInputBounds for all input.textChanged
        Performs their respective calculation on Button.clicked
        Performs copying of output from Copy.clicked
        Clear respective output from Clear.clicked

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        # --- primeRangeGen Signals ---
        self._view.primeRangeGen.rangeInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRangeGen.rangeInput, 0, 1000000))
        self._view.primeRangeGen.rangeGenButton.clicked.connect(self._generateRange)
        self._view.primeRangeGen.rangeGenCopy.clicked.connect(partial(self._copyAll, self._view.primeRangeGen.getRangeOutput))
        self._view.primeRangeGen.rangeGenClear.clicked.connect(self._view.primeRangeGen.clearRangeOutput)
        # # --- primeRandomGen Signals ---
        self._view.primeRandomGen.randomDigitInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRandomGen.randomDigitInput, 0, 12))
        self._view.primeRandomGen.randomAmountInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRandomGen.randomAmountInput, 0, 50))
        self._view.primeRandomGen.randomGenButton.clicked.connect(self._generateRandom)
        self._view.primeRandomGen.randomGenCopy.clicked.connect(partial(self._copyAll, self._view.primeRandomGen.getRandomOutput))
        self._view.primeRandomGen.randomGenClear.clicked.connect(self._view.primeRandomGen.clearRandomOutput)
        # # --- isPrime Signals ---
        self._view.isPrime.isPrimeInput.textChanged.connect(partial(self._checkInputBounds, self._view.isPrime.isPrimeInput, 0, 9999999999999999))
        self._view.isPrime.isPrimeInput.textChanged.connect(self._clearIcon)
        self._view.isPrime.isPrimeButton.clicked.connect(self._IsPrimeCheck)
