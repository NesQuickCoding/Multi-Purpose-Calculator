class BaseConvCtrl:
    """
    Handles the logic and singal connections for BaseConvUI

    Attributes
    ----------
    _view : BaseConvUI
        Stores the reference to the BaseConvUI widget
    _model : module
        Stores the reference base_conv/models.py with validator, formating, and calculating
        functions
    _bitLimits : [(int, int)]
        Stores tuples of the roof/limit for each of the 4 bit widths, with the first tiple
        being the limit for unsigned, and the second for signed
    _signed : int
        0 for unsigned, 1 for signed, used for accessing the appropriate tuple index

    Methods
    -------
    _decChanged():
        Handler for when the decimal textbox is changed. Calls conversion and format
        functions for every base, and sends the results to their respective outputs.
    _hexChanged():
        Handler for when the hexadecimal textbox is changed. Calls conversion and format
        functions for every base, and sends the results to their respective outputs.
    _binChanged():
        Handler for when the binary textbox is changed. Calls conversion and format
        functions for every base, and sends the results to their respective outputs.
    _setSigned():
        Handler for when the signed/unsigned radio buttons change. Calls conversion and
        format functions for every base, and sends the results to their respective outputs.
    _setNegate():
        Toggles negation of a number and changed every textbox. Calls conversion and format
        functions for every base, and sends the results to their respective outputs.
    _connectTextSignals
        Connects textbox textHasChanged signals.
    _disconnectTextSignals
        Disconnects textbox textHasChanged signals.
    _setAllTextBoxes(decOutput, hexOutput, binOutput)
        Disables textbox signals, sets the text, then re-enables them.
    _connectBitSignals()
        Connects the dropbox and radio buttons to handle changes in their state.
    """
    def __init__(self, view, model):
        """
        Constructs the BaseConvCtrl, constructing signals for BaseConvUI and connecting
        them to the correct model/function for conversion calculations

        Parameters
        ----------
        view : BaseConvUI
            Used to reference and connect BaseConvUI's attributes
        model : module
            Reference to base_conv/models.py with validator, formating, and calculating
            functions

        Returns
        -------
        BaseConvUI
            Connects BaseConvUI to the appropriate signals
        """
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
        """
        Handles the input of the Decimal field
        1. Validates the number
        2. Formats to decimal
        3. Formats the value to hexadecimal
        4. Formats the value to binary
        4. Sets the input for all three fields with their respective formatted value

        Parameters
        ----------
        None

        Raises
        ------
        ValueError
            Occurs when formatting the three with an invalid string or type.
            Typically done on null strings, passes whenever triggered.

        Returns
        -------
        None
        """
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
        """
        Handles the input of the Hexadecimal field
        1. Validates the number
        2. Formats the hexadecimal value
        3. Formats the value to decimal
        4. Formats the value to binary
        4. Sets the input for all three fields with their respective formatted value

        Parameters
        ----------
        None

        Raises
        ------
        ValueError
            Occurs when formatting the three with an invalid string or type.
            Typically done on null strings, passes whenever triggered.

        Returns
        -------
        None
        """
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
        """
        Handles the input of the Binary field
        1. Validates the number
        2. Formats the binary value
        3. Formats the value to decimal
        4. Formats the value to hexadecimal
        4. Sets the input for all three fields with their respective formatted value

        Parameters
        ----------
        None

        Raises
        ------
        ValueError
            Occurs when formatting the three with an invalid string or type.
            Typically done on null strings, passes whenever triggered.

        Returns
        -------
        None
        """
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

    def _setSigned(self):
        """
        Sets _signed based on signage selection from the QRadioButtons. Will also disable the
        negate button if _signed is 1/True. Immediately calls for conversion and changes out
        once set.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self._view.unSignedRadio.isChecked():
            self._signed = 0
            self._view.negateButton.setEnabled(False)
        elif self._view.signedRadio.isChecked():
            self._signed = 1
            self._view.negateButton.setEnabled(True)
        self._decChanged()
    
    def _setNegate(self):
        """
        Adds a '-' to decTextBox then sets the textbox, causing conversion to happen automatically
        If a '-' is already there, it is trimmed and the conversion is triggered again

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self._view.dec.decTextBox.document().toPlainText()[0] != '-':
            self._view.dec.decTextBox.document().setPlainText("-" + self._view.dec.decTextBox.document().toPlainText())
        else:
            self._view.dec.decTextBox.document().setPlainText(self._view.dec.decTextBox.document().toPlainText()[1:])
        
    def _connectTextSignals(self):
        """
        Connects decTextBox, hexTextBox, and binTextBox textChanged signals

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
        self._view.hex.hexTextBox.textChanged.connect(lambda: self._hexChanged())
        self._view.bin.binTextBox.textChanged.connect(lambda: self._binChanged())

    def _disconnectTextSignals(self):
        """
        Disconnects decTextBox, hexTextBox, and binTextBox textChanged signals

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.dec.decTextBox.textChanged.disconnect()
        self._view.hex.hexTextBox.textChanged.disconnect()
        self._view.bin.binTextBox.textChanged.disconnect()
    
    def _setAllTextBoxes(self, decOutput, hexOutput, binOutput):
        """
        Sets decTextBox, hexTextBox, and binTextBox to their respective output. Disconnects
        signals first, then reconnects after setting text.

        Parameters
        ----------
        decOutput : str
            decTextBox's new text value
        hexOutput : str
            hexTextBox's new text value
        binOutput : str
            binTextBox's new text value

        Returns
        -------
        None
        """
        self._disconnectTextSignals()
        self._view.dec.decTextBox.document().setPlainText(decOutput)
        self._view.hex.hexTextBox.document().setPlainText(hexOutput)
        self._view.bin.binTextBox.document().setPlainText(binOutput)
        self._connectTextSignals()

    def _connectBitSignals(self):
        """
        Connects bitDropBox, unSignedRadio and negateButton to their respective signals,
        listening to any changes in their state.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.bitDropBox.currentIndexChanged.connect(self._decChanged)
        self._view.unSignedRadio.toggled.connect(self._setSigned)
        self._view.negateButton.clicked.connect(self._setNegate)
