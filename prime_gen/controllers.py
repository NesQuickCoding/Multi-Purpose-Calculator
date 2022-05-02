from PyQt5.QtWidgets import QApplication

from functools import partial

class PrimeGenControl:
    def __init__(self, view, model):
        self._view = view
        self._rangeGen = model.range_1_n
        self._randomGen = model.digit_size
        self._isPrime = model.is_prime
        self._connectRangeSignals()
        
    def _copyAll(self, getFunction):
        QApplication.clipboard().setText(getFunction())
    
    def _checkInputBounds(self, inputLabel, minValue, maxValue):
        if inputLabel.text():
            if int(inputLabel.text()) == minValue:
                inputLabel.setText('')
            elif int(inputLabel.text()) > maxValue:
                inputLabel.setText(str(maxValue))
    
    # --- Models for primeRangeGen ---
    def _generateRange(self):
        if self._view.primeRangeGen.rangeInput.text():
            self._view.primeRangeGen.setRangeOutput("Calculating....")
            self._view.primeRangeGen.setRangeOutput(str(self._rangeGen(int(self._view.primeRangeGen.rangeInput.text())))[1:-1])
        else:
            self._view.primeRangeGen.setRangeOutput("Please enter a value")
    
    # --- Models for primeRandomGen ---
    def _generateRandom(self):
        if self._view.primeRandomGen.randomDigitInput.text() and self._view.primeRandomGen.randomAmountInput.text():
            self._view.primeRandomGen.setRandomOutput("Calculating....")
            self._view.primeRandomGen.setRandomOutput(str(self._randomGen(int(self._view.primeRandomGen.randomDigitInput.text()), int(self._view.primeRandomGen.randomAmountInput.text())))[1:-1])
        else:
            self._view.primeRandomGen.setRandomOutput("Please enter a value for digit length and amount of numbers")
    
    # --- Models for isPrime ---
    def _IsPrimeCheck(self):
        if self._view.isPrime.isPrimeInput.text():
            if self._isPrime(int(self._view.isPrime.isPrimeInput.text())):
                self._view.isPrime.isPrimeIcon.renderer().load("assets/check.svg")
                self._view.isPrime.isPrimeText.setText("Is Prime!")
            else:
                self._view.isPrime.isPrimeIcon.renderer().load("assets/cancel.svg")
                self._view.isPrime.isPrimeText.setText("Is Not Prime!")
        else:
            self._view.isPrime.isPrimeText.setText("Enter A\nNumber")
    
    def _clearIcon(self):
        self._view.isPrime.isPrimeIcon.renderer().load('')
        self._view.isPrime.isPrimeText.setText('')

    # --- Signal Connection ---
    def _connectRangeSignals(self):
        # --- primeRangeGen Signals ---
        self._view.primeRangeGen.rangeInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRangeGen.rangeInput, 0, 1000000))
        self._view.primeRangeGen.rangeGenButton.clicked.connect(self._generateRange)
        self._view.primeRangeGen.rangeGenCopy.clicked.connect(partial(self._copyAll, self._view.primeRangeGen.getRangeOutput))
        self._view.primeRangeGen.rangeGenClear.clicked.connect(self._view.primeRangeGen.clearRangeOutput)
        # --- primeRandomGen Signals ---
        self._view.primeRandomGen.randomDigitInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRandomGen.randomDigitInput, 0, 12))
        self._view.primeRandomGen.randomAmountInput.textChanged.connect(partial(self._checkInputBounds, self._view.primeRandomGen.randomAmountInput, 0, 50))
        self._view.primeRandomGen.randomGenButton.clicked.connect(self._generateRandom)
        self._view.primeRandomGen.randomGenCopy.clicked.connect(partial(self._copyAll, self._view.primeRandomGen.getRandomOutput))
        self._view.primeRandomGen.randomGenClear.clicked.connect(self._view.primeRandomGen.clearRandomOutput)
        # --- isPrime Signals ---
        self._view.isPrime.isPrimeInput.textChanged.connect(partial(self._checkInputBounds, self._view.isPrime.isPrimeInput, 0, 9999999999999999))
        self._view.isPrime.isPrimeInput.textChanged.connect(self._clearIcon)
        self._view.isPrime.isPrimeButton.clicked.connect(self._IsPrimeCheck)
