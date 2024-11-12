# ws23365_EMATM0048
Coursework of EMATM0048

## Name: Isarapon Prasertstid

## Link: [https://github.com/IsaraponPrasertstid/ws23365_EMATM0048.git](https://github.com/IsaraponPrasertstid/ws23365_EMATM0048)

## Part 1:
The Coffee Shop Program is created to simulate the coffee shop operation. The user can input sales quantity and make decision to add or remove baristas. The program will show the basic information such as expenditure, cash and stock. The aim of the Coffee Shop Program is to make a profit and avoid going bankrupt.

In order to write code more easily and perform many operations for this task, I use an object-oriented programming approach to create multiple classes. To enhance code maintainability, I employ the principle of encapsulation. I also utilize the inheritance principle, allowing the child class to leverage the capabilities of the parent class.

### Files Description

1.	**coffee_program.py**
This file contains CoffeeProgram class. The CoffeeProgram class provides the main interface for interacting with the coffee program, including methods for receiving user input and displaying information.

This class includes methods:
  -	**mounth_input**: Allow the user to input the number of months.
  -	**theme_month**: Set and display of current month on the screen.
    
2.	**insufficient.py**
This file contains Insufficient class which is class for managing constraints of the coffee shop. This class is ensuring that the sale input do not exceed constraints related to demand, ingredients, and labor.

This class includes methods:
  - **calculate_insufficient**: Calculate and check constraints related to demand, ingredients, and labor. This method takes into account various factors such as coffee types, specialty baristas, and barista labor.
    
3.	**main.py**
This file is the entry point for the coffee shop program. You can run the coffee shop program in here.

There are initialises instances of other classes and perform simulation here.

4.	**owner.py**
This file contains Owner class which is extending the functionalities of CoffeeShop. This class adds optional way to make a decision with coffee shop. It inherits from the CoffeeShop class, and it have its own methods.

This class includes methods:
  -	**run_simulation**: Run a monthly simulation for the coffee shop.
  -	**make_decisions**: Make decisions based on the current cash status of the coffee shop. make_decisions method evaluates the cash status and makes decisions to avoid bankruptcy. These decisions are based on the current cash status from the test method.
    
5.	**bankrupt.py**
This file contains Bankrupt class. Bankrupt will handle and display when the coffee shop is bankruptcy. This class provides methods to show the status of the coffee shop, focusing on the cash status and ingredient views, which are important in the evaluation of bankruptcy.

This class includes methods:
  - **final_display**: Show coffee shop's status, including cash balance, ingredient, and barista details.
    
6.	**barista.py**
This file contains Barista class. Barista Class responsible is for managing barista operations. It handles the add, remove and tracking baristas.

This class includes methods:
  - **add_barista**: Add a new barista to the coffee shop. This method will increment the number of baristas and adds a new barista to the list.
  -	**get_baristas**: Get barista list.
  -	**get_number_baristas**: Get number of baristas.
  -	**remove_barista**: To enable user removing barista.
  -	**can_remove_baristas**: Check whether number of removed baristas is less than or equal to current total baristas or not? in order to check if the user is typing wrong value.
    
7.	**coffee_shop.py**
This file contains CoffeeShop class. CoffeeShop Class is the main operations of a coffee shop. This class manage a number of things such as cash status, income and expenditure calculations, ingredient purchasing, barista information.

This class includes methods:
  -	**get_coffee_recipe**: Method to return (get) coffee_types
  -	**get_baristas**: Method to retrieve list barista names from outside and return the list of barista names.
  -	**get_number_baristas**: Method to retrieve the number of baristas from outside and return the number of baristas.
  -	**get_existing_quantity**: Method to return (get) quantities.
  -	**get_depreciation**: Method to return (get) depreciation.
  -	**calculate_income**: Method to calculate income from each coffee type.
  -	**calculate_expense_baristas**: Method to calculate cost of barista.
  -	**calculate_ingredient_costs**: Method to calculate cost of pantry.
  -	**ingredient_stock**: Method to calculate ingredient stock.
  -	**buy_new_ingredient**: Method to calculate cost of ingredient.
  -	**cash_status**: Method to calculate cash status of coffee shop.
  -	**test**: Method to return cash status.
    
8.	**supplier.py**

This file contains Supplier class. Supplier class provides a supplier name and prices in each ingredient.

This class includes methods:
  -	**get_price_from_supplier**: Method to get prices from each ingredient from a specific supplier.
    
## Instructions for Running Part 1 Code
1. Clone this repository: [GitHub Repository](https://github.com/IsaraponPrasertstid/ws23365_EMATM0048.git)
2. Run the coffee shop program by using main.py

## Part 2:
I have to import another library
1. For making HTTP requests
   - import requests

2. Analysing data
   - import pandas as pd
  - import numpy as np 
3. Plot graph
  - import matplotlib.pyplot as plt
  - import seaborn as sns

4. Fitting simple linear regression
  - from sklearn.linear_model import LinearRegression

5. splitting the dataset into the training set and test set
  - from sklearn.model_selection import train_test_split
6. Fitting polynomial
  - from sklearn.preprocessing import PolynomialFeatures
7. Finding error both MSE and R^2
  - from sklearn.metrics import mean_squared_error, r2_score
8. Convert a string containing a list into an actual python list object
  - import ast 
    
## Instructions for Running Part 2 Code
1. Clone this repository: [GitHub Repository](https://github.com/IsaraponPrasertstid/ws23365_EMATM0048.git)
2. Install the fllowing packages
   - pip install requests
   - pip install pandas
   - pip install numpy
   - pip install matplotlib
   - pip install seaborn
   - pip install scikit-learn
3. Run the data_analytic_eonet.ipynb

   **IMPORTANT**
The old file I previously sent had a problem because the API changed data in that link and resulted in my analytic. During my last data analysis, I did not use the CSV file, which led to issues when the API was affected. In this new submission, I used the data from the old CSV file for direct analysis. However, there was a problem with a column called 'coordination' in the old file, so I had to make some corrections. That are the reason for this update.
