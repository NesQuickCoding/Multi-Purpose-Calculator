from functools import partial

class MainCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.mainCalc.displayText())
        self._view.mainCalc.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.mainCalc.displayText() == "ERROR":
            self._view.mainCalc.clearDisplay()

        expression = self._view.mainCalc.displayText() + sub_exp
        self._view.mainCalc.setDisplayText(expression)

    def _changeSecCalc(self):
        if self._view.mainCalc.calcDropBox.currentIndex() == 1:
            self._view.secCalc.secCalcDisplay(1)
        else:
            self._view.secCalc.secCalcDisplay(0)
    
    def _connectSignals(self):
        for btnText, btn in self._view.mainCalc.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.mainCalc.buttons["="].clicked.connect(self._calculateResult)
        self._view.mainCalc.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.mainCalc.buttons["C"].clicked.connect(self._view.mainCalc.clearDisplay)
        self._view.mainCalc.calcDropBox.currentIndexChanged.connect(self._changeSecCalc)
