"""
Brinae Bain
Class: CS 521 - Spring 1
Final Project

This program takes user input currency ISO codes (validated) and converts the currency
to the desired currency. The program outputs the result to the console, as well as updates
a .csv file in the same directory. The .csv file is appended with each new conversion, and includes the recorded date and time. The validation for ISO codes completes an API request to fixer.io for valid currency ISO codes. 

Currently, the name == main modules with predetermined currencies and random amounts are set to default rather than the user input option. See docstring at bottom to run user input option.
"""
#Imported Classes and Modules
from fixer import _Symbols
from fixer import Converter
from time import sleep
from input_output import File
from datetime import datetime
import random

#Declaring Public Global Set variable
FROM = set() #Set of recent origin countries
TO = set() #Set of recent destination countries

print("\n Welcome to Brinae's Currency Converter!")

# Function input_() validates user input for testing out your own currencies:
def input_():
    main_symbols = []
    #Asking for the origin currency with ISO code validation
    while True:
    	try:
    		from_country = input("What is the currency you would like to convert from? \n Please insert the currency code: ")
    		from_country = from_country.upper()
    		main_symbols = _Symbols.get_symbols()
    		if from_country not in main_symbols:
    			print("\n","You did not enter in an appropriate ISO currency code.")
    			raise ValueError
    			continue
    		else:
    			break
    	except ValueError:
    		print("ValueError: Please try again.")
    
    #Asking for the destination currency with ISO code validation
    while True:
    	try:
    		to_country = input("What is the currency you would like to convert to? \n Please insert the currency code: ")
    		to_country = to_country.upper()
    		if to_country not in main_symbols:
    			print("\n","You did not enter in an appropriate ISO currency code.")
    			raise ValueError
    			continue
    		else:
    			break
    	except ValueError:
    		print("ValueError: Please try again.")	
    
    #Asking for the amount desired as a whole number:
    while True:
    	try:
    		amount_str = input("Please enter the amount you would like to convert, round to the nearest whole number: ")
    		amount_str = amount_str.replace(",","")
    		for i in amount_str:
    			if (i.isalpha() == True) or (i == "."):
    				raise ValueError
    				continue
    		else:
    			amount = (amount_str)
    			break
    	except ValueError:
    		print("ValueError: Please enter whole numbers.")
    
    return (from_country, to_country, amount)

# Function program(inputs) calls a various methods from the Conversion class to 
# complete the conversion and get recorded data.
def program(inputs):
    assert len(inputs) == 3
    c1 = Converter(inputs[0], inputs[1], inputs[2])
    FROM.add(inputs[0])
    TO.add(inputs[1])
    c = c1.conversion()
    r = c1.__truediv__(c)
    assert isinstance(c, float)
    print("\n", c1.__str__())
    for i in range(1,5):
        print("  ........", end = '\n')
        sleep(0.5)
    print("\n Your converted amount is: ", "{:.2f}".format(c), inputs[1])
    print("\n Your conversion rate is: ", "{:.2f} \n".format(r))
    sleep(2)
    _record(inputs, c, r)
    print(5 * "\n")
    return c, r

# Private function _record(inputs, c, r) records the conversion along with a date time
# into a .csv (that is create if non-existent) using the File class
def _record(inputs, c, r):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    row_info = (date_time, inputs[2], inputs[0], " is equal to ", "{:.2f}".format(c), inputs[1], "rate:", "{:.2f}".format(r))
    saved_data = File("Conversions.csv")
    saved_data.update_file(row_info)
    print("\n Your record, Conversions.csv, has been updated:")
    print("\n ", row_info)
    print("\n Your recent origin countries:")
    print("\n ", FROM)
    print("\n Your recent destination countries:")
    print("\n ", TO)


# Unit Test #1: USD to EUR (Random amount)
if __name__ == "__main__":
    rand_amt = random.randint(0,10000)
    inputs = ('USD', 'EUR', str(rand_amt))
    assert len(inputs) == 3
    program(inputs)

    

# Unit Test #2: SEK to MXN (Random amount)
if __name__ == "__main__":
    rand_amt = random.randint(0,10000)
    inputs = ('SEK', 'MXN', str(rand_amt))
    assert len(inputs) == 3
    program(inputs)

 

#####   
# Feel free to input your own currency codes and amount, just remove the docstring quotes below to call the input_() function. You'll need to run lines 12 - 109 first. 

'''
inputs = input_()
assert len(inputs) == 3
program(inputs)
'''

