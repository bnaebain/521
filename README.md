# Currency Converter Project for Boston University CS 521: Python

This final project is composed of three unique Python program scripts, one main program (main.py) and two class programs (fixer.py and input_output.py). Overall, the program takes currency ISO codes and an amount from user input and provides a converted monetary amount. The program uses the requests module to access the API from fixer.io. The program also creates (or appends) a .csv file to record every conversion the program makes with a date and time stamp from when it was created. In the main program you will also find two unit-tests that use random amounts, one converts USD to EUR, and one converts SEK to MXN. In a docstring at the bottom, I have the function to call a version that would have a user input their own currencies and amount into the console- you can run lines 134-136 to use the input version. 

The main program includes two public functions and one private function:

•	def input_(): Input function to collect ISO codes and an amount via user input. Validates the ISO codes with fixer.io’s API by calling the Fixer program’s private _Symbols class function get_symbols. 
•	def program(inputs): This is the primary script to convert the currencies. This module makes use of fixer.io’s API to submit our ISO codes and receive the returned conversion value. This module makes use of the Fixer program’s public Converter class to get the conversions, calls a magic class method __truediv__() to get the conversion rate, prints the results to the console (with added flair), and calls the private _record function to edit the .csv. This program also makes use of a set type to show recent recorded currencies in the console. 
•	def _record(): uses the File class from input_output.py to create or update the .csv file in the current working drive. 

Within the project you can find all four container types, an example of each:
•	List: main.input_.main_symbols
•	Tuple: main._record.row_info
•	Set: main.FROM
•	Dictionary: fixer._Symbols.jsonResponse

The iteration type (while), if, and try/else conditions can all be found in the main.input_() function. 

The unit tests are notated by if __name__ == "__main__":. Each will automatically run when you run the main script. No need to run them one by one. The user input version will require the removal of the docstring quotes (lines 133 and 137) or to run the selection of lines 134 – 136. You must install requests; all other modules are native: datetime, time, random, os, and csv. Use of the requests module was pre-approved. 
