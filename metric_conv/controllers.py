class MetricConvCtrl:
    """
    Handles the logic and signal connections for the MetricConvUI
    
    Attributes
    ----------
    _view : MetricConvWidget
        Stores the reference to the QWidget
    _model : function
        Stores the reference to the specific function for calculations

    Methods
    -------
    _connectComboBoxSignals():
        Connects MetricConvWidget's QComboBoxs' signal whenever their current index changes
    _connectTextSignals():
        Connects MetricConvWidget's QLineEdits' signal whenever their text changes
    _disconnectTextSignals():
        Disconnects MetricConvWidget's QLineEdits' signal
    _setTextFields(inputField, outputField, inputString, outputString):
        Changes inputField and outputField's text with outputString by disconnecting
        their text signals, sets their text, and reactivates the signals
    _textChanged(inputField, outputField, inputMenu, outputMenu):
        Passes the text of inputField and the indexes of inputMenu and outputMenu to be
        calculated by _model.
        Activates when a user changes the text of the QLineEdits or changes the current index
        of the QComboBoxs
    _toggleValidStyle():
        Changes the object name for the left/rightTextEdit fields to valid, and loads stylesheet
    _toggleInvalidStyle()
        Changes the object name for the left/rightTextEdit fields to invalid, and loads stylesheet
    """
    def __init__(self, view, model):
        """
        Constructs the MetricConvCtrl, building signals for MetricConvWidget and connecting
        them to the correct model/function for conversion calculations

        Parameters
        ----------
        view : MetricConvWidget
            Used to reference and connect MetricConvWidget's attributes
        model : function
            Reference to the function to perform conversion calculations

        Returns
        -------
        MetricConvCtrl
            Connects MetricConvWidget to the appropriate signals
        """
        super().__init__()
        self._view = view
        self._model = model
        self._connectComboBoxSignals()
        self._connectTextSignals()
    
    def _connectComboBoxSignals(self):
        """
        Connects MetricConvWidget's QComboBoxs' signal whenever their current index changes

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.leftComboBox.currentIndexChanged.connect(lambda: self._textChanged(self._view.leftTextEdit, self._view.rightTextEdit, self._view.leftComboBox.currentIndex(), self._view.rightComboBox.currentIndex()))
        self._view.rightComboBox.currentIndexChanged.connect(lambda: self._textChanged(self._view.rightTextEdit, self._view.leftTextEdit, self._view.rightComboBox.currentIndex(), self._view.leftComboBox.currentIndex()))

    def _connectTextSignals(self):
        """
        Connects MetricConvWidget's QLineEdits' signal whenever their text changes

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.leftTextEdit.textChanged.connect(lambda: self._textChanged(self._view.leftTextEdit, self._view.rightTextEdit, self._view.leftComboBox.currentIndex(), self._view.rightComboBox.currentIndex()))
        self._view.rightTextEdit.textChanged.connect(lambda: self._textChanged(self._view.rightTextEdit, self._view.leftTextEdit, self._view.rightComboBox.currentIndex(), self._view.leftComboBox.currentIndex()))

    def _disconnectTextSignals(self):
        """
        Disconnects MetricConvWidget's QLineEdits' signal

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._view.leftTextEdit.textChanged.disconnect()
        self._view.rightTextEdit.textChanged.disconnect()
    
    def _setTextFields(self, inputField, outputField, inputString, outputString):
        """
        Changes inputField and outputField's text with outputString by disconnecting
        their text signals, sets their text, and reactivates the signals

        Parameters
        ----------
        inputField : QLineEdit
            Reference to MetricConvWidget's left/rightTextField
        outputField : QLineEdit
            Reference to MetricConvWidget's left/rightTextField. Will always be the opposite
            of inputField
        inputString : str
            String to set for inputField's new text
        outputString : str
            String to set for outputField's new text
        
        Returns
        -------
        None
        """
        self._disconnectTextSignals()
        inputField.setText(inputString)
        outputField.setText(outputString)
        self._connectTextSignals()
    
    def _textChanged(self, inputField, outputField, inputMenu, outputMenu):
        """
        Passes the text of inputField and the indexes of inputMenu and outputMenu to be
        calculated by _model.
        Activates when a user changes the text of the QLineEdits or changes the current index
        of the QComboBoxs

        Parameters
        ----------
        inputField : QLineEdit
            Reference to MetricConvWidget's left/rightTextField
        outputField : QLineEdit
            Reference to MetricConvWidget's left/rightTextField. Will always be the opposite
            of inputField
        inputMenu : int
            Index value for the current index of the input menu
        outputMenug : int
            Index value for the current index of the output menu
        
        Returns
        -------
        None
        """
        inputString = inputField.text()
        outputString = inputField.text()
        
        if inputString or outputString:
            try:
                outputString = str(self._model(float(inputString), inputMenu, outputMenu))
                self._toggleValidStyle()
            except ValueError:
                self._toggleInvalidStyle()
                pass
        else:
            self._toggleValidStyle()       
        
        self._setTextFields(inputField, outputField, inputString, outputString)

    def _toggleValidStyle(self):
        """
        Changes the object name for the left/rightTextEdit fields to valid, and loads stylesheet

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self._view.leftTextEdit.setObjectName("metricValidInput")
        self._view.rightTextEdit.setObjectName("metricValidInput")
        self._view.leftTextEdit.setStyleSheet(open('./Ext_Stylesheet.css').read())
        self._view.rightTextEdit.setStyleSheet(open('./Ext_Stylesheet.css').read())
    
    def _toggleInvalidStyle(self):
        """
        Changes the object name for the left/rightTextEdit fields to invalid, and loads stylesheet

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self._view.leftTextEdit.setObjectName("metricInvalidInput")
        self._view.rightTextEdit.setObjectName("metricInvalidInput")
        self._view.leftTextEdit.setStyleSheet(open('./style/Ext_Stylesheet.css').read())
        self._view.rightTextEdit.setStyleSheet(open('./style/Ext_Stylesheet.css').read())
