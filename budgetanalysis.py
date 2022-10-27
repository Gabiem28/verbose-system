# Program Name: budgetanalysis.py
# Author: Gabriela Malabanan
# Date: October 27,2022
# Program Description: Write a program that asks user to enter amount of money her or she has budgeted for a month.
#                      Then, prompt user to enter each of his expenses for the month and keep a running total.
#                      When the user is finished entering their expenses, the program should display the amount that the user
#                      is under or over budget.
#
# Input: Amount of money user has budgeted for a month, each of the users expenses
# 
# Processing: 1. Asks user to input money he or she has budgeted for a month
#             2. Then, prompt user to enter each of his or her expenses for the month and keep a running total.
#             3. Asks the user if they are finished entering expenses.
#             4. Display the total amount of expenses and if they are under or over budget
#
# Output: Total expenses for the month, and if user is under or over budget


print("Welcome to Budget Analysis!")
print("*" * 30)


expenses = 0
totalExpenses = 0

monthlyBudget = float (input('How much have you budgeted for this month?: '))



totalExpenses += expenses 
under_over_budget = monthlyBudget - totalExpenses


print 


print ("Your total budget for this month is: $",format(monthlyBudget,'.2f'),sep=" ")
print ("Your total expenses for this month is: ",totalExpenses)