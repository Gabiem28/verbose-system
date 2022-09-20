# Filename: softwaresales.py
# Author: Gabriel Malabanan
# Date: September 20, 2022
# Program Description: Write a program that asks for the number of units sold
#                      computes the total cost of the purchase with discount

# Input: Ask user for number of units sold
#
# Process: 1. Input units sold
#          2. Determine discount for number of units sold
#          3. Calculate as units sold times unit price minus discount
#          4. Output cost of sale with discount
#
# Output: Display total cost of the purchase

DISCOUNT_PERCENT_10_TO_19 = 0.20
DISCOUNT_PERCENT_20_TO_49 = 0.30
DISCOUNT_PERCENT_50_TO_99 = 0.40
DISCOUNT_PERCENT_OVER_100 = 0.50
DISCOUNT_RANGE_1 = 10
DISCOUNT_RANGE_2 = 20
DISCOUNT_RANGE_3 = 50
DISCOUNT_RANGE_4 = 100
PACKAGE_COST = 99


print ("Cost of Sales Calculator")
print ("=" *23)
print()

unitsSold = int(input("How many packages would you like?: "))


if unitsSold >= DISCOUNT_RANGE_1 and unitsSold < DISCOUNT_RANGE_2:
    discount = DISCOUNT_PERCENT_10_TO_19
elif unitsSold >= DISCOUNT_PERCENT_20_TO_49 and unitsSold < DISCOUNT_RANGE_3:
    discount = DISCOUNT_PERCENT_20_TO_49
elif unitsSold >= DISCOUNT_RANGE_3 and unitsSold < DISCOUNT_RANGE_4:
    discount = DISCOUNT_PERCENT_50_TO_99
elif unitsSold >= DISCOUNT_RANGE_4:
    discount = DISCOUNT_PERCENT_OVER_100
else:
    discount = 0

if unitsSold > 0:

    #Calculate cost
    costOfSalesNoDiscount = unitsSold * PACKAGE_COST
    totalDiscount = costOfSalesNoDiscount * discount
    costOfSales = costOfSalesNoDiscount - totalDiscount

    #Display Cost
    print()
    print("Cost of sales = $",format(costOfSales,'.2f'))

else:
    print ("Number of packages must be greater than 0!!!")
