class BaseConvCtrl:
    def __init__(self, view, model):
        self._view = view
        self._connectTextSignals()
        self._bitSignals()
        self._model = model
        self._bitLimits = [
            # unsigned, signed
            (18446744073709551615, 9223372036854775807),  #64-bit
            (4294967295, 2147483647),                     #32-bit
            (65535, 32767),                               #16-bit
            (255, 127)                                    #8-bit
        ]
        self._signed = 0

    def _decChanged(self):
        validDecNumber = self._model.decValidator(self._view.dec.decTextBox.document().toPlainText(), self._bitLimits[self._view.bitDropBox.currentIndex()][self._signed])
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
        self._disconnectTextSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectTextSignals()
    
    def _hexChanged(self):
        validHexNumber = self._model.hexValidator(self._view.hex.hexTextBox.document().toPlainText())
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        try:
            decOutput = self._model.decFormatter(f"{int(validHexNumber, 16)}")
            hexOutput = self._model.hexFormatter(f"{hex(int(validHexNumber, 16))[2:]}")
            binOutput = self._model.binFormatter(f"{bin(int(validHexNumber, 16))[2:]}")
        except ValueError:
            pass
        self._disconnectTextSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectTextSignals()

    def _binChanged(self):
        validBinNumber = self._model.binValidator(self._view.bin.binTextBox.document().toPlainText())
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        
        try:
            decOutput = self._model.decFormatter(f"{int(validBinNumber, 2)}")
            hexOutput = self._model.hexFormatter(f"{hex(int(validBinNumber, 2))[2:]}")
            binOutput = self._model.binFormatter(f"{bin(int(validBinNumber, 2))[2:]}")
        except ValueError:
            pass

        self._disconnectTextSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectTextSignals()

    def _setBitIndex(self):
        self._decChanged()

    def _setSigned(self):
        if self._view.unSignedRadio.isChecked():
            self._signed = 0
        elif self._view.signedRadio.isChecked():
            self._signed = 1
        self._decChanged()

    def _connectTextSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        self._view.hex.hexTextBox.textChanged.connect(lambda: self._hexChanged())
        self._view.bin.binTextBox.textChanged.connect(lambda: self._binChanged())
    
    def _disconnectTextSignals(self):
        self._view.dec.decTextBox.textChanged.disconnect()
        self._view.hex.hexTextBox.textChanged.disconnect()
        self._view.bin.binTextBox.textChanged.disconnect()
    
    def _bitSignals(self):
        self._view.bitDropBox.currentIndexChanged.connect(self._setBitIndex)
        self._view.unSignedRadio.toggled.connect(self._setSigned)
