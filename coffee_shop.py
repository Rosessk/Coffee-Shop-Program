#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:53:14 2023

@author: blackrose
"""


class CoffeeShop:
    """CoffeeShop Class is the core operations of a coffee shop.
    This class manage a number of thing such as cash status, income and expenditure calculations,
    ingredient purchasing, barista information."""
    
    def __init__(self, coffee_program):        
        """initalise the constant including cash_status at starting month, rent_utilities_cost in each month
        paid_barista when there is no barista, rate_barista per hour and hour_barista in a month"""
        self._cash_status = 10000
        self._rent_utilities_cost = 1500
        self._paid_barista = 0
        self._rate_barista = 15
        self._hour_barista = 120
      
        """retrive coffee_program from outside"""
        self._coffee_program = coffee_program
             
        """initailise the ingredients with key-value pairs in dictionary"""
        self._quantity = {
            'Milk': 300, #litre
            'Beans': 20000,
            'Spices': 4000
        }
        self._depreciation = {
            'Milk': 0.4,
            'Beans': 0.1,
            'Spices': 0.1
        }
        self._pantry_cost = {
            'Milk': 0.10,
            'Beans': 0.001,
            'Spices': 0.001
        }
        
        """initailise the cofee type with key-value pairs in dictionary
        Plese note that the unit of ingredients in every type of coffee is 'g' except Milk unit is litre and
        the unit of time is minutes"""
        
        self._coffee_types = {
            'Expresso': {
                'Milk': 0.0, #litre
                'Beans': 8,
                'Spices': 0,
                'Time': 3,
                'MonthlyDemand': 500,
                'SellPrice': 1.5
            },
            'Americano': {
                'Milk': 0.0, #litre
                'Beans': 6,
                'Spices': 0,
                'Time': 2,
                'MonthlyDemand': 200,
                'SellPrice': 2.5
            },
            'Filter': {
                'Milk': 0.0, #litre
                'Beans': 4,
                'Spices': 0,
                'Time': 1,
                'MonthlyDemand': 300,
                'SellPrice': 1.5
           },
            'Macchiatto': {
                'Milk': 0.1, #litre
                'Beans': 8,
                'Spices': 2,
                'Time': 4,
                'MonthlyDemand': 400,
                'SellPrice': 3.0
            },
            'Flat_white': {
                'Milk': 0.2, #litre
                'Beans': 8,
                'Spices': 1,
                'Time': 5,
                'MonthlyDemand': 600,
                'SellPrice': 3.5
            },
            'Latte': {
                'Milk': 0.3, #litre
                'Beans': 8,
                'Spices': 3,
                'Time': 6,
                'MonthlyDemand': 1000,
                'SellPrice': 4.0
            }
        }
        
    def get_coffee_recipe(self):
        """Method  to return (get) coffee_types"""
        return self._coffee_types.items()
        
    def get_baristas(self, barista):
        """Method to retrieve list barista names from outside and return the list of barista names"""
        list_barista = barista.get_baristas()
        return list_barista
 
    def get_number_baristas(self, barista):
        """Method to retrieve  the number of barista from outside and return the number of barista"""
        number_barista = barista.get_number_baristas()
        return number_barista
    
    def get_existing_quantity(self):
        """Method to return (get) quantities"""
        return self._quantity.items()
    
    def get_depreciation(self):
        """Method to return (get) depreciation"""
        return self._depreciation
            
            
    def calculate_income(self, sale_list):
        """Method to calculate income from each coffee type"""
        total_income  = 0
        sell_prices = [] 
        for each_type in self._coffee_types :
            sell_prices.append(self._coffee_types[each_type]['SellPrice'])
        for sale, sell_price in zip(sale_list, sell_prices):
            total_income += sale * sell_price
            #print(total_income)
        return total_income
    
    def calculate_expense_baristas(self, barista):   
        """Method to calculate cost of barista"""
        # paid barista     
        list_paid_baristas = []
        for barista in self.get_baristas(barista):
            paid_barista_person = self._rate_barista * self._hour_barista        
            list_paid_baristas.append(paid_barista_person)
            #print(list_paid_baristas)
            print(f"Paid {barista}, hourly rate={self._rate_barista} amount {paid_barista_person}")
        total_paid_baristas = sum(list_paid_baristas) 
        return total_paid_baristas
    def calculate_ingredient_costs(self, milk, beans, spices):
        """Method to calculate cost of pantry"""
        pantry_milk_cost = milk * self._pantry_cost['Milk']
        pantry_beans_cost = beans * self._pantry_cost['Beans']
        pantry_spices_cost = spices * self._pantry_cost['Spices']

        total_ingredient_cost = pantry_milk_cost + pantry_beans_cost + pantry_spices_cost
        return total_ingredient_cost, pantry_milk_cost, pantry_beans_cost, pantry_spices_cost 
    
    def ingredient_stock(self, milk, beans, spices, prev_month_milk, prev_month_beans, prev_month_spices):
        """Method to calculate ingredient stock"""   
        # print('testtttt prev_month_milk in depre')
        # print(prev_month_milk, prev_month_beans, prev_month_spices)
        # Calculate ingredient depreciation and round up to the nearest integer
        milk_depreciation = int(prev_month_milk * self._depreciation['Milk'])
        beans_depreciation = int(prev_month_beans * self._depreciation['Beans'])
        spices_depreciation = int(prev_month_spices * self._depreciation['Spices'])
        
         # check for remainders and add 1 if there is any
        if prev_month_milk * self._depreciation['Milk'] % 1 > 0:
             milk_depreciation += 1
        if prev_month_beans * self._depreciation['Beans'] % 1 > 0:
             beans_depreciation += 1
        if prev_month_spices * self._depreciation['Spices'] % 1 > 0:
             spices_depreciation += 1
         
         
        # after depreciation in the month
        after_depreciation_milk = prev_month_milk - milk_depreciation
        after_depreciation_beans = prev_month_beans - beans_depreciation
        after_depreciation_spices = prev_month_spices - spices_depreciation
       
        
        return after_depreciation_milk, after_depreciation_beans, after_depreciation_spices # these will be the existing stock for next month
        
    def buy_new_ingredient(self, milk_price, beans_price, spices_price, milk, beans, spices, prev_month_milk, prev_month_beans, prev_month_spices):
        """Method to calculate cost of ingredient"""  
        after_depreciation_milk, after_depreciation_beans, after_depreciation_spices = self.ingredient_stock(milk, beans, spices, prev_month_milk, prev_month_beans, prev_month_spices)  
    
        buy_milk = (self._quantity['Milk'] - after_depreciation_milk) * milk_price
        buy_beans = (self._quantity['Beans'] - after_depreciation_beans) * beans_price
        buy_spices = (self._quantity['Spices'] - after_depreciation_spices) * spices_price
        
        total_ingredients_price = buy_milk + buy_beans + buy_spices
        return total_ingredients_price

    def cash_status(self, total_ingredient_cost, pantry_milk_cost, pantry_beans_cost, pantry_spices_cost, total_income, total_paid_baristas, milk, beans, spices, total_ingredients_price, barista):
        """Method to calculate cash status of coffee shop"""  
        # paid rent/utilities
        
        print(f"Paid rent/utilities {self._rent_utilities_cost}")
        print(f"Pantry Milk cost {pantry_milk_cost:.2f}")
        print(f"Pantry Beans cost {pantry_beans_cost:.2f}")
        print(f"Pantry Spices cost {pantry_spices_cost:.2f}")

        #print(f'total_ingredients_price : {total_ingredients_price}')
    
        self._cash_status = round(self._cash_status, 2)     
        self._cash_status = self._cash_status + total_income - total_ingredient_cost - total_paid_baristas - self._rent_utilities_cost - total_ingredients_price      
        print(f"Shop Name: Boost, Cash: {self._cash_status:.2f}")
        print(f"""    Pantry
              Milk, {milk:.2f} (capacity= {self._quantity['Milk']})
              Beans, {beans:.2f} (capacity={self._quantity['Beans']})
              Spices, {spices:.2f} (capacity={self._quantity['Spices']})""")
        print("   Baristas")
        for individual in self.get_baristas(barista):
            print(f"      Barista {individual}, hourly rate=15")
        return self._cash_status
    
    ##########################################test####################################################
    def test(self):
        """Method to return cash status"""
        # perform the calculations and return the cash status
        test = self._cash_status 
        return test
 