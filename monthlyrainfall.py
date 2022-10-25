# Programn name: monthlyrainfall.py
# Author: Gabriel Malabanan
# Date: October 24, 2022
# Program Description: Given information about monthly rainfall for a period of time, caclulate the total and average monthly rainfall during a period.
#                      Write a program that uses nested loops to collect data and calculate average rainfall over a period of years. Should first
#                      ask for number of years, and outer loop will iterate once a year, inner loop will iterate once per each month of the year.
#                      Each iteration of inner loop will ask user for the inches of the rainfall of that month. Program should then display number of months,
#                      total inches of rainfall and average rainfall for the entire period.
#
# Input: Number of years (numOfYears) and inches of rainfall per month (rainPerMonth) 
# 
# Process: 1. Ask user to input number of years. If input was negative, print "invalid". If positive, go on to the next step.
#          2. Prompt the user to enter monthly rainfall per month in the number years inputted. Inner loop will will iterate twelve times.
#          3. If input was negative, print "Invalid"
#          4. Display the number of months, the total inches of raindfall and the average rainfall for the entire period.  
# Output: Total number of months, total inches of rainfall, and the average rainfall for the entire period
#

# Intro for the program
print ("Welcome to the Rainfall Program!")
print ("=" * 35)

# Variables initialized and constants declared to be later used
numOfYears = 0
rainPerMonth = 0.0
totalMonths = 0
MONTHS_PER_YEAR = 12
totalRainfall = 0.0
averageRainfall = 0.0
yearsWithRain = 0

# Asks user to input number of years
numOfYears = int(input('\nEnter the number of years: '))

# If number of years was less than 1, invalid input will be printed
while numOfYears < 1:
    print ("Invalid, number of years cannot be less than 1.")
    numOfYears = int(input('\nEnter the number of years: '))


# Outer loop once per year
for yearsWithRain in range(numOfYears):
    print ("\nYear",yearsWithRain+1)

  
    # Inner loop 12 times in a month
    # Prompts user for inches of rainfall per month
    for month in range(MONTHS_PER_YEAR):
        print ("Enter the monthly rainfall for month (in)", (month + 1),":",end =" ")
        rainPerMonth = float(input())

        while (rainPerMonth < 0):
            print ("Invalid, amount of rainfall cannot be negative") 
            print ("Enter the monthly rainfall for month (in)", (month + 1),":",end =" ")
            rainPerMonth = float(input())

        totalMonths += 1
        totalRainfall += rainPerMonth
     


# Calculates for the total amount of months and average rainfall during the period
totalMonths = numOfYears * MONTHS_PER_YEAR
averageRainfall = totalRainfall / totalMonths

       
# Ouput the total number of months, total rainfall and average rainfall
print ("=" * 50)
print ("\nTotal number of months:       ", totalMonths)
print ("Total Rainfall in inches:     ", format(totalRainfall,'.2f'))
print ("Average Rainfall:             ",format(averageRainfall,'.2f'))
