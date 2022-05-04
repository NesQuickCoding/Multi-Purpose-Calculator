import re

class BaseConvCtrl:
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _convert(self):
        pass

    def _decChanged(self):
        # Splits at anything not a 0-9 digit into a list
        decValidator = re.split("[^0-9]+", self._view.dec.decTextBox.document().toPlainText())
        # Joins to create one number again
        validDecNumber = ''.join(decValidator)
        self._view.dec.decTextBox.document().setPlainText(validDecNumber)
        self._view.hex.hexTextBox.document().setPlainText(validDecNumber)
        self._view.bin.binTextBox.document().setPlainText(validDecNumber)
    
    def _connectSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
