class MetricConvCtrl:
    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._models = model
        self._connectComboBoxSignals()
        self._connectTextSignals()
    
    def _leftTextChanged(self):
        pass

    def _rightTextChanged(self):
        pass

    def _connectComboBoxSignals(self):
        pass

    def _connectTextSignals(self):
        self._view.leftTextEdit.textChanged.connect(self._leftTextChanged)
        self._view.rightTextEdit.textChanged.connect(self._rightTextChanged)

    def _disconnectTextSignals(self):
        self._view.leftTextEdit.textChanged.disconnect()
        self._view.rightTextEdit.textChanged.disconnect()
    
    def _setTextFields(self, string):
        self._disconnectTextSignals()
        self._view.leftTextEdit.setText(string)
        self._view.rightTextEdit.setText(string)
        self._connectTextSignals()
