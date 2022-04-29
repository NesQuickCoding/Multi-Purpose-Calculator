from PyQt5.QtWidgets import QApplication

from functools import partial

class PrimeGenControl:
    def __init__(self, view, model):
        self._view = view
        self._rangeGen = model.range_1_n
        self._randomGen = model.digit_size
        self._connectRangeSignals()
 #------
    def _generateRange(self):
        if self._view.rangeInput.text():
            self._view.setRangeOutput("Calculating....")
            self._view.setRangeOutput(str(self._rangeGen(int(self._view.rangeInput.text())))[1:-1])
        else:
            self._view.setRangeOutput("Please enter a value")
    
    def _copyRange(self):
        QApplication.clipboard().setText(self._view.getRangeOutput())
    
    def _checkInputBounds(self, inputLabel, minValue, maxValue):
        if inputLabel.text():
            if int(inputLabel.text()) == minValue:
                inputLabel.setText('')
            elif int(inputLabel.text()) > maxValue:
                inputLabel.setText(f"{maxValue}")
#------
    def _generateRandom(self):
        if self._view.randomDigitInput.text() and self._view.randomAmountInput.text():
            self._view.setRandomOutput("Calculating....")
            self._view.setRandomOutput(str(self._randomGen(int(self._view.randomDigitInput.text()), int(self._view.randomAmountInput.text())))[1:-1])
        else:
            self._view.setRandomOutput("Please enter a value for digit length and amount of numbers")

    def _connectRangeSignals(self):
        self._view.rangeInput.textChanged.connect(partial(self._checkInputBounds, self._view.rangeInput, 0, 1000000))
        self._view.rangeGenButton.clicked.connect(self._generateRange)
        self._view.rangeGenCopy.clicked.connect(self._copyRange)
        self._view.rangeGenClear.clicked.connect(self._view.clearRangeOutput)
        # ----
        self._view.randomDigitInput.textChanged.connect(partial(self._checkInputBounds, self._view.randomDigitInput, 0, 12))
        self._view.randomAmountInput.textChanged.connect(partial(self._checkInputBounds, self._view.randomAmountInput, 0, 50))
        self._view.randomGenButton.clicked.connect(self._generateRandom)
