


print ("Welcome to the Konditorei Coffee Shop!\n")

# Define constants for coffee cost per pound, shipping and overhead cost
COFFEE_COST = 10.50 
SHIPPING_COST = 0.86
OVERHEAD_COST = 1.50

# Prompts user to enter amount of coffee they would like to purchase
print ("Cost of coffee per :")
print ("$10.50 per lb")
print ("Shipping Cost:")
print ("$0.86 + fixed cost of $1.50\n")
coffeeWeight = float (input('Enter amount of coffee you would like to purchase (lbs): '))

# Calculations for total cost of shipping
totalCost = (SHIPPING_COST + COFFEE_COST) * coffeeWeight + OVERHEAD_COST


# Display totalCost as output
print ("Your total cost for the coffee is: $",format(totalCost,'.2f'),sep='')