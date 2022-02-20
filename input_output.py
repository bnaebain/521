"""
Brinae Bain
Class: CS 521 - Spring 1
Final Project
Description of Program (1-2 sentence summary in your own words):
    input / output 
"""

import os
import csv

cwd = os.getcwd()

class File:
    
    def __init__(self, title):
        self.file = open("Conversions.csv", "a")
        
    def update_file(self, info):
        writer = csv.writer(self.file)
        writer.writerow(info)
        self.file.close()
        
    

        
