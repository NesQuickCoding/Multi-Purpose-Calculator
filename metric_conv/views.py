from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt

class MetricConvWidget(QWidget):
    """
    A QWidget that has two QLineEdit text fields each with their own QComboBox for a list
    of conversion options between the two sides.

    Inherits all methods and attributes from QWidget

    Attributes
    ----------

    leftTextEdit : QLineEdit
        Left input/output field for conversion
    leftComboBox : QComboBox
        Left side conversion unit options
    rightTextEdit : QLineEdit
        Right input/output field for conversion
    rightComboBox : QComboBox
        Right side conversion unit options

    Methods
    -------
    _createOptionLayout(QLineEditObj, QComboBoxObj, items):
        Internal method for initialization, used to create the layout and
        QComboBox
    """
    def __init__(self, stringLabel, unitOptions):
        """
        Constructs a MetricConvWidget, including it's layout and attributes
        Used perform unit conversion between two units

        Parameters
        ----------
        stringLabel : str
            Used to create A QLabel for the MetricConvWidget object
        unitOptions: [str]
            A list of str objects, each one being a different measurement unit

        Returns
        -------
        MetricConvWidget
            Newly constructed widget
        """
        super().__init__()   
        mainLayout = QVBoxLayout()
        
        label = QLabel(stringLabel)
        label.setFont(QFont('Arial', 12))
        mainLayout.addWidget(label)

        convLayout = QHBoxLayout()

        self.leftTextEdit = QLineEdit()
        self.leftComboBox = QComboBox()
        convLayout.addLayout(self._createOptionLayout(self.leftTextEdit, self.leftComboBox, unitOptions))
        
        equalSign = QLabel('=')
        equalSign.setFont(QFont('Arial', 12))
        convLayout.addWidget(equalSign)

        self.rightTextEdit = QLineEdit()
        self.rightComboBox = QComboBox()
        convLayout.addLayout(self._createOptionLayout(self.rightTextEdit, self.rightComboBox, unitOptions))
        
        mainLayout.addLayout(convLayout)

        self.setLayout(mainLayout)

    def _createOptionLayout(self, QLineEditObj, QComboBoxObj, items):
        """
        Creates a QVBoxLayout for each side of the conversion, as well as settings for
        left/rightTextEdit and left/rightComboBox data attributes

        Parameters
        ----------
        QLineEditObj : QLineEdit
            Reference to the object's attribute for the left/rightTextEdit
        QComboBoxObj: QComboBox
            Reference to the object's attributefor the left/rightComboBox
        items : [str]
            A list of str objects, each one being a different measurement unit

        Returns
        -------
        QVBoxLayout
            Layout with QWidgets attached
        """
        layout = QVBoxLayout()
        
        QLineEditObj.setValidator(QDoubleValidator())

        QLineEditObj.setFont(QFont('Arial', 12))

        QComboBoxObj.addItems(items)
        QComboBoxObj.setFont(QFont('Arial', 12))
        QComboBoxObj.setFixedHeight(20)
        
        layout.addWidget(QLineEditObj)
        layout.addWidget(QComboBoxObj)
        layout.setAlignment(Qt.AlignHCenter)
        
        return layout

class MetricConvUI(QWidget):
    """
    A QWidget that the UI for the Metric Conversion option of the calculator.
    Makes four different MetricConvWidget objects, one for length, weight,
    time, and digital space.

    Inherits all methods and attributes from QWidget

    Attributes
    ----------

    lengthView : MetricConvWidget
        QWidget for length conversion
    weightView : MetricConvWidget
        QWidget for weight conversion
    timeView : MetricConvWidget
        QWidget for time conversion
    sigitalStorageView : MetricConvWidget
        QWidget for digital space conversion

    Methods
    -------
    None
    """
    def __init__(self):
        """
        Initializes the MetricConvUI, with 4 MetricConvWidget objects.
        One for length, weight, time, and digital storage

        Parameters
        ----------
        None

        Returns
        -------
        MetricConvUI
            Newly constructed widget
        """
        super().__init__()

        # Menu options for each type of measurements
        lengthUnitOptions = [
            "Inches", "Feet", "Yards", "Miles",
            "Millimeters", "Centimeters", "Meters", "Kilometers"
        ]

        weightUnitOptions = [
            "Ounces", "Pounds", "Stone", "Tons (Short)",
            "Milligrams", "Grams", "Kilograms"
        ]

        timeUnitOptions = [
            "Milliseconds", "Seconds", "Minutes", "Hours",
            "Days", "Months", "Years"
        ]

        digitalStorageOptions = [
            "Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes",
            "Terabytes", "Petabytes", "Exabytes", "Zettabytes", "Yottabytes"
        ]

        layout = QVBoxLayout()

        self.lengthView = MetricConvWidget("Length", lengthUnitOptions)
        layout.addWidget(self.lengthView)

        self.weightView = MetricConvWidget("Weight", weightUnitOptions)
        layout.addWidget(self.weightView)

        self.timeView = MetricConvWidget("Time", timeUnitOptions)
        layout.addWidget(self.timeView)

        self.digitalStorageView = MetricConvWidget("Digital Storage", digitalStorageOptions)
        layout.addWidget(self.digitalStorageView)

        self.setLayout(layout)
        
