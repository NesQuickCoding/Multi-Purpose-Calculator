from PyQt5.QtWidgets import QApplication

class PrimeGenControl:
    def __init__(self, view, model):
        self._view = view
        self._rangeGen = model.range_1_n
        self._connectRangeSignals()
 
    def _generateRange(self):
        if self._view.rangeInput.text():
            self._view.setRangeOutput("Calculating....")
            self._view.setRangeOutput(str(self._rangeGen(int(self._view.rangeInput.text())))[1:-1])
        else:
            self._view.setRangeOutput("Please enter a value")
    
    def _copyRange(self):
        QApplication.clipboard().setText(self._view.getRangeOutput())
    
    def _checkRangeInput(self):
        if self._view.rangeInput.text():
            if int(self._view.rangeInput.text()) == 0:
                self._view.rangeInput.setText('')
            elif int(self._view.rangeInput.text()) > 1000000:
                self._view.rangeInput.setText('1000000')

    def _connectRangeSignals(self):
        self._view.rangeInput.textChanged.connect(self._checkRangeInput)
        self._view.rangeGenButton.clicked.connect(self._generateRange)
        self._view.rangeGenCopy.clicked.connect(self._copyRange)
        self._view.rangeGenClear.clicked.connect(self._view.clearRangeOutput)
