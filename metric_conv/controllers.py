class MetricConvCtrl:
    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._model = model
        self._connectComboBoxSignals()
        self._connectTextSignals()
    
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
    
    def _toggleInputError(self):
        self._view.leftTextEdit.setStyleSheet("border: 1px solid red;")
        self._view.rightTextEdit.setStyleSheet("border: 1px solid red;")

    def _textChanged(self, inputField, outputField):
        inputString = inputField.text()
        outputString = inputField.text()
        
        if inputString or outputString:
            try:
                outputString = str(self._model.length_conversion(float(inputString), self._view.leftComboBox.currentText(), self._view.rightComboBox.currentText()))
                inputField.setStyleSheet("border: 1px solid black;")
                outputField.setStyleSheet("border: 1px solid black;")
            except ValueError:
                inputField.setStyleSheet("border: 1px solid red;")
                outputField.setStyleSheet("border: 1px solid red;")
                pass
        else:
            inputField.setStyleSheet("border: 1px solid black;")
            outputField.setStyleSheet("border: 1px solid black;")        
        
        self._setTextFields(inputField, outputField, inputString, outputString)
