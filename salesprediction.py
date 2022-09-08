# Program name: salesprediction.py
# Author: Gabriel Malabanan
# Date: September 8, 2022
# Program Description: Write a program that asks the user to enter projected amount of total sales, and display the profit made from that amount

# Input: projected amount of total sales
# Processing: 1. Input project amount of total sales
#             2. Calculate 23% of total sales
#             3. Display the profit that will be made from total sales
# Output: total profit made

# Define Constants
ANNUAL_PROFIT = 0.23

# Asks user to input total amount of sales
totalSales = float(input('What is the amount of total sales this year?: '))

# Calculate profit made from total sales
profitFromSales = float(totalSales * ANNUAL_PROFIT)

#Displays profit made from total sales
print("The projected amount of sales this year is: $", totalSales)
print(" The profit that will be made from total sales is: $",format(profitFromSales,',.2f'))