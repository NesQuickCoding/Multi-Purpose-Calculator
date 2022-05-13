# Table Of Contents

### From main
* [Class MultiCalcWindow](#class-multicalcwindow)

	* [MultiCalcWindow.\_\_init\_\_(self)](#multicalcwindowinitself)

* [Class SecCalc](#class-seccalc)

	* [SecCalc.\_\_init\_\_(self)](#seccalcinitself)

	* [SecCalc.secCalcDisplay(self, i)](#seccalcseccalcdisplayself-i)

* [main()](#main)


****************************************************
### From ascii_conversion.views
* [Class ascii_Ui](#class-asciiui)

	* [ascii_Ui.\_\_init\_\_(self)](#asciiuiinitself)

	* [ascii_Ui._createValidators(self)](#asciiuicreatevalidatorsself)

	* [ascii_Ui._rangeValidator(self)](#asciiuirangevalidatorself)

	* [ascii_Ui._setValidators(self)](#asciiuisetvalidatorsself)

	* [ascii_Ui.printButtonPressed(self)](#asciiuiprintbuttonpressedself)

	* [ascii_Ui.convert_ascii(self, val, input_unit, output_unit)](#asciiuiconvertasciiself-val-inputunit-outputunit)


****************************************************
### From base_conv.controllers
* [Class BaseConvCtrl](#class-baseconvctrl)

	* [BaseConvCtrl.\_\_init\_\_(self, view, model)](#baseconvctrlinitself-view-model)

	* [BaseConvCtrl._decChanged(self)](#baseconvctrldecchangedself)

	* [BaseConvCtrl._hexChanged(self)](#baseconvctrlhexchangedself)

	* [BaseConvCtrl._binChanged(self)](#baseconvctrlbinchangedself)

	* [BaseConvCtrl._setSigned(self)](#baseconvctrlsetsignedself)

	* [BaseConvCtrl._setNegate(self)](#baseconvctrlsetnegateself)

	* [BaseConvCtrl._connectTextSignals(self)](#baseconvctrlconnecttextsignalsself)

	* [BaseConvCtrl._disconnectTextSignals(self)](#baseconvctrldisconnecttextsignalsself)

	* [BaseConvCtrl._setAllTextBoxes(self, decOutput, hexOutput, binOutput)](#baseconvctrlsetalltextboxesself-decoutput-hexoutput-binoutput)

	* [BaseConvCtrl._connectBitSignals(self)](#baseconvctrlconnectbitsignalsself)


****************************************************
### From base_conv.models
* [binFormatter(stringNumber, bit)](#binformatterstringnumber-bit)

* [binValidator(stringNumber, limit, isSigned)](#binvalidatorstringnumber-limit-issigned)

* [decFormatter(stringNumber)](#decformatterstringnumber)

* [decValidator(stringNumber, limit, isSigned)](#decvalidatorstringnumber-limit-issigned)

* [hexFormatter(stringNumber, bit)](#hexformatterstringnumber-bit)

* [hexValidator(stringNumber, limit, isSigned)](#hexvalidatorstringnumber-limit-issigned)

* [rightToLeftInsertion(string, position, insertChar)](#righttoleftinsertionstring-position-insertchar)

* [signedBaseToInt(value, bits)](#signedbasetointvalue-bits)

* [signedIntToBase(value, bits, base)](#signedinttobasevalue-bits-base)


****************************************************
### From base_conv.views
* [Class BaseConvUI](#class-baseconvui)

	* [BaseConvUI.\_\_init\_\_(self)](#baseconvuiinitself)

	* [BaseConvUI._createBitLengthBox(self)](#baseconvuicreatebitlengthboxself)

* [Class BinBase](#class-binbase)

	* [BinBase.\_\_init\_\_(self)](#binbaseinitself)

* [Class DecBase](#class-decbase)

	* [DecBase.\_\_init\_\_(self)](#decbaseinitself)

* [Class HexBase](#class-hexbase)

	* [HexBase.\_\_init\_\_(self)](#hexbaseinitself)

* [Class NumBase](#class-numbase)

	* [NumBase.\_\_init\_\_(self)](#numbaseinitself)

	* [NumBase._CreateNumHeader(self, headerText)](#numbasecreatenumheaderself-headertext)

	* [NumBase._CreateNumTextBox(self)](#numbasecreatenumtextboxself)


****************************************************
### From base_conv.test
* [Class TestWindowBaseConv](#class-testwindowbaseconv)

	* [TestWindowBaseConv.\_\_init\_\_(self)](#testwindowbaseconvinitself)

* [main_test_base_conv()](#maintestbaseconv)


****************************************************
### From birthday_conversion.views
* [Class birthday_Ui](#class-birthdayui)

	* [birthday_Ui.\_\_init\_\_(self)](#birthdayuiinitself)

	* [birthday_Ui._inputCheck(self)](#birthdayuiinputcheckself)

	* [birthday_Ui.enterButtonPressed(self)](#birthdayuienterbuttonpressedself)

	* [birthday_Ui.get_birthday(self, combo_input, calendar_input)](#birthdayuigetbirthdayself-comboinput-calendarinput)

* [get_days(month, day, year)](#getdaysmonth-day-year)

* [get_months(month, day, year)](#getmonthsmonth-day-year)

* [get_years(month, day, year)](#getyearsmonth-day-year)


****************************************************
### From prime_gen.views
* [Class IsPrime](#class-isprime)

	* [IsPrime.\_\_init\_\_(self)](#isprimeinitself)

	* [IsPrime._CreateIsPrimeHeader(self)](#isprimecreateisprimeheaderself)

	* [IsPrime._CreateIsPrimeInput(self)](#isprimecreateisprimeinputself)

	* [IsPrime._CreateIsPrimeOutput(self)](#isprimecreateisprimeoutputself)

* [Class PrimeGenUI](#class-primegenui)

	* [PrimeGenUI.\_\_init\_\_(self)](#primegenuiinitself)

* [Class PrimeRandomGen](#class-primerandomgen)

	* [PrimeRandomGen.\_\_init\_\_(self)](#primerandomgeninitself)

	* [PrimeRandomGen._CreateRandomHeader(self)](#primerandomgencreaterandomheaderself)

	* [PrimeRandomGen._CreateRandomInput(self)](#primerandomgencreaterandominputself)

	* [PrimeRandomGen._CreateRandomButtons(self)](#primerandomgencreaterandombuttonsself)

	* [PrimeRandomGen.setRandomOutput(self, text)](#primerandomgensetrandomoutputself-text)

	* [PrimeRandomGen.getRandomOutput(self)](#primerandomgengetrandomoutputself)

	* [PrimeRandomGen.clearRandomOutput(self)](#primerandomgenclearrandomoutputself)

* [Class PrimeRangeGen](#class-primerangegen)

	* [PrimeRangeGen.\_\_init\_\_(self)](#primerangegeninitself)

	* [PrimeRangeGen._CreateRangeHeader(self)](#primerangegencreaterangeheaderself)

	* [PrimeRangeGen._CreateRangeInput(self)](#primerangegencreaterangeinputself)

	* [PrimeRangeGen._CreateRangeButtons(self)](#primerangegencreaterangebuttonsself)

	* [PrimeRangeGen.setRangeOutput(self, text)](#primerangegensetrangeoutputself-text)

	* [PrimeRangeGen.getRangeOutput(self)](#primerangegengetrangeoutputself)

	* [PrimeRangeGen.clearRangeOutput(self)](#primerangegenclearrangeoutputself)

* [Class ScrollLabel](#class-scrolllabel)

	* [ScrollLabel.\_\_init\_\_(self)](#scrolllabelinitself)

	* [ScrollLabel.setText(self, text)](#scrolllabelsettextself-text)

	* [ScrollLabel.text(self)](#scrolllabeltextself)


****************************************************
### From main_calc.controllers
* [Class MainCalcCtrl](#class-maincalcctrl)

	* [MainCalcCtrl.\_\_init\_\_(self, model, view)](#maincalcctrlinitself-model-view)

	* [MainCalcCtrl._calculateResult(self)](#maincalcctrlcalculateresultself)

	* [MainCalcCtrl._buildExpression(self, keyInput)](#maincalcctrlbuildexpressionself-keyinput)

	* [MainCalcCtrl._changeSecCalc(self)](#maincalcctrlchangeseccalcself)

	* [MainCalcCtrl._connectSignals(self)](#maincalcctrlconnectsignalsself)


****************************************************
### From main_calc.models
* [astTransversal(astObj)](#asttransversalastobj)

* [evaluateExpression(expression)](#evaluateexpressionexpression)


****************************************************
### From main_calc.views
* [Class MainCalcUI](#class-maincalcui)

	* [MainCalcUI.\_\_init\_\_(self, dropMenu)](#maincalcuiinitself-dropmenu)

	* [MainCalcUI._createCalcOutput(self)](#maincalcuicreatecalcoutputself)

	* [MainCalcUI._createDropBox(self, dropMenu)](#maincalcuicreatedropboxself-dropmenu)

	* [MainCalcUI._createButtons(self)](#maincalcuicreatebuttonsself)

	* [MainCalcUI.setCalcOutput(self, text)](#maincalcuisetcalcoutputself-text)

	* [MainCalcUI.getCalcOutput(self)](#maincalcuigetcalcoutputself)

	* [MainCalcUI.backSpaceCalcOutput(self)](#maincalcuibackspacecalcoutputself)

	* [MainCalcUI.clearCalcOutput(self)](#maincalcuiclearcalcoutputself)


****************************************************
### From metric_conv.controllers
* [Class MetricConvCtrl](#class-metricconvctrl)

	* [MetricConvCtrl.\_\_init\_\_(self, view, model)](#metricconvctrlinitself-view-model)

	* [MetricConvCtrl._connectComboBoxSignals(self)](#metricconvctrlconnectcomboboxsignalsself)

	* [MetricConvCtrl._connectTextSignals(self)](#metricconvctrlconnecttextsignalsself)

	* [MetricConvCtrl._disconnectTextSignals(self)](#metricconvctrldisconnecttextsignalsself)

	* [MetricConvCtrl._setTextFields(self, inputField, outputField, inputString, outputString)](#metricconvctrlsettextfieldsself-inputfield-outputfield-inputstring-outputstring)

	* [MetricConvCtrl._textChanged(self, inputField, outputField, inputMenu, outputMenu)](#metricconvctrltextchangedself-inputfield-outputfield-inputmenu-outputmenu)

	* [MetricConvCtrl._toggleValidStyle(self)](#metricconvctrltogglevalidstyleself)

	* [MetricConvCtrl._toggleInvalidStyle(self)](#metricconvctrltoggleinvalidstyleself)


****************************************************
### From metric_conv.models
* [digital_space_conversion(input_value: float, input_index: int, output_index: int) -> float](#digitalspaceconversioninputvalue:-float-inputindex:-int-outputindex:-int---float)

* [length_conversion(input_value: float, input_index: int, output_index: int) -> float](#lengthconversioninputvalue:-float-inputindex:-int-outputindex:-int---float)

* [time_conversion(input_value: float, input_index: int, output_index: int) -> float](#timeconversioninputvalue:-float-inputindex:-int-outputindex:-int---float)

* [weight_conversion(input_value: float, input_index: int, output_index: int) -> float](#weightconversioninputvalue:-float-inputindex:-int-outputindex:-int---float)


****************************************************
### From metric_conv.views
* [Class MetricConvUI](#class-metricconvui)

	* [MetricConvUI.\_\_init\_\_(self)](#metricconvuiinitself)

* [Class MetricConvWidget](#class-metricconvwidget)

	* [MetricConvWidget.\_\_init\_\_(self, stringLabel, unitOptions)](#metricconvwidgetinitself-stringlabel-unitoptions)

	* [MetricConvWidget._createOptionLayout(self, QLineEditObj, QComboBoxObj, items)](#metricconvwidgetcreateoptionlayoutself-qlineeditobj-qcomboboxobj-items)


****************************************************
### From metric_conv.test
* [Class TestWindowMetricConv](#class-testwindowmetricconv)

	* [TestWindowMetricConv.\_\_init\_\_(self)](#testwindowmetricconvinitself)

* [main_test_metric_conv()](#maintestmetricconv)


****************************************************
### From prime_gen.controllers
* [Class PrimeGenCtrl](#class-primegenctrl)

	* [PrimeGenCtrl.\_\_init\_\_(self, view, model)](#primegenctrlinitself-view-model)

	* [PrimeGenCtrl._copyAll(self, getFunction)](#primegenctrlcopyallself-getfunction)

	* [PrimeGenCtrl._checkInputBounds(self, inputLabel, minValue, maxValue)](#primegenctrlcheckinputboundsself-inputlabel-minvalue-maxvalue)

	* [PrimeGenCtrl._generateRange(self)](#primegenctrlgeneraterangeself)

	* [PrimeGenCtrl._generateRandom(self)](#primegenctrlgeneraterandomself)

	* [PrimeGenCtrl._IsPrimeCheck(self)](#primegenctrlisprimecheckself)

	* [PrimeGenCtrl._clearIcon(self)](#primegenctrlcleariconself)

	* [PrimeGenCtrl._connectSignals(self)](#primegenctrlconnectsignalsself)


****************************************************
### From prime_gen.models
* [digit_size(digits: int, total: int)](#digitsizedigits:-int-total:-int)

* [is_prime(n: int)](#isprimen:-int)

* [range_1_n(limit: int)](#range1nlimit:-int)


****************************************************
### From prime_gen.views
* [Class IsPrime](#class-isprime)

	* [IsPrime.\_\_init\_\_(self)](#isprimeinitself)

	* [IsPrime._CreateIsPrimeHeader(self)](#isprimecreateisprimeheaderself)

	* [IsPrime._CreateIsPrimeInput(self)](#isprimecreateisprimeinputself)

	* [IsPrime._CreateIsPrimeOutput(self)](#isprimecreateisprimeoutputself)

* [Class PrimeGenUI](#class-primegenui)

	* [PrimeGenUI.\_\_init\_\_(self)](#primegenuiinitself)

* [Class PrimeRandomGen](#class-primerandomgen)

	* [PrimeRandomGen.\_\_init\_\_(self)](#primerandomgeninitself)

	* [PrimeRandomGen._CreateRandomHeader(self)](#primerandomgencreaterandomheaderself)

	* [PrimeRandomGen._CreateRandomInput(self)](#primerandomgencreaterandominputself)

	* [PrimeRandomGen._CreateRandomButtons(self)](#primerandomgencreaterandombuttonsself)

	* [PrimeRandomGen.setRandomOutput(self, text)](#primerandomgensetrandomoutputself-text)

	* [PrimeRandomGen.getRandomOutput(self)](#primerandomgengetrandomoutputself)

	* [PrimeRandomGen.clearRandomOutput(self)](#primerandomgenclearrandomoutputself)

* [Class PrimeRangeGen](#class-primerangegen)

	* [PrimeRangeGen.\_\_init\_\_(self)](#primerangegeninitself)

	* [PrimeRangeGen._CreateRangeHeader(self)](#primerangegencreaterangeheaderself)

	* [PrimeRangeGen._CreateRangeInput(self)](#primerangegencreaterangeinputself)

	* [PrimeRangeGen._CreateRangeButtons(self)](#primerangegencreaterangebuttonsself)

	* [PrimeRangeGen.setRangeOutput(self, text)](#primerangegensetrangeoutputself-text)

	* [PrimeRangeGen.getRangeOutput(self)](#primerangegengetrangeoutputself)

	* [PrimeRangeGen.clearRangeOutput(self)](#primerangegenclearrangeoutputself)

* [Class ScrollLabel](#class-scrolllabel)

	* [ScrollLabel.\_\_init\_\_(self)](#scrolllabelinitself)

	* [ScrollLabel.setText(self, text)](#scrolllabelsettextself-text)

	* [ScrollLabel.text(self)](#scrolllabeltextself)


****************************************************
### From prime_gen.test
* [Class TestWindowPrimeGen](#class-testwindowprimegen)

	* [TestWindowPrimeGen.\_\_init\_\_(self)](#testwindowprimegeninitself)

* [main_test_prime_gen()](#maintestprimegen)


****************************************************
### From temp_conversion.temp_conv_logic
* [Class temp_Ui](#class-tempui)

	* [temp_Ui.\_\_init\_\_(self)](#tempuiinitself)

	* [temp_Ui.enterButtonPressed(self)](#tempuienterbuttonpressedself)

	* [temp_Ui.convert_temp(self, val, original_unit, unit_to_convert_to)](#tempuiconverttempself-val-originalunit-unittoconvertto)


****************************************************
# From main


****************************************************
## __class MultiCalcWindow__
Primary Widget for App. Initializes Window and Main and Sec Calc Widgets.
Loads stylesheet for entire app. 

Inhereits all methods and attributes from QMainWindow

Attributes
----------
__generalLayout : QHBoxWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stores the layout of the main

___centralWidget : QWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains central widget bound to self

__mainCalc : MainCalcUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Main Calc Widget

__secCalc : SecCalc__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sec Calc Widget

Methods
-------
__None__



****************************************************
## __MultiCalcWindow.\_\_init\_\_(self)__
Initilizer for App. Sets window size, title, loads style sheet,
and initializes Main Calc and Sec Calc widgets

Parameters
----------
__None__

Returns
-------
__MultiCalcWindow__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Main application



****************************************************

****************************************************
## __class SecCalc__
Secondary calc widget display and handler. Controls which widget to render based 
on MainCalcUI's combobox current index value.

Inhereits all methods and attributes from QStackedWidget

Attributes
----------
__option : {"QWidget's Name", QWidget}__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores QWidget options for secondary display, including their name and

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reference to their class.

Methods
-------
__secCalcDisplay(i):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets the index for the corresponding widget to display



****************************************************
## __SecCalc.\_\_init\_\_(self)__
Initializes the widget, and list from DROPBOX_MENU

Parameters
----------
__None__

Returns
-------
__SecCalc__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __SecCalc.secCalcDisplay(self, i)__
Changes which Widget to render

Parameters
----------
__i : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index of selected widget

Returns
-------
__None__



****************************************************
## __main()__
Main drivers that initializes PyQt5 application, creates a the calculator,
as well as controllers for specific widgets.

Parameters
----------
__None__

Returns
-------
__None__


****************************************************
# From ascii_conversion.views


****************************************************
## __class ascii_Ui__
Creates a QWidget that converts between a decimal, hexidecimal, and ASCII character value
Also creates signals, and conversion calculations

Inhereits all methods and attributes from QWidget

Attributes
----------
__button : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button to initiate conversion

__input : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input text field

__validators : [QValidators]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to determine which validations to apply on input, based on the

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;radioButtons selection

__output : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output text field

__radioButtons : [QRadioButtons]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list containing all the radiobuttons in the widget.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 - Char (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 - Decimal (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 - Hexadecimal (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 - Char (Output)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 - Decimal (Output)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 - Hexadecimal (Output)

Methods
-------
___createValidators():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a list of three different validators for chr, int, and hex input

___rangeValidator():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets roof range input for dec and hex. Changes to the input text if input value

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exceeds the range for chr() (1,114,111). Called every time input changes.

___setValidators():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Signal handler to change validation method when radiobuttons input selection changes

__printButtonPressed():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends input to convert_ascii then sets the results to output

__convert_ascii(val, input_unit, output_unit):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take the string of val and converts from input_unit to output_unit



****************************************************
## __ascii_Ui.\_\_init\_\_(self)__
Initializes the ascii_Ui, including it's layout from basic.ui, attributes, and
signal connections

Parameters
----------
__None__

Returns
-------
__ascii_Ui__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __ascii_Ui.\_createValidators(self)__
Creates a list of three different validators for chr, int, and hex input

Parameters
----------
__None__

Returns
-------
__[QRegExpValidator, QIntValidator, QRegValidator]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three different validators for chr, int, and hex input



****************************************************
## __ascii_Ui.\_rangeValidator(self)__
Sets roof range input for dec and hex. Changes to the input text if input value
exceeds the range for chr() (1,114,111). Called every time input changes.

If a ValueError occurs, likely for trying to int type cast an empty string,
does no operation.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __ascii_Ui.\_setValidators(self)__
Signal handler to change validation method when radiobuttons input selection changes

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __ascii_Ui.printButtonPressed(self)__
Sends input to convert_ascii then sets the results to output

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __ascii_Ui.convert_ascii(self, val, input_unit, output_unit)__
Take the string of val and converts from input_unit to output_unit

If at any point during the type conversions fail (ValueError), usually casting empty strings,
set output to "Invalid Input"

Parameters
----------
__val : int, str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input value to convert

__input_unit : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The input value input

__output_unit : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The desired converted output

Returns
-------
__int, str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Final conversion results.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type depends if converting to decimal or hexadecimal/char.



****************************************************
# From base_conv.controllers


****************************************************
## __class BaseConvCtrl__
Handles the logic and singal connections for BaseConvUI

Attributes
----------
___view : BaseConvUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the BaseConvUI widget

___model : module__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference base_conv/models.py with validator, formating, and calculating

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions

___bitLimits : [(int, int)]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores tuples of the roof/limit for each of the 4 bit widths, with the first tiple

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;being the limit for unsigned, and the second for signed

___signed : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 for unsigned, 1 for signed, used for accessing the appropriate tuple index

Methods
-------
___decChanged():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handler for when the decimal textbox is changed. Calls conversion and format

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions for every base, and sends the results to their respective outputs.

___hexChanged():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handler for when the hexadecimal textbox is changed. Calls conversion and format

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions for every base, and sends the results to their respective outputs.

___binChanged():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handler for when the binary textbox is changed. Calls conversion and format

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions for every base, and sends the results to their respective outputs.

___setSigned():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handler for when the signed/unsigned radio buttons change. Calls conversion and

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format functions for every base, and sends the results to their respective outputs.

___setNegate():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Toggles negation of a number and changed every textbox. Calls conversion and format

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions for every base, and sends the results to their respective outputs.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_connectTextSignals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects textbox textHasChanged signals.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_disconnectTextSignals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Disconnects textbox textHasChanged signals.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_setAllTextBoxes(decOutput, hexOutput, binOutput)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Disables textbox signals, sets the text, then re-enables them.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_connectBitSignals()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects the dropbox and radio buttons to handle changes in their state.



****************************************************
## __BaseConvCtrl.\_\_init\_\_(self, view, model)__
Constructs the BaseConvCtrl, constructing signals for BaseConvUI and connecting
them to the correct model/function for conversion calculations

Parameters
----------
__view : BaseConvUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to reference and connect BaseConvUI's attributes

__model : module__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to base_conv/models.py with validator, formating, and calculating

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;functions

Returns
-------
__BaseConvUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects BaseConvUI to the appropriate signals



****************************************************
## __BaseConvCtrl.\_decChanged(self)__
Handles the input of the Decimal field
1. Validates the number
2. Formats to decimal
3. Formats the value to hexadecimal
4. Formats the value to binary
4. Sets the input for all three fields with their respective formatted value

If a ValueError occurs when formatting the three with an invalid string or type,
typically null strings, no formatting is done

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_hexChanged(self)__
Handles the input of the Hexadecimal field
1. Validates the number
2. Formats the hexadecimal value
3. Formats the value to decimal
4. Formats the value to binary
4. Sets the input for all three fields with their respective formatted value

If a ValueError occurs when formatting the three with an invalid string or type,
typically null strings, no formatting is done

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_binChanged(self)__
Handles the input of the Binary field
1. Validates the number
2. Formats the binary value
3. Formats the value to decimal
4. Formats the value to hexadecimal
4. Sets the input for all three fields with their respective formatted value

If a ValueError occurs when formatting the three with an invalid string or type,
typically null strings, no formatting is done

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_setSigned(self)__
Sets _signed based on signage selection from the QRadioButtons. Will also disable the
negate button if _signed is 1/True. Immediately calls for conversion and changes out
once set.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_setNegate(self)__
Adds a '-' to decTextBox then sets the textbox, causing conversion to happen automatically
If a '-' is already there, it is trimmed and the conversion is triggered again

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_connectTextSignals(self)__
Connects decTextBox, hexTextBox, and binTextBox textChanged signals

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_disconnectTextSignals(self)__
Disconnects decTextBox, hexTextBox, and binTextBox textChanged signals

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_setAllTextBoxes(self, decOutput, hexOutput, binOutput)__
Sets decTextBox, hexTextBox, and binTextBox to their respective output. Disconnects
signals first, then reconnects after setting text.

Parameters
----------
__decOutput : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decTextBox's new text value

__hexOutput : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hexTextBox's new text value

__binOutput : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;binTextBox's new text value

Returns
-------
__None__



****************************************************
## __BaseConvCtrl.\_connectBitSignals(self)__
Connects bitDropBox, unSignedRadio and negateButton to their respective signals,
listening to any changes in their state.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************

****************************************************
# From base_conv.models

## __binFormatter(stringNumber, bit)__
Formats a binary string to have a space every 4 digits

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string number to convert to int, base 2, then to convert to bin

__bit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of bit-width for bit shifting

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Binary number with spaces (ie 10 1010 1100)


****************************************************
## __binValidator(stringNumber, limit, isSigned)__
Validates a binary number in string form:
- If a negative sign in the beginning only if isSigned is enabled
- Uses RegExp to confirm input is only digits
- Splits at the spaces and merges into a legal binary number
- Checks if it's in the limit bounds and manipulates to the limit

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string representation of an binary number with a space every four digits

__limit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roof limit of the number based on signage and bit-width

__isSigned : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 for false, 1 for true

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A valid hex number that can be used for formatting and conversion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to other bases


****************************************************
## __decFormatter(stringNumber)__
Formats a decimal number in string form to have thousands place commas

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal number in string form

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integer with commas (ie, 104,532)


****************************************************
## __decValidator(stringNumber, limit, isSigned)__
Validates a decimal number in string form:
- If a negative sign in the beginning of string number, isSigned is enabled
- Uses RegExp to confirm input is only digits
- Splits at the commas and merges into a legal int number
- Checks if it's in the limit bounds and manipulates based on limit:
    if signed: floor is negative of limit minus 1
    if unsigned: floor is zero

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string representation of an decimal number with thousandths place commas

__limit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roof limit of the number based on signage and bit-width

__isSigned : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 for false, 1 for true

Returns
-------
__int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A valid int number that can be used for formatting and conversion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to other bases


****************************************************
## __hexFormatter(stringNumber, bit)__
Formats a hexadecimal string to have a space every 4 digits

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string number to convert to int, base 16, then to convert to hex

__bit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of bit-width for bit shifting

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hexadecimal with spaces (ie 10 1FA9 032A)


****************************************************
## __hexValidator(stringNumber, limit, isSigned)__
Validates a hexadecimal number in string form:
- If a negative sign in the beginning only if isSigned is enabled
- Uses RegExp to confirm input is only digits
- Splits at the spaces and merges into a legal hex number
- Checks if it's in the limit bounds and manipulates to the limit

Parameters
----------
__stringNumber : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string representation of an hexadecimal number with a space every four digits

__limit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roof limit of the number based on signage and bit-width

__isSigned : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 for false, 1 for true

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A valid hex number that can be used for formatting and conversion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to other bases


****************************************************
## __rightToLeftInsertion(string, position, insertChar)__
Formats a string to insert a character at every <position> place

Parameters
----------
__string : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original string to manipulate

__position : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Every nth space, insert a character into that space

__insertChar : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The character or str to insert at that place

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly moddified string


****************************************************
## __signedBaseToInt(value, bits)__
Takes an int value in hex or bin representation and performs a bit shift by bits value
to convert to an int value with base 10

Parameters
----------
__value : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer value with hex or bin base to convert to decimal

__bits : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of bit shift to perform

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;will be either 8, 16, 32, or 64

Returns
-------
__int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns value converted to decimal


****************************************************
## __signedIntToBase(value, bits, base)__
Takes an int value and performs a bit shift by bits value
Then convert it to the base unit

Parameters
----------
__value : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integer value to convert to specified base

__bits : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of bit shift to perform

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;will be either 8, 16, 32, or 64

__base : hex()/bin()__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to convert to either of the two bases

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns value converted to hex or binary in str form


****************************************************
# From base_conv.views


****************************************************
## __class BaseConvUI__
A QWidget that creates the three main number bases of decimal, hexadecimal, and binary
base UI widgets and layout. Also creates the layout for signed/unsigned QRadioButtons,
a negate QPushButton, and QComboBox for bit-width selection.

Inherits all methods and attributes from QWidget

Attributes
----------
__unsignedRadio : QRadioButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radiobutton input for unsigned

__signedRadio : QRadioButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Radiobutton input for signed

__negateBUtton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;button to negate values

__bitDropBox : QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropbox menu selection for 8, 16, 32, or 64 bit widths

__dec : DecBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DecBase Widget

__hex : HexBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HexBase Widget

__bin : BinBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BinBase Widget

Methods
-------
___createBitLengthBox():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Internal method to create QComboBox with 8-64 bit options



****************************************************
## __BaseConvUI.\_\_init\_\_(self)__
Initializer for BaseConvUI. Creates all QWidgets and layouts

Parameters
----------
__None__

Returns
-------
__BaseConvUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initalized BaseConvUI view



****************************************************
## __BaseConvUI.\_createBitLengthBox(self)__
Internal method for creating a QComboBox with 8-64 bit-width options

Parameters
----------
__None__

Returns
-------
__QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dropbox of various bit-widths



****************************************************

****************************************************
## __class BinBase__
A binary base input/output widget

Inherits all methods and attributes from NumBase

Attributes
----------
__binHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text for the header

__binTextBox : QPlainTextEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input/output text field

Methods
-------
__None__



****************************************************
## __BinBase.\_\_init\_\_(self)__
Initializer for BinBase

Parameters
----------
__None__

Returns
-------
__BinBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initalized BinBase object



****************************************************

****************************************************
## __class DecBase__
A decimal base input/output widget

Inherits all methods and attributes from NumBase

Attributes
----------
__decHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text for the header

__decTextBox : QPlainTextEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input/output text field

Methods
-------
__None__



****************************************************
## __DecBase.\_\_init\_\_(self)__
Initializer for DecBase

Parameters
----------
__None__

Returns
-------
__DecBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initalized DecBase object



****************************************************

****************************************************
## __class HexBase__
A hexadecimal base input/output widget

Inherits all methods and attributes from NumBase

Attributes
----------
__hexHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text for the header

__hexTextBox : QPlainTextEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input/output text field

Methods
-------
__None__



****************************************************
## __HexBase.\_\_init\_\_(self)__
Initializer for HexBase

Parameters
----------
__None__

Returns
-------
__HexBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initalized HexBase object



****************************************************

****************************************************
## __class NumBase__
A QWidget that contains the foundation for three different base unit headers

Inherits all methods and attributes from QWidget

Attributes
----------
__None__

Methods
-------
___CreateNumHeader(headerText):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel with the text from headerText

___CreateNumTextBox():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QPlainTextEdit widget for input/output



****************************************************
## __NumBase.\_\_init\_\_(self)__
Constructs a NumBase widget, inheriting all of QWidget's methods and attributes

Parameters
----------
__None__

Returns
-------
__NumBase__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialized NumBase object



****************************************************
## __NumBase.\_CreateNumHeader(self, headerText)__
Constructs a QLabel header with headerText

Parameters
----------
__headerText : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input string

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A QLabel header



****************************************************
## __NumBase.\_CreateNumTextBox(self)__
Constructs a QPlainTextEdit widget

Parameters
----------
__None__

Returns
-------
__QPlainTextEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QPlanTextEdit object to be used for input/output



****************************************************
# From base_conv.test


****************************************************
## __class TestWindowBaseConv__
Constructs a QMainWindow to create and append to it's window a BaseConvUI
widget for testing purposes

Inherits all methods and attributes from QMainWindow

Attributes
----------
__generalLayout : QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stores the layout of the main

___centralWidget : QWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains central widget bound to self

__metricConvUI : BaseConvGenUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initializes and stores BaseConvGenUI

Methods
-------
__None__



****************************************************
## __TestWindowBaseConv.\_\_init\_\_(self)__
Initilizer for TestWindow

Parameters
----------
__None__

Returns
-------
__TestWindow__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the central widget for main application



****************************************************
## __main_test_base_conv()__
Main drivers that initializes PyQt5 application, creates a TestWindow widget,
and BaseConvCtrl object to connect to signals.

Parameters
----------
__None__

Returns
-------
__None__


****************************************************
# From birthday_conversion.views


****************************************************
## __class birthday_Ui__
Creates a QWidget where the user can put in a previous date (such as a birthday), and see how
many years, months, or days have elapsed since then.

Inhereits all methods and attributes from QWidget

Attributes
----------
__button : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to submit inputs

__inputMonth : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line input field for numerical month (1-12)

__inputDay : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line input field for numerical day (1-31)

__inputYear : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line input field for numerical year (1-yearLimit)

__yearLimit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retrieves and stores the current year

__lineEdit_Year : Qline__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for int input having 4 digits representing years.

Methods
-------
___inputCheck():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Performs a date validation check for the input fields every time the

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user changes the input. Performs limit checks on fields based on

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;month and year.

__enterButtonPressed():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends a list input that contains [month,day,year] from user input

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to get_birthday then sets the text of output to the results.

__get_birthday(combo_input, calendar_input):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Takes in a list of uuser's date input, creates a date object with it,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;then looks at the combo box's type selection and sends to appropriate

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;convert function.



****************************************************
## __birthday_Ui.\_\_init\_\_(self)__
Initializes the birthday_Ui, including it's layout from basic.ui and attributes

Parameters
----------
__None__

Returns
-------
__birthday_Ui__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __birthday_Ui.\_inputCheck(self)__
Performs a date validation check for the input fields every time the
user changes the input. Performs limit checks on fields based on
month and year.

If a ValueError occurs during input checks for inputDays, likely because other
fields are blank, the limit falls on certain defaults like 31 or 28.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __birthday_Ui.enterButtonPressed(self)__
Sends a list input that contains [month,day,year] from user input
to get_birthday then sets the text of output to the results.

If a ValueError occurs, likely if certain input fields are empty,
submission is ignored.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __birthday_Ui.get_birthday(self, combo_input, calendar_input)__
Takes in a list and a choice input from the combo box for the type of conversion the user wants
Years, Months, Days and returns the conversion in text.

If the user entered a date that is outside of a valid date range (ValueError),
sets output to "Invalid".

Parameters
----------
__combo_input : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input choice from the combo box depending on the conversion user picks.

__calender_input : [int]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List of numeric date inputs from the user            

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elapsed time results in desired units, as a string



****************************************************
## __get_days(month, day, year)__
Takes in three int values that represents a specific day (such as a birthday)
and calculates elapsed days based on today.

Parameters
----------
__month : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric month value (1-12)

__day : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric day value (1-31)

__year : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric year value (1-present year)

Returns
-------
__int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elapsed days


****************************************************
## __get_months(month, day, year)__
Takes in three int values that represents a specific day (such as a birthday)
and calculates elapsed months based on today.

Parameters
----------
__month : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric month value (1-12)

__day : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric day value (1-31)

__year : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric year value (1-present year)

Returns
-------
__int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elapsed months


****************************************************
## __get_years(month, day, year)__
Takes in three int values that represents a specific day (such as a birthday)
and calculates elapsed years based on today.

Parameters
----------
__month : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric month value (1-12)

__day : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric day value (1-31)

__year : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Numeric year value (1-present year)

Returns
-------
__int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elapsed years


****************************************************
# From prime_gen.views


****************************************************
## __class IsPrime__
Creates a QWidget that determines if a number is prime or now

Inherits all methods and attributes from QWidget

Attributes
----------
__isPrimeHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__isPrimeLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Instructional text for isPrime widget

__isPrimeInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input box for isPrime

__isPrimeButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text input field

__isPrimeIcon : QSvgWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SVG Image to show if a number is prime or not

__isPrimeText : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text confirming if a number is prime or not

__primeRangeOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateIsPrimeHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the isPrimeHeader

___CreateIsPrimeInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a a layout and isPrimeLabel, isPrimeInput, and isPrimeButton

___CreateIsPrimeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input



****************************************************
## __IsPrime.\_\_init\_\_(self)__
Initilizer for isPrime

Parameters
----------
__None__

Returns
-------
__isPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __IsPrime.\_CreateIsPrimeHeader(self)__
Creates a QLabel text header

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header text



****************************************************
## __IsPrime.\_CreateIsPrimeInput(self)__
Creates a layout with QLabel, QLineEdit, and QPushButton for isPrime

Parameters
----------
__None__

Returns
-------
__QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout of input and submit widgets



****************************************************
## __IsPrime.\_CreateIsPrimeOutput(self)__
Creates a QVBoxLayout with widgets for output results

Parameters
----------
__None__

Returns
-------
__QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Icon and Text



****************************************************

****************************************************
## __class PrimeGenUI__
Creates the core Prime Gen UI. Creates a tabs window, with each item being a
PrimeRangeGen widget, PrimeRandomGen widget, and IsPrime widget.

Inherits all methods and attributes from QWidget

Attributes
----------
__tabs : QTabWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tabs containing all the widgets

__primeRangeGen : PrimeRangeGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates PrimeRangeGen View

__primeRandomGen : PrimeRandomGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates PrimeRandomGen view

__isPrime : IsPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates IsPrime view

Methods
-------
__None__



****************************************************
## __PrimeGenUI.\_\_init\_\_(self)__
Initilizer for PrimeGenUI. Creates Tab window with all three prime gen widgets

Parameters
----------
__None__

Returns
-------
__IsPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************

****************************************************
## __class PrimeRandomGen__
Creates a Prime Number Generator QWidget that generates a specificied amount of
random prime numbers with a specificied number of digits from user input

Inherits all methods and attributes from QWidget

Attributes
----------
__randomHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__randomDigitLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label for Digit Input

__randomAmountLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label for Amount of numbers input

__randomDigitInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text input for number of digits

__randomAmountInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text input for how many random numbers

__randomGenButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button

__randomGenCopy : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copies output to clipboard

__randomGenClear : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears output text

__randomNumOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateRandomHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the randomHeader

___CreateRandpomInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a various QLineEdit object with validators and other settings

___CreateRandomButtons():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input

__setRandomOutput(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the output text of randomNumOutput

__getRandomOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns the output text of randomNumOutput

__clearRandomOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears the output text of randomNumOutput



****************************************************
## __PrimeRandomGen.\_\_init\_\_(self)__
Initilizer for PrimeRandomGen

Parameters
----------
__None__

Returns
-------
__PrimeRandomGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __PrimeRandomGen.\_CreateRandomHeader(self)__
Creates a QLabel text header

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header text



****************************************************
## __PrimeRandomGen.\_CreateRandomInput(self)__
Creates a layout with QLineEdit input text fields with instructions

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout of text input fields



****************************************************
## __PrimeRandomGen.\_CreateRandomButtons(self)__
Creates a QHBoxLayout of various QPushButtons

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Genereate, Copy All, and Clear buttons



****************************************************
## __PrimeRandomGen.setRandomOutput(self, text)__
Changes the text of randomNumOutput

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input of new text

Returns
-------
__None__



****************************************************
## __PrimeRandomGen.getRandomOutput(self)__
Returns randomNumOutput's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;randomNumOutput's text



****************************************************
## __PrimeRandomGen.clearRandomOutput(self)__
Changes the text of randomNumOutput to an empty string

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************
## __class PrimeRangeGen__
Creates a Prime Number Generator QWidget that generates based on the range
from 1 to a user inputted positive integer

Inherits all methods and attributes from QWidget

Attributes
----------
__rangeHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__rangeInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text input field

__rangeGenButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button to generate input

__rangeGenCopy : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copys results to clipboard

__rangeGenClear : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears output text

__primeRangeOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateRangeHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the rangeHeader

___CreateRangeInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLineEdit object with validators and other settings

___CreateRangeButtons(self):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input

__setRangeOutput(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the output text of primeRangeOutput

__getRangeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns the output text of primeRangeOutput

__clearRangeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears the output text of primeRangeOutput



****************************************************
## __PrimeRangeGen.\_\_init\_\_(self)__
Initilizer for PrimeRangeGen

Parameters
----------
__None__

Returns
-------
__PrimeRangeGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __PrimeRangeGen.\_CreateRangeHeader(self)__
Creates a QLabel text with instruction limits

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header/instructional text



****************************************************
## __PrimeRangeGen.\_CreateRangeInput(self)__
Creates a QLineEdit input field

Parameters
----------
__None__

Returns
-------
__QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primeRangeInput field



****************************************************
## __PrimeRangeGen.\_CreateRangeButtons(self)__
Creates a QHBoxLayout of various QPushButtons

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Genereate, Copy All, and Clear buttons



****************************************************
## __PrimeRangeGen.setRangeOutput(self, text)__
Changes the text of primeRangeGenOutput

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input of new text

Returns
-------
__None__



****************************************************
## __PrimeRangeGen.getRangeOutput(self)__
Returns primeRangeGenOutput's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primeRangeOutput's text



****************************************************
## __PrimeRangeGen.clearRangeOutput(self)__
Changes the text of primeRangeGenOutput to an empty string

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************
## __class ScrollLabel__
Custom setup of a QScrollArea to create a read-only Scroll Label for Prime Gen Output

Inherits all methods and attributes from QScrollArea

Attributes
----------
__label : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the text content of the object

Methods
-------
__setText(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes label's text with text

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns label's text



****************************************************
## __ScrollLabel.\_\_init\_\_(self)__
Construct A ScrollLabel with certain properties

Parameters
----------
__label : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to store text for the ScrollArea

Returns
-------
__ScrollArea__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __ScrollLabel.setText(self, text)__
Sets the text of label

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input for the label to change to

Returns
-------
__None__



****************************************************
## __ScrollLabel.text(self)__
Returns the string of label's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label's text



****************************************************
# From main_calc.controllers


****************************************************
## __class MainCalcCtrl__
Handles the logic and singal connections for MainCalcUI. Retrieves user input to
perform operations or send to other functions for evaluation.

Also controls the secondary calculator widget display

Attributes
----------
___evaluate : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to evaluation function

___view : MainCalcUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to MainCalcUI and it's widgets

___evalPressed : Boolean__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handled submission state. Default is False.

Methods
-------
___calculateResult():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sends expression built so far to evaluation function.

___buildExpression(keyInput):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Handler for any building expression via the calculator buttons.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dictates certain behavior to optimize use (such as not inputing

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;consecutive operators)

___changeSecCalc():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes sec calc display based on combo box index

___connectSignals():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects buttons and output to their respective handlers



****************************************************
## __MainCalcCtrl.\_\_init\_\_(self, model, view)__
Initilizer for MainCalcCtrl. Connects signals to their handlers.

Parameters
----------
__model : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to reference function for evaluation

__view : MainCalcUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to ManCalcUI and it's UI widgets.

Returns
-------
__MainCalcCtrl__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Control object for MainCalcUI



****************************************************
## __MainCalcCtrl.\_calculateResult(self)__
Sets _evalPressed to True and sends built expression to be evaluated

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MainCalcCtrl.\_buildExpression(self, keyInput)__
Handler for MainCalcUI's button to build expression. Performs certain input handling:
- Reset expression if previous result was "ERROR"
- Proper decimal point input

Parameters
----------
__keyInput : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String of button pressed

Returns
-------
__None__



****************************************************
## __MainCalcCtrl.\_changeSecCalc(self)__
Sets the widget to be used for the secondary display.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MainCalcCtrl.\_connectSignals(self)__
Connects the buttons and output signals to their proper handlers.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************

****************************************************
# From main_calc.models

## __astTransversal(astObj)__
Abstract syntax tree transversal for basic math/eval expressions.
Recursive function that calculates an expression based on end nodes,
then returns its value for higher nodes to calcuate their expressions.

Parameters
----------
__astObj : Abstract syntax tree object__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Expected ast.Constant, ast.BinOp, and ast.UnaryOp types

Raises
------
__TypeError__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If astObj is not a constant, binOp or unaryOp, thus not

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a basic eval math expression

Returns
-------
__int, float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Final evaluated expression


****************************************************
## __evaluateExpression(expression)__
Driver for abstract syntax tree transversal for basic math/eval expressions.
ast.parses expression with eval mode, sending it's body to astTransversal
for safe math evaluation.

If SyntaxErorr, ZeroDivisionError, or TypeError, sends results as "ERROR"

Parameters
----------
__express : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full math expression in str form

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Final evaluated expression


****************************************************
# From main_calc.views


****************************************************
## __class MainCalcUI__
A QWidget that creates the interface widget of a standard calculator that performs
basic functions, such as add, subtract, divide, multiply, floor division, etc.

Aside from the main calculator, also has a dropbox for a secondary calculator widget.

Inherits all methods and attributes from QWidget

Attributes
----------
__calcOutput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Main calc display for expression building and evaluation output

__calcDropBox : QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Secondary calc option menu

__buttons : [QPushButton]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list of QPushButton objects, each one a button for the calculator

Methods
-------
___createCalcOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates QLineEdit object for calc output display

___createDropBox(dropMenu):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates QComboBox with list of dropMenu options

___createButtons():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates buttons in QGridLayout

__setCalcOutput(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes calcOutput to text argument

__getCalcOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns calcOutput text value

__backSpaceCalcOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes last input character in expression

__clearCalcOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets calcOutput to "0"



****************************************************
## __MainCalcUI.\_\_init\_\_(self, dropMenu)__
Initializer for MainCalcUI. Creates all QWidgets and layouts.

Parameters
----------
__dropMenu : [str]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List of different widgets for the secondary calc display

Returns
-------
__MainCalcUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initalized MainCalcUI



****************************************************
## __MainCalcUI.\_createCalcOutput(self)__
Creates a QLineEdit object for calcOutput

Parameters
----------
__None__

Returns
-------
__QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;calcOutput with alignment defaults



****************************************************
## __MainCalcUI.\_createDropBox(self, dropMenu)__
Creates a QComboBox for calcDropBox

Parameters
----------
__dropMenu: [str]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List of possible secondary calc widgets to display

Returns
-------
__QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialized and set up QComboBox for calcDropBox



****************************************************
## __MainCalcUI.\_createButtons(self)__
Creates a all the QPushButtons for the calculator for expression
building

Parameters
----------
__None__

Returns
-------
__QGridLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialized placement setup for QPushButtons



****************************************************
## __MainCalcUI.setCalcOutput(self, text)__
Sets calcOutput text display

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New text to change to

Returns
-------
__None__



****************************************************
## __MainCalcUI.getCalcOutput(self)__
Returns calcOutput's text value

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Current calcOutput's text value



****************************************************
## __MainCalcUI.backSpaceCalcOutput(self)__
Reset calcOutput's text to "0" when output is empty.
Else removes the last character from the str.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MainCalcUI.clearCalcOutput(self)__
Reset calcOutput's text to "0" when output is empty.
Else removes the last character from the str.

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
# From metric_conv.controllers


****************************************************
## __class MetricConvCtrl__
Handles the logic and signal connections for the MetricConvUI

Attributes
----------
___view : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the QWidget

___model : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the specific function for calculations

Methods
-------
___connectComboBoxSignals():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects MetricConvWidget's QComboBoxs' signal whenever their current index changes

___connectTextSignals():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects MetricConvWidget's QLineEdits' signal whenever their text changes

___disconnectTextSignals():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Disconnects MetricConvWidget's QLineEdits' signal

___setTextFields(inputField, outputField, inputString, outputString):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes inputField and outputField's text with outputString by disconnecting

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;their text signals, sets their text, and reactivates the signals

___textChanged(inputField, outputField, inputMenu, outputMenu):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Passes the text of inputField and the indexes of inputMenu and outputMenu to be

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;calculated by _model.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Activates when a user changes the text of the QLineEdits or changes the current index

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of the QComboBoxs

___toggleValidStyle():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the object name for the left/rightTextEdit fields to valid, and loads stylesheet

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_toggleInvalidStyle()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the object name for the left/rightTextEdit fields to invalid, and loads stylesheet



****************************************************
## __MetricConvCtrl.\_\_init\_\_(self, view, model)__
Constructs the MetricConvCtrl, building signals for MetricConvWidget and connecting
them to the correct model/function for conversion calculations

Parameters
----------
__view : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to reference and connect MetricConvWidget's attributes

__model : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to the function to perform conversion calculations

Returns
-------
__MetricConvCtrl__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects MetricConvWidget to the appropriate signals



****************************************************
## __MetricConvCtrl.\_connectComboBoxSignals(self)__
Connects MetricConvWidget's QComboBoxs' signal whenever their current index changes

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_connectTextSignals(self)__
Connects MetricConvWidget's QLineEdits' signal whenever their text changes

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_disconnectTextSignals(self)__
Disconnects MetricConvWidget's QLineEdits' signal

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_setTextFields(self, inputField, outputField, inputString, outputString)__
Changes inputField and outputField's text with outputString by disconnecting
their text signals, sets their text, and reactivates the signals

Parameters
----------
__inputField : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to MetricConvWidget's left/rightTextField

__outputField : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to MetricConvWidget's left/rightTextField. Will always be the opposite

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of inputField

__inputString : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String to set for inputField's new text

__outputString : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String to set for outputField's new text

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_textChanged(self, inputField, outputField, inputMenu, outputMenu)__
Passes the text of inputField and the indexes of inputMenu and outputMenu to be
calculated by _model.
Activates when a user changes the text of the QLineEdits or changes the current index
of the QComboBoxs

Parameters
----------
__inputField : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to MetricConvWidget's left/rightTextField

__outputField : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to MetricConvWidget's left/rightTextField. Will always be the opposite

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of inputField

__inputMenu : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Index value for the current index of the input menu

__outputMenug : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Index value for the current index of the output menu

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_toggleValidStyle(self)__
Changes the object name for the left/rightTextEdit fields to valid, and loads stylesheet

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __MetricConvCtrl.\_toggleInvalidStyle(self)__
Changes the object name for the left/rightTextEdit fields to invalid, and loads stylesheet

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************

****************************************************
# From metric_conv.models

## __digital_space_conversion(input_value: float, input_index: int, output_index: int) -> float__
Calculates the conversion rate for different digital space units based on the input_index
and output_index from from the MetricConvWidget.

The different units are Bits, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Petabytes,
Exabytes, Zettabytes, Yottabytes

Parameters
----------
__input_value : float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The original numerical space value before conversion

__input_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the space unit of the input value.

__output_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the space unit that the input value will be converted to

Returns
-------
__float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The converted digital spacce measurement from input units to output's units


****************************************************
## __length_conversion(input_value: float, input_index: int, output_index: int) -> float__
Calculates the conversion rate for length distances based on the input_index and 
output_index from from the MetricConvWidget.

The different units include Inches, Feet, Yards, Miles, Millimeters, Centimeters,
Meters, Kilometers

Parameters
----------
__input_value : float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The original numerical length value before conversion

__input_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the length unit of the input value.

__output_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the length unit that the input value will be converted to

Returns
-------
__float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The converted length measurement from input units to output's units


****************************************************
## __time_conversion(input_value: float, input_index: int, output_index: int) -> float__
Calculates the conversion rate for different time units based on the input_index and 
output_index from from the MetricConvWidget.

The different units are Milliseconds, Seconds, Minutes, Hours, Days, Months, and Years

Parameters
----------
__input_value : float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The original numerical time value before conversion

__input_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the time unit of the input value.

__output_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the time unit that the input value will be converted to

Returns
-------
__float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The converted time measurement from input units to output's units


****************************************************
## __weight_conversion(input_value: float, input_index: int, output_index: int) -> float__
Calculates the conversion rate for different weights based on the input_index and 
output_index from from the MetricConvWidget.

The different units are Ounces, Pounds, Stone, Tons (Short), Milligrams, Grams,
Kilograms

Parameters
----------
__input_value : float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The original numerical weight value before conversion

__input_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the weight unit of the input value.

__output_index: int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The index of the weight unit that the input value will be converted to

Returns
-------
__float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The converted weight measurement from input units to output's units


****************************************************
# From metric_conv.views


****************************************************
## __class MetricConvUI__
A QWidget that the UI for the Metric Conversion option of the calculator.
Makes four different MetricConvWidget objects, one for length, weight,
time, and digital space.

Inherits all methods and attributes from QWidget

Attributes
----------

__lengthView : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QWidget for length conversion

__weightView : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QWidget for weight conversion

__timeView : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QWidget for time conversion

__sigitalStorageView : MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QWidget for digital space conversion

Methods
-------
__None__



****************************************************
## __MetricConvUI.\_\_init\_\_(self)__
Initializes the MetricConvUI, with 4 MetricConvWidget objects.
One for length, weight, time, and digital storage

Parameters
----------
__None__

Returns
-------
__MetricConvUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************

****************************************************
## __class MetricConvWidget__
A QWidget that has two QLineEdit text fields each with their own QComboBox for a list
of conversion options between the two sides.

Inherits all methods and attributes from QWidget

Attributes
----------
__leftTextEdit : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Left input/output field for conversion

__leftComboBox : QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Left side conversion unit options

__rightTextEdit : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Right input/output field for conversion

__rightComboBox : QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Right side conversion unit options

Methods
-------
___createOptionLayout(QLineEditObj, QComboBoxObj, items):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Internal method for initialization, used to create the layout and

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QComboBox



****************************************************
## __MetricConvWidget.\_\_init\_\_(self, stringLabel, unitOptions)__
Constructs a MetricConvWidget, including it's layout and attributes
Used perform unit conversion between two units

Parameters
----------
__stringLabel : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to create A QLabel for the MetricConvWidget object

__unitOptions: [str]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list of str objects, each one being a different measurement unit

Returns
-------
__MetricConvWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __MetricConvWidget.\_createOptionLayout(self, QLineEditObj, QComboBoxObj, items)__
Creates a QVBoxLayout for each side of the conversion, as well as settings for
left/rightTextEdit and left/rightComboBox data attributes

Parameters
----------
__QLineEditObj : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to the object's attribute for the left/rightTextEdit

__QComboBoxObj : QComboBox__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to the object's attributefor the left/rightComboBox

__items : [str]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list of str objects, each one being a different measurement unit

Returns
-------
__QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with QWidgets attached



****************************************************
# From metric_conv.test


****************************************************
## __class TestWindowMetricConv__
Constructs a QMainWindow to create and append to it's window a MetricConvUI
widget for testing purposes

Inherits all methods and attributes from QMainWindow

Attributes
----------
__generalLayout : QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stores the layout of the main

___centralWidget : QWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains central widget bound to self

__metricConvUI : MetricConvGenUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initializes and stores MetricConvGenUI

Methods
-------
__None__



****************************************************
## __TestWindowMetricConv.\_\_init\_\_(self)__
Initilizer for TestWindow

Parameters
----------
__None__

Returns
-------
__TestWindow__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the central widget for main application



****************************************************
## __main_test_metric_conv()__
Main drivers that initializes PyQt5 application, creates a TestWindow widget,
and 4 MetricConvCtrl objects to connect to four different MetricConvWidgets within
MetricConvUI, as well as the appropriate conversion functions from models.

Parameters
----------
__None__

Returns
-------
__None__


****************************************************
# From prime_gen.controllers


****************************************************
## __class PrimeGenCtrl__
Handles the logic and signal connections for the PrimeGenUI

Attributes
----------
___view : PrimeGenUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the QWidget of PrimeGenUI

___rangeGen : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the range_1_n function in prime_gen/models.py

___randomGen : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the digit_size function in prime_gen/models.py

___isPrime : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the reference to the is_prime function in prime_gen/models.py

Methods
-------
___copyAll(getFunction):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copys the text provided from the passed funtion in getFunction

___checkInputBounds(inputLabel, minValue, maxValue):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks the range of inputLabel.text() and modifies based on the minValue and maxValue

___generateRange():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates range based on rangeInput.text()

___generateRandom():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates random number based on randomDigitiInput.text() and randomAmountInput.text()

___IsPrimeCheck():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks if a number is prime based on on isPrimeInput.text()

___clearIcon():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears the file path for the SVG icon

___connectSignals():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects the signals for the QLineEdit and QPushButtons for all three Prime Gen Modes



****************************************************
## __PrimeGenCtrl.\_\_init\_\_(self, view, model)__
Constructs the PrimeGenCtrl, building signals for PrimeGenUI and connecting
them to the correct model/function for conversion calculations

Parameters
----------
__view : PrimeGenUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to reference and connect PrimeGenUI's attributes

__model : module__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reference to prime_gen/models.py, containing the generation/validation functions

Returns
-------
__PrimeGenCtrl__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connects PrimeGenUI to the appropriate signals



****************************************************
## __PrimeGenCtrl.\_copyAll(self, getFunction)__
Copys the text return by the passed getFunction for an output field

Parameters
----------
__getFunction : function__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the function that will return its respective get for an output value

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_checkInputBounds(self, inputLabel, minValue, maxValue)__
Checks to see if the value of int(inputLabel.text()) is between minValue and maxValue
Changes to empty string if it's lower than min, and to maxValue if higher than maxValue
Then sets inputLabel's text if it is out of those bounds

Parameters
----------
__inputLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QLabel of the respective input field

__minValue : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minumum value to validate the range

__maxValue : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum value to validate the range

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_generateRange(self)__
Calculates the prime numbers in a range from rangeInput.text()
Then sets rangeOutput's text to the results
Sets to "Please enter a value" if rangeInput.text() is empty

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_generateRandom(self)__
Calculates random prime numbers from randomDigitInput and randomAmountInput
Then sets randomOutput's text to the results
Sets to "Please enter a value" if either input is empty

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_IsPrimeCheck(self)__
Validates if a isPrime.text() is in fact a prime number, then outputs the results
with an SVG image and text
If input is empty, then the text asks for you to input a number

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_clearIcon(self)__
Clears the output results of isPrime, setting the image and text to empty

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __PrimeGenCtrl.\_connectSignals(self)__
Connects the various signals for primeRangeGen, primeRandomGen, and isPrime
Performs checkInputBounds for all input.textChanged
Performs their respective calculation on Button.clicked
Performs copying of output from Copy.clicked
Clear respective output from Clear.clicked

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************

****************************************************
# From prime_gen.models

## __digit_size(digits: int, total: int)__
Generate a set of random prime numbers by a digit size
Will generate a number number that has <digits> amount of digits
Then check if the number is prime
This prime number generator will continue finding random prime numbers
Until a <total> amount is found

Parameters
----------
__digits : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of digit places for each random number

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precondition, must be positive, non-zero integer

__total : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;how many random prime numbers to generate

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precondition, must be positive, non-zero integer

Returns
-------
__[int]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Results of randomly generated prime numbers


****************************************************
## __is_prime(n: int)__
Determines if a number is prime or not

Parameters
----------
__n : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precondition, n must be a positive integer

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number to test if prime

Returns
-------
__Boolean__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True if n is prime, False if not


****************************************************
## __range_1_n(limit: int)__
Finds all the prime numbers from 1 to <limit> (inclusive)
Generates numbers based off of the Sieve of Atkin algorithm 
ref: https://en.wikipedia.org/wiki/Sieve_of_Atkin

Parameters
----------
__limit : int__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Precondition, limit must be a positive, non-zero integer

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit of the range

Returns
-------
__[int], [str]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Final list of integers that are prime numbers

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If there are none, returns ["None"]


****************************************************
# From prime_gen.views


****************************************************
## __class IsPrime__
Creates a QWidget that determines if a number is prime or now

Inherits all methods and attributes from QWidget

Attributes
----------
__isPrimeHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__isPrimeLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Instructional text for isPrime widget

__isPrimeInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input box for isPrime

__isPrimeButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text input field

__isPrimeIcon : QSvgWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SVG Image to show if a number is prime or not

__isPrimeText : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text confirming if a number is prime or not

__primeRangeOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateIsPrimeHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the isPrimeHeader

___CreateIsPrimeInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a a layout and isPrimeLabel, isPrimeInput, and isPrimeButton

___CreateIsPrimeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input



****************************************************
## __IsPrime.\_\_init\_\_(self)__
Initilizer for isPrime

Parameters
----------
__None__

Returns
-------
__isPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __IsPrime.\_CreateIsPrimeHeader(self)__
Creates a QLabel text header

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header text



****************************************************
## __IsPrime.\_CreateIsPrimeInput(self)__
Creates a layout with QLabel, QLineEdit, and QPushButton for isPrime

Parameters
----------
__None__

Returns
-------
__QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout of input and submit widgets



****************************************************
## __IsPrime.\_CreateIsPrimeOutput(self)__
Creates a QVBoxLayout with widgets for output results

Parameters
----------
__None__

Returns
-------
__QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Icon and Text



****************************************************

****************************************************
## __class PrimeGenUI__
Creates the core Prime Gen UI. Creates a tabs window, with each item being a
PrimeRangeGen widget, PrimeRandomGen widget, and IsPrime widget.

Inherits all methods and attributes from QWidget

Attributes
----------
__tabs : QTabWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tabs containing all the widgets

__primeRangeGen : PrimeRangeGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates PrimeRangeGen View

__primeRandomGen : PrimeRandomGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates PrimeRandomGen view

__isPrime : IsPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates IsPrime view

Methods
-------
__None__



****************************************************
## __PrimeGenUI.\_\_init\_\_(self)__
Initilizer for PrimeGenUI. Creates Tab window with all three prime gen widgets

Parameters
----------
__None__

Returns
-------
__IsPrime__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************

****************************************************
## __class PrimeRandomGen__
Creates a Prime Number Generator QWidget that generates a specificied amount of
random prime numbers with a specificied number of digits from user input

Inherits all methods and attributes from QWidget

Attributes
----------
__randomHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__randomDigitLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label for Digit Input

__randomAmountLabel : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label for Amount of numbers input

__randomDigitInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text input for number of digits

__randomAmountInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text input for how many random numbers

__randomGenButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button

__randomGenCopy : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copies output to clipboard

__randomGenClear : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears output text

__randomNumOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateRandomHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the randomHeader

___CreateRandpomInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a various QLineEdit object with validators and other settings

___CreateRandomButtons():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input

__setRandomOutput(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the output text of randomNumOutput

__getRandomOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns the output text of randomNumOutput

__clearRandomOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears the output text of randomNumOutput



****************************************************
## __PrimeRandomGen.\_\_init\_\_(self)__
Initilizer for PrimeRandomGen

Parameters
----------
__None__

Returns
-------
__PrimeRandomGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __PrimeRandomGen.\_CreateRandomHeader(self)__
Creates a QLabel text header

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header text



****************************************************
## __PrimeRandomGen.\_CreateRandomInput(self)__
Creates a layout with QLineEdit input text fields with instructions

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout of text input fields



****************************************************
## __PrimeRandomGen.\_CreateRandomButtons(self)__
Creates a QHBoxLayout of various QPushButtons

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Genereate, Copy All, and Clear buttons



****************************************************
## __PrimeRandomGen.setRandomOutput(self, text)__
Changes the text of randomNumOutput

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input of new text

Returns
-------
__None__



****************************************************
## __PrimeRandomGen.getRandomOutput(self)__
Returns randomNumOutput's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;randomNumOutput's text



****************************************************
## __PrimeRandomGen.clearRandomOutput(self)__
Changes the text of randomNumOutput to an empty string

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************
## __class PrimeRangeGen__
Creates a Prime Number Generator QWidget that generates based on the range
from 1 to a user inputted positive integer

Inherits all methods and attributes from QWidget

Attributes
----------
__rangeHeader : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text header

__rangeInput : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text input field

__rangeGenButton : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button to generate input

__rangeGenCopy : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copys results to clipboard

__rangeGenClear : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears output text

__primeRangeOutput : ScrollLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scroll label for output

Methods
-------
___CreateRangeHeader():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLabel object for the rangeHeader

___CreateRangeInput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a QLineEdit object with validators and other settings

___CreateRangeButtons(self):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Creates a layout of QPushButtons for input

__setRangeOutput(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes the output text of primeRangeOutput

__getRangeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns the output text of primeRangeOutput

__clearRangeOutput():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clears the output text of primeRangeOutput



****************************************************
## __PrimeRangeGen.\_\_init\_\_(self)__
Initilizer for PrimeRangeGen

Parameters
----------
__None__

Returns
-------
__PrimeRangeGen__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __PrimeRangeGen.\_CreateRangeHeader(self)__
Creates a QLabel text with instruction limits

Parameters
----------
__None__

Returns
-------
__QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header/instructional text



****************************************************
## __PrimeRangeGen.\_CreateRangeInput(self)__
Creates a QLineEdit input field

Parameters
----------
__None__

Returns
-------
__QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primeRangeInput field



****************************************************
## __PrimeRangeGen.\_CreateRangeButtons(self)__
Creates a QHBoxLayout of various QPushButtons

Parameters
----------
__None__

Returns
-------
__QHBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Layout with Genereate, Copy All, and Clear buttons



****************************************************
## __PrimeRangeGen.setRangeOutput(self, text)__
Changes the text of primeRangeGenOutput

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input of new text

Returns
-------
__None__



****************************************************
## __PrimeRangeGen.getRangeOutput(self)__
Returns primeRangeGenOutput's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primeRangeOutput's text



****************************************************
## __PrimeRangeGen.clearRangeOutput(self)__
Changes the text of primeRangeGenOutput to an empty string

Parameters
----------
__None__

Returns
-------
__None__



****************************************************

****************************************************
## __class ScrollLabel__
Custom setup of a QScrollArea to create a read-only Scroll Label for Prime Gen Output

Inherits all methods and attributes from QScrollArea

Attributes
----------
__label : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the text content of the object

Methods
-------
__setText(text):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changes label's text with text

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns label's text



****************************************************
## __ScrollLabel.\_\_init\_\_(self)__
Construct A ScrollLabel with certain properties

Parameters
----------
__label : QLabel__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used to store text for the ScrollArea

Returns
-------
__ScrollArea__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __ScrollLabel.setText(self, text)__
Sets the text of label

Parameters
----------
__text : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input for the label to change to

Returns
-------
__None__



****************************************************
## __ScrollLabel.text(self)__
Returns the string of label's text

Parameters
----------
__None__

Returns
-------
__str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Label's text



****************************************************
# From prime_gen.test


****************************************************
## __class TestWindowPrimeGen__
Constructs a QMainWindow to create and append to it's window a PrimeGenUI widget
for testing purposes

Inherits all methods and attributes from QMainWindow

Attributes
----------
__generalLayout : QVBoxLayout__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stores the layout of the main

___centralWidget : QWidget__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains central widget bound to self

__primeGenUI : PrimeGenUI__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initializes and stores PrimeGenUI

Methods
-------
__None__



****************************************************
## __TestWindowPrimeGen.\_\_init\_\_(self)__
Initilizer for TestWindow

Parameters
----------
__None__

Returns
-------
__TestWindow__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the central widget for main application



****************************************************
## __main_test_prime_gen()__
Main drivers that initializes PyQt5 application, creates a TestWindow widget,
and PrimeGenCtrl to connect to the primeGenUI in the main view, as well as sending
the models module.

Parameters
----------
__None__

Returns
-------
__None__


****************************************************
# From temp_conversion.temp_conv_logic


****************************************************
## __class temp_Ui__
Creates a QWidget that performs temperature conversion between Fahrenheit, Celcius,
and Kelvin.

Inhereits all methods and attributes from QWidget

Attributes
----------
__button : QPushButton__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit button to initiate conversion

__input : QLineEdit__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input text field

__radioButtons : [QRadioButtons]__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list containing all the radiobuttons in the widget.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 - Fahrenheit (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 - Celcius (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 - Kelvin (Input)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 - Fahrenheir (Output)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 - Celcius (Output)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 - Kelvin (Output)

Methods
-------
__enterButtonPressed():__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Send input value and input and output base to convert_temp when pressed

__convert_temp(val, original_unit, unit_to_convert_to):__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converts val from original_unit to unit_to_convert_to



****************************************************
## __temp_Ui.\_\_init\_\_(self)__
Initializes the UI, including loading the widgets from its ui file, and connecting
signals.

Parameters
----------
__None__

Returns
-------
__temp_Ui__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newly constructed widget



****************************************************
## __temp_Ui.enterButtonPressed(self)__
If text field is filled, sends input value and input and output base 
to convert_temp when pressed, then takes results and outputs them

Parameters
----------
__None__

Returns
-------
__None__



****************************************************
## __temp_Ui.convert_temp(self, val, original_unit, unit_to_convert_to)__
Converts val from original_unit to unit_to_convert_to

Parameters
----------
__val : float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the input temperature value

__original_unit : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input temperature unit

__unit_to_convert_to : str__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output temperature unit to convert to

Returns
-------
__float__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;converted temperature value



****************************************************
