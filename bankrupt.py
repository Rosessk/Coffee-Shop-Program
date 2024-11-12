#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:38:14 2023

@author: blackrose
"""

class Bankrupt:
    """Bankrupt will handle and display when the coffee shop is bankruptcy
    This class provides methods to sjow the status of the coffee shop, focusing on
    the cash status and ingredient views, which are important in the evaluation of bankruptcy."""

        
    def final_display(self, month, cash_status, milk, beans, spices, list_baristas, capacity_ingredient, depreciation_factor):
        """ Show coffee shop's status, including cash balance, ingredient,
        and barista details"""
    
        milk_stock = milk - milk * depreciation_factor['Milk']
        beans_stock = beans - beans * depreciation_factor['Beans']
        spices_stock = spices - spices * depreciation_factor['Spices']
        print("====== FINAL STATE month", month, "======")
        print(f"Shop Name: Boost, Cash: {cash_status:.2f}")
        print(f"""    Pantry
              Milk, {milk_stock:.2f} (capacity= {capacity_ingredient['Milk']})
              Beans, {beans_stock:.2f} (capacity={capacity_ingredient['Beans']})
              Spices, {spices_stock:.2f} (capacity={capacity_ingredient['Spices']})""")
        print("   Baristas")
        for individual in list_baristas:
            print(f"      Barista {individual}, hourly rate=15")
     
    