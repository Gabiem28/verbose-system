# Programn name: speedingfinecalculator.py
# Author: Gabriel Malabanan
# Date: October 13, 2022
# Program Description: Write a program that will prompt for the speed limit and the actual speed the motorist was measured travelling. When the information is entered, the program
#                      will determine wheter a fine is due or not and if a fine is due, what the fine amount is. Posted speed limit will always be a whole number
#
# Input: speedLimit, speedOfMotorist
# 
# Process: 1. Prompt user for the speed speed limit and the speed of the motorist
#          2. If motorist is within speed limit, fine is not given. If they are above speed limit, a fine will be given
#          3. Calculate fine based on the following:
#               25 or lower: $70
#               26 - 45: $85
#               46-45: $100
#               over 65: $150
#          4. For every unit of speed over speed limit +5, $5 is added to the fine
#          5. Display fine of the motorist
# 
# Output: Total fine of Motorist
#



# Intro
print ("Speeding Fine Calculator...")
print ("=" * 30, "\n")

# Constants for fine
FINE_25_LOWER = 70
FINE_26_TO_45 = 85
FINE_46_TO_65 = 100
FINE_OVER_65 = 150 
EVERY_SPEED_5 = 5

# Constants for each speed limit
SPEED_LIMIT_1 = 25
SPEED_LIMIT_2 = 26
SPEED_LIMIT_3 = 46
SPEED_LIMIT_4 = 65

# Defined motorFine to be used in conditional statements
motorFine = 0

# Prompts user to input speed limit and motorist's fine
speedLimit = int(input('What is the speed limit?: '))
motorSpeed = int(input('What was the motorist\'s speed?: '))


#Conditional statements
if speedLimit >= SPEED_LIMIT_2 and speedLimit < SPEED_LIMIT_3:
    motorFine = FINE_26_TO_45

elif speedLimit >= SPEED_LIMIT_3 and speedLimit < SPEED_LIMIT_4:
    motorFine = FINE_46_TO_65

elif speedLimit >= SPEED_LIMIT_4:
    motorFine = FINE_OVER_65
else:
    motorFine = FINE_25_LOWER



# Prints the total motorist fine
print ("Your fine is: $", motorFine, sep ="")
