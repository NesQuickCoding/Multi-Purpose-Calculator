import re

class BaseConvCtrl:
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _convert(self):
        pass

    def _decChanged(self):
        # Splits at anything not a 0-9 digit into a list
        decValidator = re.split(r"[^0-9]+", self._view.dec.decTextBox.document().toPlainText())
        # Joins to create one number again
        validDecNumber = ''.join(decValidator)
        # Format number to have thousand comma separator
        try:
            validDecNumber = f"{int(validDecNumber):,}"
        except ValueError:
            pass
        
        # Disconnect signal to prevent an infinite loop with textChanged signal
        # then setPlainText and connect signal again
        self._view.dec.decTextBox.textChanged.disconnect()
        self._view.dec.decTextBox.document().setPlainText(validDecNumber)
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        
        # self._view.hex.hexTextBox.document().setPlainText(validDecNumber)
        # self._view.bin.binTextBox.document().setPlainText(validDecNumber)
    
    def _hexChanged(self):
        hexValidator = re.split(r"[^0-9a-fA-F]+", self._view.hex.hexTextBox.document().toPlainText())
        validHexNumber = ''.join(hexValidator).upper()
        print(validHexNumber)

    def _connectSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        self._view.hex.hexTextBox.textChanged.connect(lambda: self._hexChanged())
