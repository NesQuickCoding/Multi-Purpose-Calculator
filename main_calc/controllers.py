from functools import partial

class MainCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.mainCalc.getCalcOutput())
        self._view.mainCalc.setCalcOutput(result)

    def _buildExpression(self, sub_exp):
        if self._view.mainCalc.getCalcOutput() == "ERROR":
            self._view.mainCalc.clearCalcOutput()

        expression = self._view.mainCalc.getCalcOutput() + sub_exp
        self._view.mainCalc.setCalcOutput(expression)

    def _changeSecCalc(self):
        self._view.secCalc.secCalcDisplay(self._view.mainCalc.calcDropBox.currentIndex())

    def _connectSignals(self):
        for buttonText, button in self._view.mainCalc.buttons.items():
            if buttonText not in {"=", "C", "BS"}:
                button.clicked.connect(partial(self._buildExpression, buttonText))
        
        self._view.mainCalc.buttons["="].clicked.connect(self._calculateResult)
        self._view.mainCalc.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.mainCalc.buttons["BS"].clicked.connect(self._view.mainCalc.backSpaceCalcOutput)
        self._view.mainCalc.buttons["C"].clicked.connect(self._view.mainCalc.clearCalcOutput)
        self._view.mainCalc.calcDropBox.currentIndexChanged.connect(self._changeSecCalc)
