print ("Motorist's Trip Details")
print ("=" * 25)

# Initialize user choice to y if user wants to add more trips
moreTrips = 'y'

trips = []

# Text file is opened and program to write in it
motoristFile = open('motorist.txt', 'w')

# While loop which breaks only if user enters no
while moreTrips != 'n':

    print ("\nEnter the following information")

    # Prompts user to enter starting city
    startCity = str(input("Starting City: "))
    
    # Prompts user to enter ending city
    endCity = str(input("Ending City: "))

    # Prompts user to enter distance traveled
    distance = float(input("Distance: "))

    # Prompts user to enter gallons used
    gallons = float(input("Gallons: "))

    print (startCity,endCity,distance,gallons, sep=',')

    trips.append((startCity,endCity,distance,gallons))

    # Writes whatever user has input into text file
    for trip in trips:
        (f"{trip[0]},{trip[1]},{trip[2]}\n")


    # Asks user if they want to add another trip
    print ("Do you want to add another trip?")
    moreTrips = input("Input 'y' for yes and 'n' for no: " )

motoristFile.close()