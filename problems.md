Andrew Alagna:
I ran into problem's trying to load the generated Qt creator UI file into our program. At first I attempted to generate the python code from the UI, but quickly realized that the generated code was too unorganized. I ended up loading the UI file directly into the temperature conversion class, and writing all of the logic to process the data manually. Instead of generating all of the python code, I found this an easier way to organize and write custom logic.


**Neslie Fernandez:**

* **ASCII Conversion:**
  * **Problem:** Invalid char input length or characters
    * **Solution:** Input Validators to validate inputs with proper length / characters
  * **Problem:** Running the ASCII Conversion with no radio buttons checked causes the app to crash
    * **Solution:** Set Default checked radio buttons for both Convert To and Convert From sections
    

* **Birthday Conversion:**
    * **Problem:** Invalid inputs for Month, Day, Year and non leap years
      * **Solution:** Add a try catch to check whether a date is valid
    * **Problem:** Dates beyond present day will output negative values
      * **Solution:** Henry Baum created input validators to prevent users entering a date going over the present day.
  
  

* **App Scaling:**
  * **Problem:** Scaling issues with multiple monitors when app is moved from one screen resolution to another cutting the app view / input line height
    * **Solution:** Enable high dpi scaling and using high dpi pixmaps to keep app scaling constant from different screens
  * **Problem:** Right portion of the app not showing all the widgets
    * **Solution:** Increase fixed size height by 50
    