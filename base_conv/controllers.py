class BaseConvCtrl:
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _convert(self):
        pass

    def _decChanged(self):
        self._view.hex.hexTextBox.document().setPlainText(self._view.dec.decTextBox.document().toPlainText())
        self._view.bin.binTextBox.document().setPlainText(self._view.dec.decTextBox.document().toPlainText())
    
    def _connectSignals(self):
        self._view.dec.decTextBox.textChanged.connect(lambda: self._decChanged())
