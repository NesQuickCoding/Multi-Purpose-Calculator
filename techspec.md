# Table Of Contents

### From main
* [Class MultiCalcWindow](#class-multicalcwindow)

	* [MultiCalcWindow.\_\_init\_\_(self)](#multicalcwindowinitself)

* [Class SecCalc](#class-seccalc)

	* [SecCalc.\_\_init\_\_(self)](#seccalcinitself)

	* [SecCalc.secCalcDisplay(self, i)](#seccalcseccalcdisplayself-i)

* [main()](#main)


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
