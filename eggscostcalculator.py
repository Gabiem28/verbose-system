# Programn name: eggscostcalculator.py
# Author: Gabriel Malabanan
# Date: October 11, 2022
# Program Description: 
#
# Input: type of egg, number of eggs ordered
# 
# Process: 1. Ask user to input type of eggs and number of eggs they want to order
#          2. For each egg the user chooses, calculate the item of the price by multiplying
#             quantity of eggs by corresponding item cost
#          3. Calculate if there is a discount based on amount of eggs
#          4. Output total cost of ordered eggs
# 
# Output: Total cost of ordered eggs
#



print ("Eggs Cost Calculator...\n")

# Constants for type of egg and cost of each
BROWN_EGG = 0.50
WHITE_EGG = 0.75
CHOC_EGG = 1.50
RAINBOW_EGG = 2.50


DISCOUNT_2 = 0.02
DISCOUNT_3 = 0.03
DISCOUNT_4 = 0.04
DISCOUNT_5 = 0.05
DISCOUNT_6 = 0.06
NO_DISCOUNT = 0

DISCOUNT_RANGE_1 = 13
DISCOUNT_RANGE_2 = 97

eggType = str(input('Enter type of egg you would like to order:'))
eggAmount = int(input('Enter the amount of this type of egg that you would like to order: '))


if eggType == "Brown" or eggType == "brown":
    
   costOfEach = eggAmount * BROWN_EGG
   if eggAmount >= DISCOUNT_RANGE_1 and eggAmount < DISCOUNT_RANGE_2:
        discount = DISCOUNT_2
   if eggAmount >= DISCOUNT_RANGE_2:
        discount = DISCOUNT_3
   else:
    discount = NO_DISCOUNT
    
    
elif eggType == "White" or eggType == "white":
    costOfEach = eggAmount * WHITE_EGG
    if eggAmount >= DISCOUNT_RANGE_1 and eggAmount < DISCOUNT_RANGE_2:
        discount = DISCOUNT_3
    if eggAmount >= DISCOUNT_RANGE_2:
        discount = DISCOUNT_4
    else:
        discount = NO_DISCOUNT


elif eggType == "Chocolate" or eggType == "chocolate":
    costOfEach = eggAmount * CHOC_EGG
    if eggAmount >= DISCOUNT_RANGE_1 and eggAmount < DISCOUNT_RANGE_2:
        discount = DISCOUNT_4
    if eggAmount >= DISCOUNT_RANGE_2:
        discount = DISCOUNT_5
    else:
        discount = NO_DISCOUNT


elif eggType == "Rainbow" or eggType == "rainbow":
    costOfEach = eggAmount * RAINBOW_EGG
    if eggAmount >= DISCOUNT_RANGE_1 and eggAmount < DISCOUNT_RANGE_2:
        discount = DISCOUNT_5
    if eggAmount >= DISCOUNT_RANGE_2:
        discount = DISCOUNT_6
    else:
        discount = NO_DISCOUNT 
else:
    print ("Invalid Input")

if eggAmount > 0:

    discountPrice = costOfEach * discount
    finalCost = costOfEach - discountPrice

    print ("Your total cost is: $",format(finalCost,'.2f'),sep="")
else:
    print ("Must be greater than 0!")