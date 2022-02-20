# 521
CS 521: Intro to Python

This is my final project for my Python course. A currency converter. 

This program takes user input currency ISO codes (validated) and converts the currency
to the desired currency. The program outputs the result to the console, as well as updates
a .csv file in the same directory. The .csv file is appended with each new conversion, and includes the recorded date and time. The validation for ISO codes completes an API request to fixer.io for valid currency ISO codes. 

Currently, the name == main modules with predetermined currencies and random amounts are set to default rather than the user input option. See docstring at bottom to run user input option.
