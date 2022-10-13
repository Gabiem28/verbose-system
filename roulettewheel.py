# Filename: roulettewheel.py
# Author: Gabriel Malabanan
# Date: September 26, 2022
# Program Description: Write a program that asks user to enter a pocket number (0-36) and display whether
#                      pocket is green, red or black
#
# Input: Ask user for pocketNumber
#
# Process: 1. Input pocket number
#          2. Determine whether ball is within 0-36. If not in range, display invalild pocket
#          3. Determine whether ball is 0. Print green if ball is 0
#          4. Determine whether ball is even between 1-10 and 19-28. If so, ball is black. If not, ball is red
#          5. Determine whether ball is even between 11-18 and 29-36. If so, ball is red. If not, ball is black
#
# Output: Display pocketColor



#Intro
print ("Roulette Wheel Colors App ...")

# Asks user to input and defines range of pocketNumber
pocketNumber = int(input("Please enter a pocket number (0-36): "))
if pocketNumber >= 0 and pocketNumber <=36:

# Processing
    if pocketNumber == 0:
        pocketColor = "green"

    elif pocketNumber >= 1 and pocketNumber <= 10:
        if pocketNumber % 2 == 0:
            pocketColor = "black"
        else:
            pocketColor = "red"

    elif pocketNumber >= 11 and pocketNumber <= 18:
        if pocketNumber % 2 == 0:
            pocketColor = "red"
        else:
            pocketColor = "black"

    elif pocketNumber >= 19 and pocketNumber <= 28:
        if pocketNumber % 2 == 0:
            pocketColor = "black"
        else:
            pocketColor = "red"

    elif pocketNumber >= 29 and pocketNumber <= 36:
        if pocketNumber % 2 == 0:
            pocketColor = "red"
        else:
            pocketColor = "black"
    print ("The Color of the Wheel Pocket is", pocketColor,".")
    
else:
    # Displays error if number not within range
    print ("Error ... Invalid pocket. Try Again")
