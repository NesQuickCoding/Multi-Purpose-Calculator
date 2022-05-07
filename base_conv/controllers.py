class BaseConvCtrl:
    def __init__(self, view, model):
        self._view = view
        self._connectTextSignals()
        self._connectBitSignals()
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
        # Validate input for decimal text field
        # shorthand - validBaseNumber = baseValidator(baseTextBox's text, bit-width and signage numerical limit, signed/unsigned mode)
        validDecNumber = self._model.decValidator(self._view.dec.decTextBox.document().toPlainText(), self._bitLimits[self._view.bitDropBox.currentIndex()][self._signed], self._signed)
        
        # Format the output for each field
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        try:
            decOutput = self._model.decFormatter(validDecNumber)
            # First argument is converts the string to hex/dec, and trims 0x/0b after it's conversion
            # Trims differently based on a conditional if the number is negative or positive
            # Second argument is the bit-width, based on the dropbox index value
            hexOutput = self._model.hexFormatter(f"{hex(int(validDecNumber))[2:]}" if int(validDecNumber) >= 0 else f"-{hex(int(validDecNumber))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
            binOutput = self._model.binFormatter(f"{bin(int(validDecNumber))[2:]}" if int(validDecNumber) >= 0 else f"-{bin(int(validDecNumber))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
        except ValueError:
            pass

        # Disconnect signals to prevent an infinite loop with textChanged signal
        # then setPlainText and connect signal again
        self._setAllTextBoxes(decOutput, hexOutput, binOutput)

    def _hexChanged(self):
        validHexNumber = self._model.hexValidator(self._view.hex.hexTextBox.document().toPlainText(), self._bitLimits[self._view.bitDropBox.currentIndex()][0], self._signed)
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        
        try:
            if self._signed:
                decOutput = self._model.decFormatter(str(self._model.signedBaseToInt(int(validHexNumber, 16), 64 // (2**self._view.bitDropBox.currentIndex()))))
            else:
                decOutput = self._model.decFormatter(f"{int(validHexNumber, 16)}")
            hexOutput = self._model.hexFormatter(f"{hex(int(validHexNumber, 16))[2:]}" if int(validHexNumber, 16) >= 0 else f"-{hex(int(validHexNumber, 16))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
            binOutput = self._model.binFormatter(f"{bin(int(validHexNumber, 16))[2:]}" if int(validHexNumber, 16) >= 0 else f"-{bin(int(validHexNumber, 16))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
        except ValueError:
            pass

        self._setAllTextBoxes(decOutput, hexOutput, binOutput)

    def _binChanged(self):
        validBinNumber = self._model.binValidator(self._view.bin.binTextBox.document().toPlainText(), self._bitLimits[self._view.bitDropBox.currentIndex()][0], self._signed)
        decOutput = ""
        hexOutput = ""
        binOutput = ""
        
        try:
            if self._signed:
                decOutput = self._model.decFormatter(str(self._model.signedBaseToInt(int(validBinNumber, 2), 64 // (2**self._view.bitDropBox.currentIndex()))))
            else:
                decOutput = self._model.decFormatter(f"{int(validBinNumber, 2)}")
            hexOutput = self._model.hexFormatter(f"{hex(int(validBinNumber, 2))[2:]}" if int(validBinNumber, 2) >= 0 else f"-{hex(int(validBinNumber))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
            binOutput = self._model.binFormatter(f"{bin(int(validBinNumber, 2))[2:]}" if int(validBinNumber, 2) >= 0 else f"-{bin(int(validBinNumber))[3:]}", 64 // (2**self._view.bitDropBox.currentIndex()))
        except ValueError:
            pass

        self._setAllTextBoxes(decOutput, hexOutput, binOutput)

    def _setBitIndex(self):
        self._decChanged()

    def _setSigned(self):
        if self._view.unSignedRadio.isChecked():
            self._signed = 0
            self._view.negateButton.setEnabled(False)
        elif self._view.signedRadio.isChecked():
            self._signed = 1
            self._view.negateButton.setEnabled(True)
        self._decChanged()
    
    def _setNegate(self):
        if self._view.dec.decTextBox.document().toPlainText()[0] != '-':
            self._view.dec.decTextBox.document().setPlainText("-" + self._view.dec.decTextBox.document().toPlainText())
        else:
            self._view.dec.decTextBox.document().setPlainText(self._view.dec.decTextBox.document().toPlainText()[1:])
        pass

    def _connectTextSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        self._view.hex.hexTextBox.textChanged.connect(lambda: self._hexChanged())
        self._view.bin.binTextBox.textChanged.connect(lambda: self._binChanged())

    def _disconnectTextSignals(self):
        self._view.dec.decTextBox.textChanged.disconnect()
        self._view.hex.hexTextBox.textChanged.disconnect()
        self._view.bin.binTextBox.textChanged.disconnect()
    
    def _setAllTextBoxes(self, decOutput, hexOutput, binOutput):
        self._disconnectTextSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectTextSignals()

    def _connectBitSignals(self):
        self._view.bitDropBox.currentIndexChanged.connect(self._setBitIndex)
        self._view.unSignedRadio.toggled.connect(self._setSigned)
        self._view.negateButton.clicked.connect(self._setNegate)
