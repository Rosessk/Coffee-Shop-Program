#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:57:11 2023

@author: blackrose
"""


class CoffeeProgram:
    """CoffeeProgram Class representing the UX interface for a coffee program.
    The class provides the main interface for interacting with the coffee program, including
    methods for receiving user input and displaying information."""
    ######################################test####################################################
    def __init__(self):
        self._month = 1  # initialize the current month to 1


    def mounth_input(self):
        """Allow the user to input the number of months.
        If the user does not enter a value, it defaults to 6 months."""
        months = input("Please enter number of months: ")
        if months == '':
            months = 6
            print("The default is 6 months")
        else:
            months = int(months)
        return months
    def theme_month(self, month = 6):
        """Set and display of current month on the screen."""
        
        self._month = month
        print("================================")
        print("====== SIMULATING month", month, "======")
        print("================================")
    
    
