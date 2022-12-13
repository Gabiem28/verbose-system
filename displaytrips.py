# File Name: motoristtrip.py
# Author: Gabriel Malabanan
# Date: December 13, 2022
# Program Description: Write a program that read the file created by the first program and display the starting and ending cities,
# distance and gallons
# Input: Starting city, Ending City, Distance, Gallons
#
# Processing: 1. Open text file and read its contents
#             2. Print all of text that user has inputted from previous program
#
# Output: User input of Starting city, Ending City, Distance, Gallons
#




print ("Motorist's Trip Details")
print ("=" * 25)



print("Starting City\t" + "Ending City\t" + " Distance   " + "Gallons\t")
print ("=" * 13 + "\t" + "=" * 14 + "\t" + "=" * 9 + "   " + "=" * 8) 

motoristFile = open ('motorist.txt', 'r')



startCity = (motoristFile.readline())
endCity = (motoristFile.readline())
distance = (motoristFile.readline())
gallons = (motoristFile.readline())


print(startCity + "\t" + endCity + "\t" + distance  + "\t" + gallons)



motoristFile.close()






