#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 18:39:08 2023

@author: blackrose
"""


from coffee_shop import CoffeeShop


class Owner(CoffeeShop):
    """class extending the functionalities of CoffeeShop.
    This class adds optional way to make a desicion with coffee shop.
    It inherits from the CoffeeShop class and it have its own methods."""
    
    def __init__(self, coffee_program, barista, sale_list):
        super().__init__(coffee_program)
        self._barista = barista
        self._sale_list = sale_list

    def run_simulation(self, month):
        """run a monthly simulation for the coffee shop."""
            
        print(f"\n-------------- Month {month + 1} test --------------")
        self.make_decisions()

    def make_decisions(self):
        """Make decisions based on the current cash status of the coffee shop.
        make_decisions method evaluates the cash status and makes decisions to avoid bankruptcy.
        This decisions are based on the current cash status from the test method."""
        
        # decision making based on the current cash status retrieved from the test method
        current_cash_status = self.test()
        
        try:
            # decision making based on cash status
            if current_cash_status < 1000:
                print("You risk bankruptcy.")
                
                # fix to full demand to make shop can get full income to avoid bankruptcy
                self._sale_list = [500, 200, 300, 400, 600, 1000]
                preferred_sale = self._sale_list[0] * 1.5 + self._sale_list[1] * 2.5 + self._sale_list[2] * 1.5 + self._sale_list[3] * 3.0 + self._sale_list[4] * 3.5 + self._sale_list[5] * 4.0
                
                # estimate pantry cost because it is never up to 100
                fix_pantry = 100
                
                # calculate cash of next month
                new_cash = preferred_sale + self.get_number_baristas(self._barista) * 1800 - 1500 - fix_pantry + self.test()
                
                print("In the following month")
                print(f"""Coffee Expresso input should be {self._sale_list[0]}\nCoffee Americano input should be {self._sale_list[1]}\nCoffee Filter input should be {self._sale_list[2]}\nCoffee Macchiatto input should be {self._sale_list[3]}\nCoffee Flat_white input should be {self._sale_list[4]}\nCoffee Latte input should be {self._sale_list[5]}""")
                print("---------------------------------------------")
                print(f"The cash will be {new_cash}")
                print("")
    
            else:
                # use the sale_list from last input of user
                preferred_sale = self._sale_list[0] * 1.5 + self._sale_list[1] * 2.5 + self._sale_list[2] * 1.5 + self._sale_list[3] * 3.0 + self._sale_list[4] * 3.5 + self._sale_list[5] * 4.0 
                
                # estimate pantry cost because it is never up to 100
                fix_pantry = 100
                
                # calculate cash of next month
                new_cash = preferred_sale - self.get_number_baristas(self._barista) * 1800 - 1500 - fix_pantry + self.test()
                
                print("In the following month")
                print(f"""Coffee Expresso input should be {self._sale_list[0]}\nCoffee Americano input should be {self._sale_list[1]}\nCoffee Filter input should be {self._sale_list[2]}\nCoffee Macchiatto input should be {self._sale_list[3]}\nCoffee Flat_white input should be {self._sale_list[4]}\nCoffee Latte input should be {self._sale_list[5]}""")
                print("---------------------------------------------")
                print(f"You can define value as the old month, and the cash will be {new_cash}")
                print("")
                
        except IndexError:
            print("Can not show the decision of next month")
    
    
    
