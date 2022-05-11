from PyQt5.QtWidgets import QWidget, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QComboBox
from PyQt5.QtCore import Qt

class NumBase(QWidget):
    """
    A QWidget that contains the foundation for three different base unit headers

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    None

    Methods
    -------
    _CreateNumHeader(headerText):
        Creates a QLabel with the text from headerText
    _CreateNumTextBox():
        Creates a QPlainTextEdit widget for input/output
    """
    def __init__(self):
        """
        Constructs a NumBase widget, inheriting all of QWidget's methods and attributes

        Parameters
        ----------
        None

        Returns
        -------
        NumBase
            Initialized NumBase object
        """
        super().__init__()

    def _CreateNumHeader(self, headerText):
        """
        Constructs a QLabel header with headerText

        Parameters
        ----------
        headerText : str
            Input string

        Returns
        -------
        QLabel
            The QLabel header
        """
        header = QLabel(headerText)
        header.setObjectName("baseConvHeader")
        return header
    
    def _CreateNumTextBox(self):
        """
        Constructs a QPlainTextEdit

        Parameters
        ----------
        None

        Returns
        -------
        QPlainTextEdit
            The QPlanTextEdit to be used for input/output
        """
        textbox = QPlainTextEdit()
        textbox.setObjectName("baseEditBox")
        textbox.document().setPlainText("0")
        return textbox

class DecBase(NumBase):
    """
    A decimal base input/output widget

    Inherits all methods and attributes from NumBase

    Attributes
    ----------
    decHeader : QLabel
        Text for the header
    decTextBox : QPlainTextEdit
        Input/output text field

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initializer for DecBase

        Parameters
        ----------
        None

        Returns
        -------
        DecBase
            Initalized DecBase object
        """
        layout = QVBoxLayout()
        super().__init__()        
        self.decHeader = self._CreateNumHeader("Decimal")
        self.decTextBox = self._CreateNumTextBox()
        layout.addWidget(self.decHeader)
        layout.addWidget(self.decTextBox)
        self.setLayout(layout)

class HexBase(NumBase):
    """
    A hexadecimal base input/output widget

    Inherits all methods and attributes from NumBase

    Attributes
    ----------
    hexHeader : QLabel
        Text for the header
    hexTextBox : QPlainTextEdit
        Input/output text field

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initializer for DecBase

        Parameters
        ----------
        None

        Returns
        -------
        HexBase
            Initalized HexBase object
        """
        super().__init__()
        layout = QVBoxLayout()
        self.hexHeader = self._CreateNumHeader("Hexadecimal")
        self.hexTextBox = self._CreateNumTextBox()
        layout.addWidget(self.hexHeader)
        layout.addWidget(self.hexTextBox)
        self.setLayout(layout)        

class BinBase(NumBase):
    """
    A binary base input/output widget

    Inherits all methods and attributes from NumBase

    Attributes
    ----------
    binHeader : QLabel
        Text for the header
    binTextBox : QPlainTextEdit
        Input/output text field

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initializer for BinBase

        Parameters
        ----------
        None

        Returns
        -------
        BinBase
            Initalized BinBase object
        """
        super().__init__()  
        layout = QVBoxLayout()
        self.binHeader = self._CreateNumHeader("Binary")
        self.binTextBox = self._CreateNumTextBox()
        layout.addWidget(self.binHeader)
        layout.addWidget(self.binTextBox)
        self.setLayout(layout)      

class BaseConvUI(QWidget):
    """
    A QWidget creates the three main number bases of decimal, hexadecimal, and binary.
    Also creates the layout for signed/unsigned QRadioButtons, a negate QPushButton,
    and QComboBox for bit-width selection.

    Inherits all methods and attributes from QWidget

    Attributes
    ----------
    unsignedRadio : QRadioButton
        Radiobutton input for unsigned
    signedRadio : QRadioButton
        Radiobutton input for signed
    negateBUtton : QPushButton
        button to negate values
    bitDropBox : QComboBox
        Dropbox menu selection for 8, 16, 32, or 64 bit widths
    dec : DecBase
        DecBase Widget
    hex : HexBase
        HexBase Widget
    bin : BinBase
        BinBase Widget

    Methods
    -------
    _createBitLengthBox():
        Internal method to create QComboBox with 8-64 bit options
    """
    def __init__(self):
        """
        Initializer for BaseConvUI. Creates all QWidgets and layouts

        Parameters
        ----------
        None

        Returns
        -------
        BaseConvUI
            Initalized BaseConvUI view
        """
        super().__init__()
        layout = QVBoxLayout()
        bitLayout = QHBoxLayout()
        bitLayout.setAlignment(Qt.AlignHCenter)
        self.unSignedRadio = QRadioButton("Unsigned")
        self.unSignedRadio.setObjectName("unSignedRadio")
        self.unSignedRadio.setChecked(True)
        self.signedRadio = QRadioButton("Signed")
        self.signedRadio.setObjectName("signedRadio")
        self.negateButton = QPushButton("Negate")
        self.negateButton.setObjectName("negate")
        self.negateButton.setEnabled(False)
        self.bitDropBox = self._createBitLengthBox()
        bitLayout.addWidget(self.unSignedRadio)
        bitLayout.addWidget(self.signedRadio)
        bitLayout.addWidget(self.negateButton)
        bitLayout.addWidget(self.bitDropBox)
        layout.addLayout(bitLayout)
        self.dec = DecBase()
        layout.addWidget(self.dec)
        self.hex = HexBase()
        layout.addWidget(self.hex)
        self.bin = BinBase()
        layout.addWidget(self.bin)
        self.setLayout(layout)

    def _createBitLengthBox(self):
        """
        Internal method for creating a QComboBox with 8-64 bit-width options

        Parameters
        ----------
        None

        Returns
        -------
        QComboBox
            Dropbox of various bit-widths
        """
        bitDropBox = QComboBox()
        bitDropBox.setObjectName("bitDropBox")
        bitDropBox.addItems(["QWord - 64bit", "DWord - 32bit", "Word - 16bit", "Byte - 8bit"])
        return bitDropBox
