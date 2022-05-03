from functools import partial

class MultiCalcCtrl:
    """PyCalc's Controller."""

    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.calcMain.displayText())
        self._view.calcMain.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.calcMain.displayText() == "ERROR":
            self._view.calcMain.clearDisplay()

        expression = self._view.calcMain.displayText() + sub_exp
        self._view.calcMain.setDisplayText(expression)

    def _changeSide(self):
        if self._view.calcMain.calcDropBox.currentIndex() == 1:
            self._view.calcSide.primeGenTabs.show()
            self._view.calcSide.placeHolder.hide()
        else:
            self._view.calcSide.primeGenTabs.hide()
            self._view.calcSide.placeHolder.show()
    
    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.calcMain.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.calcMain.buttons["="].clicked.connect(self._calculateResult)
        self._view.calcMain.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.calcMain.buttons["C"].clicked.connect(self._view.calcMain.clearDisplay)
        self._view.calcMain.calcDropBox.currentIndexChanged.connect(self._changeSide)
