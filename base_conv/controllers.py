class BaseConvCtrl:
    def __init__(self, view, model):
        self._view = view
        self._connectSignals()
        self._model = model

    def _decChanged(self):
        validDecNumber = self._model.decValidator(self._view.dec.decTextBox.document().toPlainText())
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        try:
            decOutput = self._model.decFormatter(validDecNumber)
            hexOutput = self._model.hexFormatter(f"{hex(int(validDecNumber))[2:]}")
            binOutput = self._model.binFormatter(f"{bin(int(validDecNumber))[2:]}")
        except ValueError:
            pass

        # Disconnect signal to prevent an infinite loop with textChanged signal
        # then setPlainText and connect signal again
        self._disconnectSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectSignals()
    
    def _hexChanged(self):
        validHexNumber = self._model.hexValidator(self._view.hex.hexTextBox.document().toPlainText())
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        try:
            decOutput = self._model.decFormatter(f"{int(validHexNumber, 16)}")
            hexOutput = self._model.hexFormatter(validHexNumber)
            binOutput = self._model.binFormatter(f"{bin(int(validHexNumber, 16))[2:]}")
        except ValueError:
            pass
        self._disconnectSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectSignals()

    def _binChanged(self):
        validBinNumber = self._model.binValidator(self._view.bin.binTextBox.document().toPlainText())
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        
        try:
            decOutput = self._model.decFormatter(f"{int(validBinNumber, 2)}")
            hexOutput = self._model.hexFormatter(f"{hex(int(validBinNumber, 2))[2:]}")
            binOutput = self._model.binFormatter(validBinNumber)
        except ValueError:
            pass

        self._disconnectSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectSignals()

    def _connectSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        self._view.hex.hexTextBox.textChanged.connect(lambda: self._hexChanged())
        self._view.bin.binTextBox.textChanged.connect(lambda: self._binChanged())
    
    def _disconnectSignals(self):
        self._view.dec.decTextBox.textChanged.disconnect()
        self._view.hex.hexTextBox.textChanged.disconnect()
        self._view.bin.binTextBox.textChanged.disconnect()
