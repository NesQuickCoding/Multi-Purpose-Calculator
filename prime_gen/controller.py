from PyQt5.QtWidgets import QApplication

from functools import partial

class PrimeGenControl:
    def __init__(self, view, model):
        self._view = view
        self._rangeGen = model.range_1_n
        self._randomGen = model.digit_size
        self._isPrime = model.is_prime
        self._connectRangeSignals()
 #------
    def _generateRange(self):
        if self._view.rangeInput.text():
            self._view.setRangeOutput("Calculating....")
            self._view.setRangeOutput(str(self._rangeGen(int(self._view.rangeInput.text())))[1:-1])
        else:
            self._view.setRangeOutput("Please enter a value")
    
    def _copyAll(self, getFunction):
        QApplication.clipboard().setText(getFunction())
    
    def _checkInputBounds(self, inputLabel, minValue, maxValue):
        if inputLabel.text():
            if int(inputLabel.text()) == minValue:
                inputLabel.setText('')
            elif int(inputLabel.text()) > maxValue:
                inputLabel.setText(str(maxValue))
#------
    def _generateRandom(self):
        if self._view.randomDigitInput.text() and self._view.randomAmountInput.text():
            self._view.setRandomOutput("Calculating....")
            self._view.setRandomOutput(str(self._randomGen(int(self._view.randomDigitInput.text()), int(self._view.randomAmountInput.text())))[1:-1])
        else:
            self._view.setRandomOutput("Please enter a value for digit length and amount of numbers")
#------
    def _IsPrimeCheck(self):
        if self._view.isPrimeInput.text():
            if self._isPrime(int(self._view.isPrimeInput.text())):
                self._view.isPrimeIcon.renderer().load("assets/check.svg")
                self._view.isPrimeText.setText("Is Prime!")
            else:
                self._view.isPrimeIcon.renderer().load("assets/cancel.svg")
                self._view.isPrimeText.setText("Is Not Prime!")
        else:
            self._view.isPrimeText.setText("Please enter a value")

#------
    def _connectRangeSignals(self):
        self._view.rangeInput.textChanged.connect(partial(self._checkInputBounds, self._view.rangeInput, 0, 1000000))
        self._view.rangeGenButton.clicked.connect(self._generateRange)
        self._view.rangeGenCopy.clicked.connect(partial(self._copyAll, self._view.getRangeOutput))
        self._view.rangeGenClear.clicked.connect(self._view.clearRangeOutput)
        # ----
        self._view.randomDigitInput.textChanged.connect(partial(self._checkInputBounds, self._view.randomDigitInput, 0, 12))
        self._view.randomAmountInput.textChanged.connect(partial(self._checkInputBounds, self._view.randomAmountInput, 0, 50))
        self._view.randomGenButton.clicked.connect(self._generateRandom)
        self._view.randomGenCopy.clicked.connect(partial(self._copyAll, self._view.getRandomOutput))
        self._view.randomGenClear.clicked.connect(self._view.clearRandomOutput)
        # ----
        self._view.isPrimeInput.textChanged.connect(partial(self._checkInputBounds, self._view.isPrimeInput, 0, 9999999999999999))
        self._view.isPrimeButton.clicked.connect(self._IsPrimeCheck)
