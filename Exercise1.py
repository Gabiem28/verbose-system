# Program name: Excercise1.py
# Author: Gabriel Malabanan
# Date: September 8, 2022
# Program Description: Write a program that prompts the user for two numbers, then calculate and output the sum, difference, product and quotient of two numbers.

# Asks to input 1st and 2nd number
numberOne = float(input ('Enter 1st number: '))
numberTwo = float(input ('Enter 2nd number: '))

# Calculations
numberAdd = float(numberOne + numberTwo)
numberSubtract = float(numberOne - numberTwo)
numberMult = float(numberOne * numberTwo)
numberDivide = float(numberOne / numberTwo)


# Prints the values of the two numbers
print ("The two numbers were: ",numberOne, "and",numberTwo)
print ("The sum of the two numbers is :",numberAdd)
print ("The difference of the two numbers is :",numberSubtract)
print ("The product of the two numbers is :",numberMult)
print ("The quotient of the two numbers is :",numberDivide)

