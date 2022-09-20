# Filename: geometrycalculator.py
# Author: Gabriel Malabanan
# Date: September 19, 2022
# Program Description: Given imformation about a circle, rectangle and a triangle, calculate the area of the shape
#                      from the information given. Write a program that asks the user to input required information
#                      for a shape then calculates the area of the shape.

# Input: Option (1-4), radius, length, width, base, height
#
# Process: 1. Prompt user for option 1-4
#          2. If number <1 or >4 was chosen, display invalid output
#          2. If option 1 was chosen, prompt user for radius, then calculate area of circle.
#          3. If option 2 was chosen, prompt user for length and width, then calculate area of rectangle.
#          4. If option 3 was chosen, prompt user for base and height, then calculate area of triangle.
#
# Output:  1. If option 1 was chosen, display area of circle
#          2. If option 2 was chosen, display area of rectangle
#          3. If option 3 was chosen, display area of triangle
#          4. If option 4 was chosen, display ending message
#

from math import pi

# Intro and shows user the options
print ("Geometry Calculator\n")
print ("1. Calculate Area of a Circle\n")
print ("2. Calculate the Area of a Rectangle\n")
print ("3. Calculate the Area of a Triangle\n")
print ("4. Quit\n")

# Asks the user for choice (1-4)
choice = int(input('Enter your choice (1-4): '))

# Process
if choice == 1:
    # Asks user to input radius
    radius = float(input('Enter the radius of the circle: '))
    if radius < 0:
        print ("Invalid Output")
    else:
    # Outputs the area of circle
        print ("The area of the circle is: ",round(pi*radius*radius,2))


# Option 2
elif choice == 2:
    # Asks user to input length and width
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    if length < 0 or width < 0:
        print("Invalid Output")
    else:
    #Outputs the area of the rectangle
        print ("The area of the rectangle is: ",round(length*width,2))

#Option 3
elif choice == 3:
    # Asks the user to input base and height
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    if base < 0 or height < 0:
        print ("Invalid Output")
    else:
        # Outputs the area of the triangle
        print ("The area of the triangle is: ",round((base*height)/2,2))

# Option 4      
elif choice == 4:
    print("Have a nice day!")

# Output if number outside 1-4 was chosen
else:
    print("Invalid Output")

