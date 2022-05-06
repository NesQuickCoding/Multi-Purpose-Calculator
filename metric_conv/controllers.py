class MetricConvCtrl:
    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._models = model
        self._connectComboBoxSignals()
        self._connectTextSignals()
    
    def _connectComboBoxSignals(self):
        pass

    def _connectTextSignals(self):
        self._view.leftTextEdit.textChanged.connect(lambda: self._textChanged(self._view.leftTextEdit, self._view.rightTextEdit))
        self._view.rightTextEdit.textChanged.connect(lambda: self._textChanged(self._view.rightTextEdit, self._view.leftTextEdit))

    def _disconnectTextSignals(self):
        self._view.leftTextEdit.textChanged.disconnect()
        self._view.rightTextEdit.textChanged.disconnect()
    
    def _setTextFields(self, string):
        self._disconnectTextSignals()
        self._view.leftTextEdit.setText(string)
        self._view.rightTextEdit.setText(string)
        self._connectTextSignals()
    
    def _textChanged(self, inputField, outputField):
        if self._view.leftComboBox.currentIndex() != self._view.rightComboBox.currentIndex():
            # run conversions
            pass
        
        self._setTextFields(inputField.text())
