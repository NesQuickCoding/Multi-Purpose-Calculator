## Problem
Early in development, we tried to utilize QT Creater to aid in creating the look and size of our app. But when generating the raw python code, it was far too unorganized to control the logic.

## Solution
Instead, the UI files would be loaded directly with PyQt5, creating the widgets and layout, but handling the logic, may it be signal handling or conversion equations, would be written manually. This was an easier solution to keep code and organized for the rest of the team while still implimenting custom logic.

---

## Problem
When developing the input functionality for the ASCII conversion widget, each input method needed different of validation to be done, otherwise a TypeError exception would be raised. But since each conversion unit (decimal, hexadecimal, and char) have their own different valid inputs (example, char must be one digit only, dec must not be negative or a float, hexadecimal can have both numbers and certain characters), different validations must be applied at different times. Also, without having the raido buttons default on a certain selection, an exception would be raised if the user immediatly submits without selection a unit manually.

## Solution
PyQt5 has input validators that work to a certain extent. By creating a list of different QValidators with different settings, and by creating a signal handler that would pick the validator whenever input unit selection changed, we were able to apply the appropriate validator for the input. To further the functionality our input validation, we wrote custom ones that would use Reg Exp and pass if ValueError exceptions rose. We also set certain radio button selection on when the widget is initialized.

---

## Problem
When developing the input functionality for the Brithday Conversion widget, we also encountered a similar situation with input validation. This time it extended to not allowing a certain range or float or integers, but also the context of other input fieldd's value. For example, if your month input was 4 (April), you can had the day value of 30. But this wouldn't work if month was 2 (Feburary). We also had to make sure the date inputted was not ahead of today's date.

## Solution
Ultimately, we had to create limit checks being done for all three boxes eveery time textChanged was triggered for any of them. Once called, each input field would see what the other input field's values were in order to decide what their limit could be. After these checks were done, it would also compare to the current date, and if it was ahead of that, then the input would jus default to the current date.

---

## Problem
We noticed our app's windows and widgets were different on each other's screens, sometimes making certain input fields too sqeezed to be readable. We also noticed behavior that moving the app across different monitors would also affect the UI's size and porportions negatively.

## Solution
After some research, we found what contributed to this was different zoom/scaling done by certain OS settings. The solution was to enable high dpi scaling and use high dpi pixmaps to keep scaling constant across all different screens. We also increased our window size slightly.

---

## Problem
Originally, our main calculator used eval() in order to evaluate our expression built as a string. However, using eval can has serious security issues and should be avoid whenever possible.

## Solution
Using ast.parse allows us to break out expression how eval would into a syntax tree. We then can iterate through the tree, and examine if each node that returns is a constant (number), operator, or urnary (signage) type of node. If it's never any of those three, the program will raise an error and shut down, effectively preventing any unintended usage that eval could supply.

---

## Problem
When developing the input functionality for the ASCII conversion widget, each input method needed different of validation to be done, otherwise a TypeError exception would be raised. But since each conversion unit (decimal, hexadecimal, and char) have their own different valid inputs (example, char must be one digit only, dec must not be negative or a float, hexadecimal can have both numbers and certain characters), different validations must be applied at different times. Also, without having the raido buttons default on a certain selection, an exception would be raised if the user immediatly submits without selection a unit manually.

## Solution
PyQt5 has input validators that work to a certain extent. By creating a list of different QValidators with different settings, and by creating a signal handler that would pick the validator whenever input unit selection changed, we were able to apply the appropriate validator for the input. To further the functionality our input validation, we wrote custom ones that would use Reg Exp and pass if ValueError exceptions rose. We also set certain radio button selection on when the widget is initialized.

---

## Problem
Our Tech Spec required us to list and detail every single class and function that was created for this project. Over the course of development, we created a very fair amount of code where making a single doc would be extremely time consuming and prone to errors.

## Solution
Instead of typing the document manually, we would write doc strings for all our functions and classes. After then, we would then develop a script that would parse through every module and object used in our project. If the class or function was a part of the file (meaning, we wrote it), its `__module__` property would be the module we are currently parsing through. From that point, we then retrieve its doc strings and format for markdown/html. With this solution, we only needed to write documentation once, and if we made any additions or changes, we can instantly generate another clean document without having to edit it manually.

---
