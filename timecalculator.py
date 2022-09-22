# Filename: timecalculator.py
# Author: Gabriel Malabanan
# Date: September 20, 2022
# Program Description: Write a program that asks the user a number of seconds, and convert the seconds to days,
#                      hours, mintues and/or seconds and display output

# Input: Ask user for the number of seconds
# 
# Process: 1. Input number of seconds
#          2. Determine number of 
#          3.
#          4. Output converted number of seconds to days, hours, minutes, and/or seconds
#
# Output: Display number of

# Hint: Find the remainder % (modulus operator)

print ("Time Calculator")
print ("=" *15)
print()

mins = 60
hours = 3600
days = 86400


seconds = int(input('Please enter the number of seconds: '))

if seconds >= 60 and seconds <= 3600:
    mins = seconds // 60
    seconds = seconds % 60
    print ("Minutes: ", mins, "and",seconds, "seconds")
elif seconds >= 3600 and seconds <= 86400:
    mins
