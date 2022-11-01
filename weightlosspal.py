# Programn name: weightlosspal.py
# Author: Gabriel Malabanan
# Date: October 31, 2022
# Program Description: Write a menu-driven interface program with the following options:
#                      1. Display "10 ways to cut 500 calories" guideline
#                      2. Generate next semester expected weight table.
#                      3. Quit
#                      if user chooses 1, guidelines will be displayed. If user chooses 2, program prompts
#                      for starting weight and generate a table showing what their expected weight at the 
#                      of each month should be for the next 6 months. If 3 was chosen, then the program ends.
#
# Input: Menu option 1,2 and 3. Starting weight if menu option 3 was chosen
#
# Processing: 1. Display Menu options 1,2 and 3
#             2. If option 1 was chosen by user, guidelines will be displayed
#             3. If option 2 was chosen by user, program prompts starting weight
#             4. Program generates a table showing what weight should user be at the
#                end of each month for the next 6 months
#             5. If option 3 was chosen by user, the program ends
#
# Output: Menu options, "10 ways to cut 500 calories" guidelines, or generated table of user's expected weight



# Intro
print ("500 Less a Day Makes the Weight Go Away...")
print("*" * 45)


# Variables declared and constants initialized
menuChoice = 0
CHOICE_1 = 1
CHOICE_2 = 2
QUIT_CHOICE = 3
startingWeight = 0


# while loop that executes until user chooses 3
while menuChoice != QUIT_CHOICE:
    # Display menu options
    print ("Choose one of the following options:")
    print ("\t 1. Display \"10 ways to cut 500 calories\" guideline")
    print ("\t 2. Generate next semester expected weight table")
    print ("\t 3. Quit")

    # Asks for users menu option choice
    menuChoice = int(input('Option:'))


    # If user chooses option 1
    if menuChoice == 1:
        print("\nTry these 10 ways to cut 500 calories every day.")
        print("\t* Swap your snack.")
        print("\t* Cut one high-calorie treat.")
        print("\t* DO NOT drink your calories.")
        print("\t* Make low calorie substitutions.")
        print("\t* Ask for a doggie bag")
        print("\t* Just say \"no\" to fried food.")
        print("\t* Build a thinner pizza.")
        print("\t* Use a smaller plate.")
        print("\t* Avoid alcohol.")
        print("Source: US National Library of Medicine")
    

    # If user chooses option 2
    elif menuChoice == 2:
        startingWeight = int(input('Please enter starting weight in lbs (>=100):'))


        # Input validation if weight is less than 100
        while startingWeight < 100:
            print ("Error ... Invalid weight. Try Again")
            startingWeight = int(input('Please enter starting weight in lbs (>=100):'))


        # Heading for expected weight table        
        print ("-" * 17)
        print ("Month \t Weight")
        print ("-" * 17)


        # for loop for 6 months weight table
        for i in range (1, 7):
            startingWeight = startingWeight - 4
            print(str(i) + "\t" + str(startingWeight) + " lbs")

    # If user chooses option 3, loop stops    
    elif menuChoice == 3:
        break
    
    # Input validation for numbers different from 1,2 and 3 for user's menu choice
    else:
        print("Error ... Invalid option. Try Again")


# Displayed if user chooses option 3
print ("\nGood Bye ...")

    

    

