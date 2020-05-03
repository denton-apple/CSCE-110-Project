# File: project.py
# Author: Denton Apple, Erin Ellis, Patrick Kimball
# Date: 04/026/2020
# Section: 504
# E-mail: denton_apple@tamu.edu, pskimball1@tamu.edu, erinellis@tamu.edu
# Description: This program reads a csv file of car sales in 5 different states
# sold in 2019. It performs operations on the file to find the total number
# of deals, models, brands, colors, total sale, etc. This program also 
# plots 4 different plots for data visualization, showing monthly sales, 
# sales in different states, and sales by brand. 

import csv
import matplotlib.pyplot as plt
import pandas as pd
import pip

data = open("2019_car_sale.csv")

def car_deals():
    '''This function calculates the total number of car sales in 2019'''
    
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

def state_sales():
    '''This function plots the amount of car sales per state in 2019 on a bar chart'''
    
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
    plt.figure(1)
    plt.xlabel("State", fontsize=16)
    plt.ylabel("Amount of Sale($1 hundred million)", fontsize=16)
    plt.title("Amount of Sale in Different States", fontsize=18, color='b')
    plt.bar(x_values, y_values, color='r')
    plt.text(1.5, 85000000, "Florida had\nhighest sales", color='grey', fontsize=10)
    plt.ylim(ymax = 100000000, ymin = 0)
    plt.show()
    
def month_sales():
    '''This function plots the monthly sales of cars sold in 2019'''
    
    month = pd.read_csv("2019_car_sale.csv")
    month_op = month[month.columns[1]].values
    month = month_op.tolist()
    #print(len(month))
    sale = pd.read_csv("2019_car_sale.csv")
    sale_op = sale[sale.columns[5]].values
    sale = sale_op.tolist()
    
    for i in range(len(sale)):
        sale[i] = sale[i].replace(",","")
        sale[i] = int(sale[i])
    #print(len(sale))
    jan = 0
    feb = 0
    mar = 0
    april = 0
    may = 0
    june = 0
    july = 0
    aug = 0
    sept = 0
    octo = 0
    nov = 0
    dec = 0
    
    for i in range(len(month) - 1):
        if month[i][0] == '1':
            if month[i][1] == "/":
                jan += sale[i]
            elif month[i][1] == "0":
                octo += sale[i]
            elif month[i][1] == "1":
                nov += sale[i]
            elif month[i][1] == "2":
                dec += sale[i]
        elif month[i][0] == '2':
            feb += sale[i]
        elif month[i][0] == '3':
            mar += sale[i]
        elif month[i][0] == '4':
            april += sale[i]
        elif month[i][0] == '5':
            may += sale[i]
        elif month[i][0] == '6':
            june += sale[i]
        elif month[i][0] == '7':
            july += sale[i]
        elif month[i][0] == '8':
            aug += sale[i]
        elif month[i][0] == '9':
            sept += sale[i]
            
    x_values = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    y_values = [jan, feb, mar, april, may, june, july, aug, sept, octo, nov, dec]
    plt.figure(2)
    plt.xlabel("Month", fontsize=15)
    plt.ylabel("Amount of Sale($)", fontsize=15)
    plt.title("Amount of Sale in Diffferent Months of 2019", fontsize=17)
    plt.plot(x_values, y_values, marker='o')
    plt.text(2.5, 42000000, "April had\nhighest sales", fontsize=10, color='grey')
    plt.ylim(ymax = 50000000, ymin = 0)
    plt.show()
    
def brand_sales():
    '''This function plots the percentage of car sales in 2019 based off of 
    different car brands'''
    
    # opening the files
    amount = pd.read_csv("2019_car_sale.csv")
    amount_op = amount[amount.columns[5]].values
    amount = amount_op.tolist()
    
    brand = pd.read_csv('2019_car_sale.csv')
    brand_op = brand[brand.columns[2]].values
    brand = brand_op.tolist()
    
    for i in range(len(amount)):
        amount[i] = int(amount[i].replace(',',''))
    
    # creating a dictionary for the brands and their sales
    brand_sale_dict = {}
    final_brand_sale_dict = {'Other': 0}
    total_sales = 0
    
    # adding each brand and their sales to the dictionary
    for i in range(len(brand)):
        if brand[i] in brand_sale_dict:
            brand_sale_dict[brand[i]] += amount[i]
        else:
            brand_sale_dict[brand[i]] = amount[i]
        total_sales += amount[i]
    
    # finding the brands with < 4% of the total and grouping them into Other
    for brand, sale in brand_sale_dict.items():
        if sale / total_sales < .04:
            final_brand_sale_dict['Other'] += sale
        else:
            final_brand_sale_dict[brand] = sale
    
    # sorting the final dictionary for nice graphs
    sorted_final_sales = sorted(((val, key) for (key, val) in final_brand_sale_dict.items()), reverse=True)
    #print(sorted_final_sales)
    
    
    # printing the graph
    labels = [car[1] for car in sorted_final_sales]
    sizes = [car[0] for car in sorted_final_sales]
    plt.figure(3)
    plt.title('Percentage of sale by different car brands')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()
    
def state_sales_lines():
    '''This function plots the sales amount in different states as individual
    lines on a line graph'''
    
    # opening the files
    amount = pd.read_csv("2019_car_sale.csv")
    amount_op = amount[amount.columns[5]].values
    amount = amount_op.tolist()
    
    dates = pd.read_csv('2019_car_sale.csv')
    dates_op = dates[dates.columns[1]].values
    dates = dates_op.tolist()
    
    states = pd.read_csv('2019_car_sale.csv')
    states_op = states[states.columns[3]].values
    states = states_op.tolist()
    
    
    for i in range(len(amount)):
        amount[i] = int(amount[i].replace(',',''))
    
    state_list = ['Texas', 'California', 'Florida', 'Ohio', 'Nevada']
    
    # iterating through each state and only adding the sales for those states.
    # Once that is done, it prints the graph for that state and restarts with the next state
    for state in state_list:
        jan_sales = 0
        feb_sales = 0
        mar_sales = 0
        apr_sales = 0
        may_sales = 0
        jun_sales = 0
        jul_sales = 0
        aug_sales = 0
        sep_sales = 0
        oct_sales = 0
        nov_sales = 0
        dec_sales = 0
        for i in range(len(dates)):
            if states[i] == state:
                if int(dates[i].split('/')[0]) == 1:
                    jan_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 2:
                    feb_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 3:
                    mar_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 4:
                    apr_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 5:
                    may_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 6:
                    jun_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 7:
                    jul_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 8:
                    aug_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 9:
                    sep_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 10:
                    oct_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 11:
                    nov_sales += amount[i]
                elif int(dates[i].split('/')[0]) == 12:
                    dec_sales += amount[i]
            else:
                continue
    
        # printing the graph for the current state
        x_values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                        'November', 'Decemeber']
        y_values = [jan_sales, feb_sales, mar_sales, apr_sales, may_sales, jun_sales, jul_sales, aug_sales, sep_sales,
                        oct_sales, nov_sales, dec_sales]
        plt.figure(4, figsize=(11,6))
        plt.xlabel('Month')
        plt.ylabel('Sales ($)')
        plt.title('Amount of Sales per Month per State')
        plt.plot(x_values, y_values, label=state)
    
    # showing the entire graph
    plt.legend(state_list)
    plt.show()    

def main_plots():
    '''This function is the driver of all of the graphs created for data 
    visualization'''
    
    state_sales_lines()
    brand_sales()
    month_sales()
    state_sales()

main()
main_plots()
data.close()
