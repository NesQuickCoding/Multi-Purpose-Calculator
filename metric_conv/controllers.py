class MetricConvCtrl:
    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._model = model
        self._connectComboBoxSignals()
        self._connectTextSignals()
        self._leftUnitIndex = 0
        self._rightUnitIndex = 0
    
    def _connectComboBoxSignals(self):
        self._view.leftComboBox.currentIndexChanged.connect(lambda: self._setComboSignals())
        self._view.rightComboBox.currentIndexChanged.connect(lambda: self._setComboSignals())

    def _setComboSignals(self):
        self._leftUnitIndex = (self._view.leftComboBox.currentIndex())
        self._rightUnitIndex = (self._view.rightComboBox.currentIndex())

    def _connectTextSignals(self):
        self._view.leftTextEdit.textChanged.connect(lambda: self._textChanged(self._view.leftTextEdit, self._view.rightTextEdit))
        self._view.rightTextEdit.textChanged.connect(lambda: self._textChanged(self._view.rightTextEdit, self._view.leftTextEdit))

    def _disconnectTextSignals(self):
        self._view.leftTextEdit.textChanged.disconnect()
        self._view.rightTextEdit.textChanged.disconnect()
    
    def _setTextFields(self, inputField, outputField, inputString, outputString):
        self._disconnectTextSignals()
        inputField.setText(inputString)
        outputField.setText(outputString)
        self._connectTextSignals()
    
    def _textChanged(self, inputField, outputField):
        inputString = inputField.text()
        outputString = inputField.text()
        if self._leftUnitIndex != self._rightUnitIndex:
            if self._leftUnitIndex in range(4, 7) and self._rightUnitIndex in range(4,7):
                outputString = str(self._model.metricLengthConversion(float(inputString), self._leftUnitIndex - self._rightUnitIndex))
                
        self._setTextFields(inputField, outputField, inputString, outputString)
