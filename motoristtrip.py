# File Name: motoristtrip.py
# Author: Gabriel Malabanan
# Date: December 13, 2022
# Program Description: Write a program that will ask motorist (user) for his trip details and store it. The program should prompt the user
# for the the city where he started, the city in which he stopped at,  the distance in which he traveled and the gallons used from the trip. Motorist should be able to input
# an unlimited number of trips
#
# Input: Starting city, Ending City, Distance, Gallons
#
# Processing: 1. Execute while loop which allows user to input an unlimited number of trips
#             2. Open or create text file which will store all the user input of 
#             3. Prompt user for the starting city, ending city, distance traveled and gallons used.
#             4. Ask user if they want to input more trips. If yes program will loop back. If no, program breaks
#             5. Once loop breaks, information will be stored on the text file.
#             6. Display all the trips details that the user has inputted
#
# Output: User input of Starting city, Ending City, Distance, Gallons
#


# Intro to the program
print ("Motorist's Trip Details")
print ("=" * 25)

# Initialize user choice to y if user wants to add more trips
moreTrips = 'y'

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

    # Writes whatever user has input into text file
    motoristFile.write(startCity + '\n')
    motoristFile.write(endCity + '\n')
    motoristFile.write(str(distance) + '\n')
    motoristFile.write(str(gallons) + '\n')


    # Asks user if they want to add another trip
    print ("Do you want to add another trip?")
    moreTrips = input("Input 'y' for yes and 'n' for no: " )

motoristFile.close()
