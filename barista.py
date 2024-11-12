#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 02:37:52 2023

@author: blackrose
"""

class Barista:
    """ Barista Class responsible is for managing barista operations.
    It handles the add, remove and tracking baristas"""
    
    def __init__(self, coffee_program):   
        
        """initalise number of baristas pluss/minus with 0"""
        self._number_baristas_plus = 0
        self._number_baristas_minus = 0
        
        """initalise the baristas list with empty dictionary"""
        self._baristas_list = []
        
        self._specialty_counts = {}
        
        self._coffee_program = coffee_program
        
          
    def add_barista(self, add_number, barista_name="New Barista"):
        """Add a new barista to the coffee shop.
        This method will increment the number of baristas and adds a new barista to the list."""
        self._number_baristas_plus += add_number
        self._baristas_list.append(barista_name)
        
       
        check_input = True
        
        while check_input:
            
            
            have_specialty = input(f"Does {barista_name} has a specialty in which type of coffee? (yes/no): ").lower()
            
            if have_specialty == 'yes':
                
                check_coffee = True
                
                while check_coffee:
                    specialty = input(f"Enter the coffee type that {barista_name} specializes: ").capitalize()
                    if specialty in ['Expresso','Americano','Filter','Macchiatto','Flat_white','Latte']:
                        """check correct input type of coffee"""
      
                        # check if the specialty is already in the dictionary
                        if specialty in self._specialty_counts:
                            # if yes, increment its count
                            self._specialty_counts[specialty] += 1
                        else:
                            # if not, add the item with a count of 1
                            self._specialty_counts[specialty] = 1
                        
                    
                        check_coffee = False
                    else:
                        check_coffee = True
                        print("Please type only valid coffee (Expresso, Americano, Filter, Macchiatto, Flat_white, Latte)")                 
                break
            elif have_specialty == 'no':               
                specialty = "no"      
                if specialty in self._specialty_counts:
                    # if yes, increment its count
                    self._specialty_counts[specialty] += 1
                else:
                    # if not, add the item with a count of 1
                    self._specialty_counts[specialty] = 1            
                break
            else:
                check_input = True
                print("Please enter only yes or no")
                
        if have_specialty == 'yes':
            print(f"Added {barista_name} who special for {specialty}, hourly rate=15 in month {self._coffee_program._month}")
        else:
            print(f"Added {barista_name} - non-special, hourly rate=15 in month {self._coffee_program._month}")
           
        return self._number_baristas_plus, self._baristas_list, self._specialty_counts
    
    
    def get_baristas(self):
        """ Get barista list."""
        return self._baristas_list
    
    def get_number_baristas(self):
        """ Get number of barista."""
        return len(self._baristas_list)
    
    
    def remove_barista(self, remove_number, barista_name):
        """To enable user removing barista."""
        self._number_baristas_minus -= remove_number
        self._baristas_list.remove(barista_name)
        print(f"Removed {barista_name}, hourly rate=15 in month {self._coffee_program._month}")
   #         print(self._number_baristas_minus, self._baristas_list)
       
        return (self._number_baristas_minus, self._baristas_list)
        
        
    def can_remove_baristas(self, remove_number):
        """Check wheter number of removed baristas is less than or equal to 
        current total baristas or not? in order to check if the user is typing wrong value"""
        if abs(remove_number) <= self._number_baristas_plus:
#            print(abs(remove_number),self._number_baristas_plus)
            return True
        
        else:
            print("You cannot remove more than a number of current baristas")
            return False
        
  