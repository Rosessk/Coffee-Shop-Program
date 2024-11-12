#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:57:41 2023

@author: blackrose
"""

class Supplier:
    """Supplier class provides a supplier name and  prices in each ingredient.""" 
    def __init__(self):        
        """Initalise a dictionary of supplier names (Hasty) and ingredient prices."""
        self._supplier_name = {
            'Hasty':{
                'Milk': 0.3,
                'Beans': 0.1,
                'Spices': 0.05}
            }    
    def get_price_from_supplier(self):
            """Method to get prices from each ingredient from a specific supplier."""
            milk_price = self._supplier_name['Hasty']['Milk']
            beans_price = self._supplier_name['Hasty']['Beans']
            spices_price = self._supplier_name['Hasty']['Spices']
            return milk_price, beans_price, spices_price
        
        