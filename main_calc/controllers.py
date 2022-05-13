from functools import partial
import re

class MainCalcCtrl:
    """
    Handles the logic and singal connections for MainCalcUI. Retrieves user input to
    perform operations or send to other functions for evaluation.

    Also controls the secondary calculator widget display

    Attributes
    ----------
    _evaluate : function
        Reference to evaluation function
    _view : MainCalcUI
        Reference to MainCalcUI and it's widgets
    _evalPressed : Boolean
        Handled submission state. Default is False.

    Methods
    -------
    _calculateResult():
        Sends expression built so far to evaluation function.
    _buildExpression(keyInput):
        Handler for any building expression via the calculator buttons.
        Dictates certain behavior to optimize use (such as not inputing
        consecutive operators)
    _changeSecCalc():
        Changes sec calc display based on combo box index
    _connectSignals():
        Connects buttons and output to their respective handlers
    """
    def __init__(self, model, view):
        """
        Initilizer for MainCalcCtrl. Connects signals to their handlers.

        Parameters
        ----------
        model : function
            Used to reference function for evaluation
        view : MainCalcUI
            Reference to ManCalcUI and it's UI widgets.

        Returns
        -------
        MainCalcCtrl
            Control object for MainCalcUI
        """
        self._evaluate = model
        self._view = view
        self._connectSignals()
        self._evalPressed = False

    def _calculateResult(self):
        """
        Sets _evalPressed to True and sends built expression to be evaluated

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._evalPressed = True
        self._view.mainCalc.setCalcOutput(self._evaluate(expression=self._view.mainCalc.getCalcOutput()))

    def _buildExpression(self, keyInput):
        """
        Handler for MainCalcUI's button to build expression. Performs certain input handling:
        - Reset expression if previous result was "ERROR"
        - Proper decimal point input

        Parameters
        ----------
        keyInput : str
            String of button pressed

        Returns
        -------
        None
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
        """
        Sets the widget to be used for the secondary display.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.secCalc.secCalcDisplay(self._view.mainCalc.calcDropBox.currentIndex())

    def _connectSignals(self):
        """
        Connects the buttons and output signals to their proper handlers.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for buttonText, button in self._view.mainCalc.buttons.items():
            if buttonText not in ["=", "C", "BS"]:
                button.clicked.connect(partial(self._buildExpression, buttonText))
        
        self._view.mainCalc.buttons["="].clicked.connect(self._calculateResult)
        self._view.mainCalc.calcOutput.returnPressed.connect(self._calculateResult)
        self._view.mainCalc.buttons["BS"].clicked.connect(self._view.mainCalc.backSpaceCalcOutput)
        self._view.mainCalc.buttons["C"].clicked.connect(self._view.mainCalc.clearCalcOutput)
        self._view.mainCalc.calcDropBox.currentIndexChanged.connect(self._changeSecCalc)
