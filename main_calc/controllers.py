from functools import partial

class MainCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()
        self._evalPressed = False

    def _calculateResult(self):
        self._evalPressed = True
        self._view.mainCalc.setCalcOutput(self._evaluate(expression=self._view.mainCalc.getCalcOutput()))

    def _buildExpression(self, keyInput):
        operators = ["+", "-", "*", "/", "%", "**", "//"]
        numbers = map(str, range(0, 10))
        
        # if there was an error, resets calculator
        if self._view.mainCalc.getCalcOutput() == "ERROR":
            self._view.mainCalc.clearCalcOutput()

        # prevent adding another operator if an operator is already there
        try:
            if keyInput in operators and self._view.mainCalc.getCalcOutput()[-1] in operators:
                return        
        except IndexError:
            return
        
        # if adding number when there's only a zero
        # OR if adding a number after just hitting '='
        # replaces it with just the keyInput number
        if keyInput in numbers and (self._view.mainCalc.getCalcOutput() == "0" or self._evalPressed):
            self._view.mainCalc.setCalcOutput(keyInput)
        
        # otherwise append the keyInput press into the expression
        else:
            self._view.mainCalc.setCalcOutput(self._view.mainCalc.getCalcOutput() + keyInput)
        
        self._evalPressed = False

    def _changeSecCalc(self):
        self._view.secCalc.secCalcDisplay(self._view.mainCalc.calcDropBox.currentIndex())

    def _connectSignals(self):
        for buttonText, button in self._view.mainCalc.buttons.items():
            if buttonText not in ["=", "C", "BS"]:
                button.clicked.connect(partial(self._buildExpression, buttonText))
        
        self._view.mainCalc.buttons["="].clicked.connect(self._calculateResult)
        self._view.mainCalc.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.mainCalc.buttons["BS"].clicked.connect(self._view.mainCalc.backSpaceCalcOutput)
        self._view.mainCalc.buttons["C"].clicked.connect(self._view.mainCalc.clearCalcOutput)
        self._view.mainCalc.calcDropBox.currentIndexChanged.connect(self._changeSecCalc)
