from functools import partial
import re

class MainCalcCtrl:
    """Main arithmetic calculator
    """
    def __init__(self, model, view):
        """Connect logic from the model to the view for the main calc. 

        Args:
            model : backend logic for the UI
            view : UI for the calculator
        """
        self._evaluate = model
        self._view = view
        self._connectSignals()
        self._evalPressed = False

    def _calculateResult(self):
        """Calculate basic arithmetic  
        """
        self._evalPressed = True
        self._view.mainCalc.setCalcOutput(self._evaluate(expression=self._view.mainCalc.getCalcOutput()))

    def _buildExpression(self, keyInput):
        """Build the expression we plan on evaluating with the calculator

        Args:
            keyInput (key): current key you are pressing to build expressions with
        """
        operators = ["+", "-", "*", "/", "%", "**", "//", "."]
        numbers = map(str, range(0, 10))
        
        # if there was a previous evaluation error, resets calculator
        if self._view.mainCalc.getCalcOutput() == "ERROR":
            self._view.mainCalc.clearCalcOutput()
        
        # checks to see if a number built so far has a decimal
        # but only if the last input is not an operator or is a decimal point
        if keyInput == "." and (self._view.mainCalc.getCalcOutput()[-1] not in operators or self._view.mainCalc.getCalcOutput()[-1] == '.'):
            lastNumber = re.findall(r"\d+\.?\d*", self._view.mainCalc.getCalcOutput())[-1]
            if re.search(r"\.", lastNumber):
                return

        # adding a decimal after an operator will automatically add a 0 to make a legal expression
        if keyInput == "." and self._view.mainCalc.getCalcOutput()[-1] in operators:
            self._view.mainCalc.setCalcOutput(self._view.mainCalc.getCalcOutput() + "0")
        # prevent adding another operator if an operator is already there
        elif keyInput in operators and self._view.mainCalc.getCalcOutput()[-1] in operators:
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
        """Change the display of which view is showing for the second (right-side) calculator.
        """
        self._view.secCalc.secCalcDisplay(self._view.mainCalc.calcDropBox.currentIndex())

    def _connectSignals(self):
        """Connect all of the functionality from the model to the view.
        """
        for buttonText, button in self._view.mainCalc.buttons.items():
            if buttonText not in ["=", "C", "BS"]:
                button.clicked.connect(partial(self._buildExpression, buttonText))
        
        self._view.mainCalc.buttons["="].clicked.connect(self._calculateResult)
        self._view.mainCalc.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.mainCalc.buttons["BS"].clicked.connect(self._view.mainCalc.backSpaceCalcOutput)
        self._view.mainCalc.buttons["C"].clicked.connect(self._view.mainCalc.clearCalcOutput)
        self._view.mainCalc.calcDropBox.currentIndexChanged.connect(self._changeSecCalc)
