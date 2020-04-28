# File: project.py
# Author: Denton Apple, Erin Ellis, Patrick Kimball
# Date: 04/026/2020
# Section: 504
# E-mail: denton_apple@tamu.edu
# Description:

import csv
import matplotlib.pyplot as plt
import pandas as pd

data = open("2019_car_sale.csv")

def car_deals():
    '''This function calculates the total number of car salesin 2019'''
    
    num_deals = 0
    models_list = []
    for row in data:
        num_deals += 1 
    
    return num_deals - 1

def models():
    '''This function returns the number of different car models sold in 2019'''
    
    car_models = {}
    models_list = pd.read_csv("2019_car_sale.csv")
    operation = models_list[models_list.columns[0]].values
    models_list = operation.tolist()
    
    for model in models_list:
        if model in car_models:
            car_models[model] = car_models[model] + 1
        else:
            car_models[model] = 1
    
    models_order = sorted(car_models, key=car_models.get, reverse=True)
    return len(models_order)

def brands():
    '''This function returns the number of different car brands sold in 2019'''
    
    num_car_brands = {}
    car_brands = pd.read_csv("2019_car_sale.csv")
    car_op = car_brands[car_brands.columns[2]].values
    car_brands = car_op.tolist()

    for brand in car_brands:
        if brand in num_car_brands:
            num_car_brands[brand] = num_car_brands[brand] + 1
        else:
            num_car_brands[brand] = 1
            
    brands_order = sorted(num_car_brands, key=num_car_brands.get, reverse=True)
    return len(brands_order)

def safety():
    '''This function returns the number of different safety ratings of the cars 
    sold in 2019'''
    
    car_safety = {}
    sfty_rate = pd.read_csv("2019_car_sale.csv")
    sfty_op = sfty_rate[sfty_rate.columns[4]].values
    sfty_rate = sfty_op.tolist()

    for rate in sfty_rate:
        if rate in car_safety:
            car_safety[rate] = car_safety[rate] + 1
        else:
            car_safety[rate] = 1
            
    rate_order = sorted(car_safety, key=car_safety.get, reverse=True)
    return len(rate_order)

def colors():
    '''This function returns the number of different car colors sold in 2019'''
    
    car_colors = {}
    car_color = pd.read_csv("2019_car_sale.csv")
    color_op = car_color[car_color.columns[6]].values
    car_color = color_op.tolist()

    for color in car_color:
        if color in car_colors:
            car_colors[color] = car_colors[color] + 1
        else:
            car_colors[color] = 1
            
    color_order = sorted(car_colors, key=car_colors.get, reverse = True)
    return len(color_order)

def sales():
    '''This function returns the total amount of sale, in dollars, of cars 
    sold in 2019'''
    
    car_sales = pd.read_csv("2019_car_sale.csv")
    sales_op = car_sales[car_sales.columns[5]].values
    car_sales = sales_op.tolist()

    total_sale = 0
    for i in range(len(car_sales)):
        car_sales[i] = car_sales[i].replace(",","")
        car_sales[i] = int(car_sales[i])
        total_sale += car_sales[i]
        
    return total_sale

def main():
    '''This function is the driver of the program, returning all of the dataset
    details'''
    
    print("************************* Dataset Details************************", "\n")
    print(f"Total number of deals: {car_deals()}")
    print(f"Number of different car models: {models()}")
    print(f"The number of different car brands: {brands()}")
    print(f"The number of different car safety ratings: {safety()}")
    print(f"The number of different car colors: {colors()}")
    print(f"Total amount of sale: ${sales()}")
    print()
    print("*******************************************************************")
    
main()

def state_sales():
    '''This function plots the amount of car sales per state in 2019 on a bar chart'''
    
    state_sale = {}
    states = pd.read_csv("2019_car_sale.csv")
    states_op = states[states.columns[3]].values
    states = states_op.tolist()
    #print(len(states))
    amount = pd.read_csv("2019_car_sale.csv")
    amount_op = amount[amount.columns[5]].values
    amount = amount_op.tolist()
    
    for i in range(len(amount)):
        amount[i] = amount[i].replace(",","")
        amount[i] = int(amount[i])
    
    #print(len(amount))    
    texas_sale = 0
    cal_sale = 0
    flor_sale = 0
    nevada_sale = 0
    ohio_sale = 0
    for j in range(len(states)):
        if states[j] == "Texas":
            texas_sale += amount[j]
        elif states[j] == "California":
            cal_sale += amount[j]
        elif states[j] == "Florida":
            flor_sale += amount[j]
        elif states[j] == "Nevada":
            nevada_sale += amount[j]
        elif states[j] == "Ohio":
            ohio_sale += amount[j]
            
    x_values = ["Texas", "California", "Florida", "Nevada", "Ohio"]
    y_values = [texas_sale, cal_sale, flor_sale, nevada_sale, ohio_sale]
    plt.xlabel("State", fontsize=16)
    plt.ylabel("Amount of Sale($1 hundred million)", fontsize=16)
    plt.title("Amount of Sale in Different States", fontsize=18, color='b')
    plt.bar(x_values, y_values, color='r')
    plt.text(1.5, 85000000, "Florida had\nhighest sales", color='grey', fontsize=10)
    plt.ylim(ymax = 100000000, ymin = 0)
    plt.show()
    
state_sales()    
data.close()