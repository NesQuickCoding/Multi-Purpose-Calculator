
<img src="graphics/Banner.png?raw=true" width=475 alt="Multi-Purpose Calculator">

# Multi-Purpose Calculator
## *Made for the sole survivor*

<img src= "demo/Demo.gif?raw=true" width=475 alt="General Demo of App">

Multi-Purpose Calculator is a stylish calculator application that features two on-sceen calculators and converters.

## Created By

* []() [Andrew Alagna](https://github.com/elchic00)
* []() [Henry Baum](https://github.com/habmin)
* []() [Neslie Fernandez](https://github.com/nesquickcoding)

## Features
### __Basic Calculator__
* Performs basic mathematical functions, such as add, subtract, multiply, division, floor division, modulo, and exponent.
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo1.gif" width="475" alt="Calculator Demo" />
</details>

### __ASCII Conversion__
* Convert to/from a decimal, hexidecial, and ascii character.
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo2.gif" width="475" alt="ASCII Conversion Demo" />
</details>

### __Base Conversion__
* Instantly convert an integer to/from decimal, hexadecimal, and binary bases. Values can be signed/unsigned with bit widths from 8 to 64-bits
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo3.gif" width="475" alt="Base Conversion Demo" />
</details>

### __Prime Number Generator/Validator__ 
* Generate prime numbers, ethier from a range starting at one, or randomlly with a set amount of digits. Also include a validator to determine if a number is prime or not
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo4.gif" width="475" alt="Prime Number Generator/Validator Demo" />
</details>

### __Metric Conversion__
* Convert between various units for length, weight, time, and digital storage space
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo5.gif" width="475" alt="Metric Conversion Demo" />
</details>

### __Temperature Conversion__
* Convert between fahrenheit, celcius, and kelvin
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo6.gif" width="475" alt="Metric Conversion Demo" />
</details>

### __Birthday Conversion__
* Find out how much time has elapsed when given a date in either years, month, or days
* <details>
    <summary>Demo</summary>
    <img src="demo/Demo7.gif" width="475" height="238" alt="Birthday Conversion Demo" />
</details>

## Technologies Used
* Python 3
* PyQt5

During development, a script was also created to help generate techspec in markdown/html formatting. The script can be found [here](https://github.com/habmin/docstrings_to_md).

## How to install and run:
1. Install the latest version of Python 3 to your machine
2. After installation, install PyQt5 with pip by going into your terminal and typing `pip install pyqt5`
3. Clone or download the project either with `git clone https://github.com/NesQuickCoding/Multi-Purpose-Calculator.git` or by manually downloading the ZIP and extracting its contents.
4. Run `main.py` in the root folder, either in your terminal with `python main.py` or however you wish to run the script.
5. The application will open and is ready to use. Close the application as you normally would close a window in your OS.

## Technical Specifications 
To read about each class and function created and used in the project, go to our [spec sheet](techspec.md).

## Issues Faced
To read about some issues and solutions we faced during this project, go to our [problems readme](problems.md).

## Known Issues/Bugs
Our application was systlized and designed with the application's style set as `windowsvista`. We have only worked and tested our app under this set style. Because QT mimics certain styles based on the user's OS, running this app on Mac or Linux machines may have different porportions with buttons or input. 

## Purpose
This project was developed during the Spring 2022 semester at Hunter College for CSCI 39538 - Advance Python course. It was developed over the period of 3 weeks and had the following requirements for the assignment:

* [x] Create a GUI with Python.
* [x] Work and collobrate as a group using Git/GitHub.
* [x] Create at least 4 functions (outside of the classes).
* [x] Create 3 classes for the logic of the application.
* [x] Need to have a window and at least 6 different widgets on the application.
* [x] Technical spec detailing your functions and classes and what they do.
* [x] A md file which details the problems you ran into and how you solved them.

## Resources
List of external resources used can be found [here](resources.md).

#### Feel free to clone and contribute via a pull request! All ideas are welcome.


## License

    Copyright [2022] [Andrew Alagna, Henry Baum, Neslie Fernandez]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
