#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:51:07 2023

@author: blackrose
"""
from coffee_program import CoffeeProgram
from coffee_shop import CoffeeShop
from insufficient import Insufficient
from supplier import Supplier
from bankrupt import Bankrupt
from barista import Barista
from owner import Owner

# this script is the entry point for the coffee shop program. You can run the coffee shop program in here.

# initalise value
prev_month_milk = 0
prev_month_beans = 0
prev_month_spices = 0
milk = 0
beans = 0
spices = 0

# main loop for continuous run the coffee shop program
while True:
    try:
        # Create an instance of the coffee shop components
        coffee_program = CoffeeProgram()
        coffee_shop = CoffeeShop(coffee_program)
        barista = Barista(coffee_program)
       
        months = coffee_program.mounth_input()
        # handling the case when user inputs 0 months, showing that no need to run programm
        if months == 0:
            print("Nothing to show because user select 0 month")
                
        else:
            # iterating each month
            for month in range(1, months + 1):
                prev_month_milk = milk
                prev_month_beans = beans
                prev_month_spices = spices
                
                coffee_program.theme_month(month)     
                while True:
                    # handling barista input error
                    try:
                       while True:
                        print("To add enter positive, to remove enter negative, no change enter 0.")
                        number = int(input("Enter number of baristas: "))            
                        if month ==1:
                            if number == 0:
                                print("The shop have to have number of baristas at least 1")
                             
                            else:
                                break
                 
                        if month ==1:
                            if number == 0:
                                pass
                        else:
                            break
                    
                    except ValueError:
                        print("Please enter an integer value: invalid literal")
                        continue
                    
                    # check add baristas number (do not exceed 4 people in a month)
                    if number <= 4 and number > 0:
                        for i in range(1, number+1):
                            barista_name = input("Enter barista name: ")
                            barista_name = barista_name.capitalize()
                            
                            # handling barista name input = empthy
                            while barista_name == '':
                                print("Please enter a barista name: invalid literal")
                                barista_name = input("Enter barista name: ")
                                
                            # increment number of barista
                            number_baristas_plus, baristas_list, specialty_counts = barista.add_barista(1, barista_name) ##################
                             
                        break  
                    
                    elif number < 0:  
                        if barista.can_remove_baristas(number) == True:
                            # Not allow user to remove baristas if number of bristas < 1
                            if coffee_shop.get_number_baristas(barista) == -number:
                                print("Number of baristas needs minimum: 1")
                            
                            else:
                                for i in range(1, abs(number)+1):
                                    while True:
                                        barista_name = input("Enter barista name: ")
                                        barista_name = barista_name.capitalize()
                                        if barista_name not in coffee_shop.get_baristas(barista):
                                            print(coffee_shop.get_baristas(barista))
                                            print("There is no barista with the name", barista_name)
                                            print("Please try again")
                                            
                                            
                                        else:
                                            print(coffee_shop.get_baristas(barista))
                                            barista.remove_barista(1, barista_name)
                                            break
                                break
      
                        else:
                            pass
              
                    elif number == 0:
                        print("You do not change the member of baristas for this month")
                        break
                    
                    else:
                        print("You cannot add more than 4 number of baristas in each month")
                    
                # create instances and get value from that instances
                check_insufficient = Insufficient(coffee_shop) 
                coffee_types = coffee_shop.get_coffee_recipe()     
                milk, beans, spices, sale_list = check_insufficient.calculate_insufficient(coffee_types, specialty_counts, barista, month)################   
                total_ingredient_cost, pantry_milk_cost, pantry_beans_cost, pantry_spices_cost = coffee_shop.calculate_ingredient_costs(milk, beans, spices)
                total_income = coffee_shop.calculate_income(sale_list)
                total_paid_baristas = coffee_shop.calculate_expense_baristas(barista)
                supplier = Supplier()
                milk_price, beans_price, spices_price = supplier.get_price_from_supplier()
                
                # Set total_ingredients_price based on the current month
                if month == 1:
                    total_ingredients_price = 0
                else: 
                    total_ingredients_price = coffee_shop.buy_new_ingredient(milk_price, beans_price, spices_price, milk, beans, spices, prev_month_milk, prev_month_beans, prev_month_spices)
                
                # set the current ingredients to be  previous ingredients in the next month
                prev_month_milk = milk 
                prev_month_beans = beans
                prev_month_spices = spices
                
                #print("print on cash")
                #print(prev_month_milk, prev_month_beans, prev_month_spices)
                
    
                cash_status =  coffee_shop.cash_status(total_ingredient_cost, pantry_milk_cost, pantry_beans_cost, pantry_spices_cost, total_income, total_paid_baristas, milk, beans, spices, total_ingredients_price, barista)
                
                
                depreciation_factor = coffee_shop.get_depreciation()
                
                want_milk = milk * depreciation_factor['Milk'] * milk_price
                want_beans = beans * depreciation_factor['Beans'] * beans_price
                want_spices = spices * depreciation_factor['Spices'] * spices_price
                
                # check in case the shop is bankruptcy
                
                if want_milk > cash_status:
                    print(f"Can't restock Milk, insufficient funds, need {want_milk} but only have {cash_status:.2f}.")
                    print(f"Went bankrupt restocking in month {month}.")
                    capacity_ingredient = dict(coffee_shop.get_existing_quantity())
                   
                    list_baristas = coffee_shop.get_baristas(barista) 
                    bankrupt = Bankrupt()
                    bankrupt.final_display(month, cash_status, milk, beans, spices, list_baristas, capacity_ingredient,depreciation_factor)
                    break  # End the simulation due to bankruptcy
                else:
                    if want_beans > cash_status:
                        print(f"Can't restock Beans, insufficient funds, need {want_beans} but only have {cash_status:.2f}.")
                        print(f"Went bankrupt restocking in month {month}.")
                        capacity_ingredient = dict(coffee_shop.get_existing_quantity())
                        
                        list_baristas = coffee_shop.get_baristas(barista) 
                        bankrupt = Bankrupt()
                        bankrupt.final_display(month, cash_status, milk, beans, spices, list_baristas, capacity_ingredient,depreciation_factor)
                        break  # End the simulation due to bankruptcy
                    else:
                        if want_spices > cash_status:
                            print(f"Can't restock Beans, insufficient funds, need {want_spices} but only have {cash_status:.2f}.")
                            print(f"Went bankrupt restocking in month {month}.")
                            capacity_ingredient = dict(coffee_shop.get_existing_quantity())
                            
                            list_baristas = coffee_shop.get_baristas(barista) 
                            bankrupt = Bankrupt()
                            bankrupt.final_display(month, cash_status, milk, beans, spices, list_baristas, capacity_ingredient,depreciation_factor)
                            break  # End the simulation due to bankruptcy
                
                # optional: simulation automatically making decisions for each month
                test = Owner(coffee_program, barista, sale_list)
                test.run_simulation(month)
               
    except ValueError:
        print("Please input only numbers")
        continue
    
    break


    
    
    
    
    
    
    
    
    
    
    
    
    
    
