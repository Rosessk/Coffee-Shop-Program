#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:50:27 2023

@author: blackrose
"""

class Insufficient: 
    """Class for managing constraints of the coffee shop.
     This class is ensuring that the sale input do not exceed
    constraints related to demand, ingredients, and labor."""
    
    def __init__(self, coffee_shop):        
        """Initalise the Insufficient class with the barista salary and refer to 
        the CoffeeShop class (coffee_shop)"""
        self._hr_perperson = 80 * 60  # 80 hours/person in a month
        self._coffee_shop = coffee_shop


    def calculate_insufficient(self, coffee_types, specialty_counts, barista, month):
        """Calculate and check constraints related to demand, ingredients, and labor.
        This method takes into account various factors such as coffee types, specialty baristas, and barista labor."""
        
        # get the number of baristas from CoffeeShop class
        number_of_baristas = self._coffee_shop.get_number_baristas(barista)
        
        # caculate the overall labor time of every barista
        labor_time = number_of_baristas * self._hr_perperson
        
        
        # initalise total time
        total_time = 0
        
        # initalise ingredient usage
        milk_usage = 0
        beans_usage = 0
        spices_usage = 0
        
        # set sale_list = 0 to collect all quantities that user want to sell
        sale_list = []
        
        # baseline ingredient quantities
        existing_ingredient = dict(self._coffee_shop.get_existing_quantity())
        milk = existing_ingredient['Milk']
        beans = existing_ingredient['Beans']
        spices = existing_ingredient['Spices']
        
       
           
        try: 
            
            for type, coffee_detail in self._coffee_shop.get_coffee_recipe():
                
                milk_portion = coffee_detail['Milk']
                beans_portion = coffee_detail['Beans']
                spices_portion = coffee_detail['Spices']
                
                month_demand = coffee_detail['MonthlyDemand']
                prepare_time = coffee_detail['Time']
                
               
                
                condition = True
                
                while condition:
                    
                    
                    valid_input = False  # check if input is valid
        
                    while not valid_input:  # looping until valid input is received
                         try:
                             preferred_sale = int(input(f"Coffee {type}, demand {month_demand}, how much to sell: "))
        
                             if preferred_sale < 0:
                                 # if the input is negative, it will print an error and continue the loop
                                 print("Sale cannot be negative. Please enter a positive value.")
                             else:
                                 # if input is valid -> change it to True to break out of the loop
                                 valid_input = True
        
                         except ValueError:
                             # if input is not an integer, it will go to exception and print an error
                             print("Invalid input. Please enter a valid integer.")

     
                   # preferred_sale = int(input(f"Coffee {type}, demand {month_demand}, how much to sell: "))
                   # for check
                    if not isinstance(specialty_counts, dict):
                       raise ValueError("specialty_counts must be a dictionary!!!!!!!!!!!!!!!!!!!")
   
                    # if there is no specialist
                    if list(specialty_counts.keys()) == ['no']:
                        time_will_use = preferred_sale * prepare_time
                    
                        # check if the preferred sale quantity is within the monthly demand limit
                        if preferred_sale <= month_demand:
                            milk_will_use = preferred_sale * milk_portion #ml
                            beans_will_use = preferred_sale * beans_portion
                            spices_will_use = preferred_sale * spices_portion
                            
                            # check labor capacity
                            if ((time_will_use + total_time) > labor_time):
                                capacity = (labor_time - total_time)/prepare_time
                                print(f"Insufficient labour: quantity requested {preferred_sale}, capacity {int(capacity)}")
        
                                # Check ingredient availability
                                if ((milk_usage + milk_will_use) > milk) or ((beans_usage + beans_will_use) > beans) or ((spices_usage + spices_will_use) > spices):
                                
                                    milk_need = (preferred_sale * milk_portion)  #litre
                                    beans_need = preferred_sale * beans_portion
                                    spices_need = preferred_sale * spices_portion
                                    
                                    have_milk = (milk - milk_usage)  #litre
                                    have_beans = beans - beans_usage
                                    have_spices = spices - spices_usage
    
                                    print("Insufficient ingredients:")
                                    print(f"milk need {milk_need} pantry {have_milk}")
                                    print(f"beans need {beans_need:.1f} pantry {have_beans:.1f}")
                                    print(f"spices need {spices_need:.1f} pantry {have_spices:.1f}")

                                condition = True
            
                             # Check ingredient availability    
                            elif ((milk_usage + milk_will_use) > milk) or ((beans_usage + beans_will_use) > beans) or ((spices_usage + spices_will_use) > spices):
                                milk_need = (preferred_sale * milk_portion)  #litre
                                beans_need = preferred_sale * beans_portion
                                spices_need = preferred_sale * spices_portion
                                
                                have_milk = (milk - milk_usage) #litre
                                have_beans = beans - beans_usage
                                have_spices = spices - spices_usage
                                
                                print("Insufficient ingredients:")
                                print(f"milk need {milk_need} pantry {have_milk}")
                                print(f"beans need {beans_need:.1f} pantry {have_beans:.1f}")
                                print(f"spices need {spices_need:.1f} pantry {have_spices:.1f}")
  
                                # Check labor capacity
                                if ((time_will_use + total_time) > labor_time):
                                    capacity = (labor_time - total_time)/prepare_time      
                                    print(f"Insufficient labour: quantity requested {preferred_sale}, capacity {int(capacity)}")

                                condition = True

                            else:
                                # Update ingredient usages and time
                                total_time += prepare_time * preferred_sale
                                milk_usage += preferred_sale * milk_portion 
                                beans_usage += preferred_sale * beans_portion
                                spices_usage += preferred_sale * spices_portion
                                
                                sale_list.append(preferred_sale)

                                condition = False
                        else:
                            print(f"Insufficient demand for {preferred_sale}, demand is {month_demand}") #chack again
                            condition = True
                    
                            
                    # in case, there is at least one specialist 
                    else:  
                        # Check if the preferred sale quantity is within the monthly demand limit
                        if preferred_sale <= month_demand:
                            milk_will_use = preferred_sale * milk_portion #ml
                            beans_will_use = preferred_sale * beans_portion
                            spices_will_use = preferred_sale * spices_portion
                            
                            specialty_counts # {'Americano': 1, 'Filter': 1}
                            
                            # initalise value of time
                            labor_time_special = 0
                            labor_time_non_special = 0
                            
                            # initalise value of time only in month 1 and first type of coffee
                            if month == 1 and type == 'Expresso':
                                time_special = 0  
                                time_non_special = 0  

                            # check if type is in specialty_counts dict and assign to type_cheeck
                            if type in specialty_counts:
                                type_cheeck = type
                            else:
                                type_cheeck = None
                            
                            # if type = first type of coffee, then initalise value for first time
                            if type == 'Expresso':
                                for specialty, count in specialty_counts.items():
                                    if type_cheeck == type:
                                        # count total_time_special
                                        labor_time_special += count * self._hr_perperson                                  
                                    else:
                                        labor_time_non_special += count * self._hr_perperson                                
                                time_non_special = 0
                                # Time required for NON-specialty   
                                for key, value in specialty_counts.items():
                                    if key != type:
                                        time_non_special += value * 80 * 60    
                            else:
                                if type_cheeck != None:
                                    time_non_special -= specialty_counts[type_cheeck]     
                                else:
                                    pass
                                
                            coffee_types = dict(coffee_types)       
                       
                            # go to case specialist for calculating labor time
                            if type_cheeck == type:
                                # calculate time required 
                                if type == 'Expresso':
                                    for type_coffee, count_barista in specialty_counts.items():
                                        specialty_counts[type_coffee] = count_barista * 80 * 60
                                    time_special = specialty_counts[type_cheeck]
                                                           
                                # time required for  specialty coffee type    
                                time_special = specialty_counts[type_cheeck] * 80 * 60
                                                           
                                # if there is only special but not non-special, give the time that not use to non-special
                                if type_cheeck == type and len(specialty_counts.keys()) == 1:
                                    time_non_special = time_special - coffee_types[type_cheeck]['Time'] * preferred_sale
                                    time_special = coffee_types[type_cheeck]['Time'] * preferred_sale
                                    
                                                       
                                coffee_types = dict(coffee_types)                        
                                # calculate total time for the requested coffee type
                                time_will_use = coffee_types[type]['Time'] * preferred_sale
                                    
                                    
                                # check if the time required exceeds the capacity of the specialized barista        
                                if time_will_use > time_special * 2:
                                    time_will_use -= time_special * 2 # the specialize person can do 2 time from normal
                                    time_non_special # still the same
                                 #   print(time_non_special)
                            
                                        
                                        # check if non-specialized baristas can handle the existing workload
                                    if time_non_special > time_will_use:
                                        time_non_special -= time_will_use
                                        # update value
                                        time_special = 0  # there is nothing left
                                        specialty_counts[type_cheeck] = time_special # to be zero
                                        condition = False
                                            
                                            
                                    # if not, calculate the maximum capacity and inform about insufficient labor    
                                    else:
                                        capacity = (time_non_special/coffee_types[type]['Time']) + ((time_special*2)/coffee_types[type]['Time'])  
                                        print(f"Insufficient labour: quantity requested {preferred_sale}, capacity {int(capacity)}")
                       
                                        labor_time = 'Insufficient'
                                        condition = True
                                            # check ingredient availability
                                        if ((milk_usage + milk_will_use) > milk) or ((beans_usage + beans_will_use) > beans) or ((spices_usage + spices_will_use) > spices):
                                            
                                            milk_need = (preferred_sale * milk_portion)  #litre
                                            beans_need = preferred_sale * beans_portion
                                            spices_need = preferred_sale * spices_portion
                                                
                                            have_milk = (milk - milk_usage)  #litre
                                            have_beans = beans - beans_usage
                                            have_spices = spices - spices_usage
                
                                            print("Insufficient ingredients:")
                                            print(f"milk need {milk_need} pantry {have_milk}")
                                            print(f"beans need {beans_need:.1f} pantry {have_beans:.1f}")
                                            print(f"spices need {spices_need:.1f} pantry {have_spices:.1f}")
                                               
                                        condition = True
                                                  
                                    
                                # if the specialized barista can handle the workload, update the time left for them
                                else:
                                    time_special  -= time_will_use / 2
                                    specialty_counts[type_cheeck] = time_special
                                    time_non_special = specialty_counts[type_cheeck] + time_non_special
                                    condition = False
                                    labor_time = 'sufficient'
                                    
                                        
                            # if the requested type is not a specialty, use non-specialized labor time        
                            else:
                                try:
                                    time_special
                                except UnboundLocalError:
                                    time_special = 0
                                    
                                coffee_types = dict(coffee_types)
                                if time_non_special + time_special < coffee_types[type]['Time'] * preferred_sale:

                                    capacity = ((time_non_special + time_special)/coffee_types[type]['Time']) ######
                          #          print(";;;;")
                              #      print(time_non_special, time_special)
                                    print(f"Insufficient labour: quantity requested {preferred_sale}, capacity {int(capacity)}")
                                    labor_time = 'Insufficient'
                                    
                                    condition = True    
                                    
                                    # check ingredient availability
                                    if ((milk_usage + milk_will_use) > milk) or ((beans_usage + beans_will_use) > beans) or ((spices_usage + spices_will_use) > spices):
                                        
                                        milk_need = (preferred_sale * milk_portion)  #litre
                                        beans_need = preferred_sale * beans_portion
                                        spices_need = preferred_sale * spices_portion
                                            
                                        have_milk = (milk - milk_usage)  #litre
                                        have_beans = beans - beans_usage
                                        have_spices = spices - spices_usage
            
                                        print("Insufficient ingredients:")
                                        print(f"milk need {milk_need} pantry {have_milk}")
                                        print(f"beans need {beans_need:.1f} pantry {have_beans:.1f}")
                                        print(f"spices need {spices_need:.1f} pantry {have_spices:.1f}")
                                        condition = True
                                                
                                 
                                    
                                else:
                                    time_non_special = time_non_special + time_special
                                    time_non_special += -coffee_types[type]['Time'] * preferred_sale
                                    # in case, next loop is special so time_non_special will be not overlap with time_special
                                    
                                    time_non_special -=  time_special ###########
                                    if time_non_special > 0:
                                        pass
                                    else:
                                        time_special = time_special + (time_non_special - time_special)
                                        time_non_special = 0
                                        
                                    if time_special < 0:
                                        time_special = 0
                                        
                              
                                    
                                   # print(time_non_special, time_special)
                                    labor_time = 'sufficient'
                                    # print(f'time_non_special = {time_non_special}')
                                    condition = False
                                        

                          # check labor capacity

                            if labor_time != 'Insufficient':
                                
                                # check ingredient availability
                                if ((milk_usage + milk_will_use) > milk) or ((beans_usage + beans_will_use) > beans) or ((spices_usage + spices_will_use) > spices):
                                
                                    milk_need = (preferred_sale * milk_portion)  #litre
                                    beans_need = preferred_sale * beans_portion
                                    spices_need = preferred_sale * spices_portion
                                        
                                    have_milk = (milk - milk_usage)  #litre
                                    have_beans = beans - beans_usage
                                    have_spices = spices - spices_usage
        
                                    print("Insufficient ingredients:")
                                    print(f"milk need {milk_need} pantry {have_milk}")
                                    print(f"beans need {beans_need:.1f} pantry {have_beans:.1f}")
                                    print(f"spices need {spices_need:.1f} pantry {have_spices:.1f}")
                                        
                                    condition = True    
                                else:
                                    # update ingredient usages and time
                                    total_time += prepare_time * preferred_sale
                                    milk_usage += preferred_sale * milk_portion 
                                    beans_usage += preferred_sale * beans_portion
                                    spices_usage += preferred_sale * spices_portion
                                        
                                    sale_list.append(preferred_sale)
                                  #  print(sale_list)
                                    
                                    condition = False
                                    
                                

                        else:
                            print(f"Insufficient demand for {preferred_sale}, demand is {month_demand}") #chack again
                            condition = True
                        
                      
            # update ingredient quantities
            milk -= milk_usage
            beans -= beans_usage
            spices -= spices_usage

        except ValueError:
            print("Please input only numbers.") 
        
        return milk, beans, spices, sale_list
    
    
    
    