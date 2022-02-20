"""
Brinae Bain
Class: CS 521 - Spring 1
Date: 
Final Project
	Fixer.io Requests
    
"""
import requests


class _Symbols:
    '''Used to identify validated symbols from user input using request API'''
    
    def get_symbols():
        response = requests.get(str.__add__('http://data.fixer.io/api/symbols?access_key=',
                                      'fab696bb4082dd825a4681f6be651707'))
        response.raise_for_status()
        jsonResponse = response.json()
        symbols = jsonResponse['symbols']
        return symbols
	

class Converter:
    '''The conversion functions, that retrieve the response object from fixer.io'''
    
    def __init__(self, f, t, a):
        self.from_country = f
        self.to_country = t
        self.amount = a

        
    def conversion(self):
        _url = ["http://data.fixer.io/api/convert", "?access_key=fab696bb4082dd825a4681f6be651707", "&from=", self.from_country, "&to=", self.to_country, "&amount=", self.amount]
        _url_str = "".join(_url)
        c = requests.get(_url_str)
        
        c.raise_for_status()
        jsonResponse = c.json()
        conversion = jsonResponse['result']
        return conversion
    

    def __str__(self):
        return 'Converting ' + self.amount + ' ' + self.from_country + ' to ' +self.to_country

    def __truediv__(self, other):
        amount = int(self.amount)
        return other / amount