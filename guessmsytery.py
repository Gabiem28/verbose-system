import random

# Intro
print("Guess the Mystery number ... \n")


# First function guess
def getGuess(first, last):

    # Infinite loop that validates the user's input 
    while True:
        print("Enter your guess (",first,"-",last,"): ", end="")

        # Asks for user's input
        guess = int(input())

        # Loop breaks if the guessed number is within 1-100
        if first <= guess <= last:
            break

        # Else statement keeps loop going until its broken
        else:
            print("Error ... Incorrect number. Try again")
            continue

    return guess


def guessWin(number, guess):

    # If user input was less then random generated number, print "is too high"
    if number < guess:
        print(" --->  ", guess, "is too High ...\n")
        return False

    # If user input was greater than random generated number, print "is too low"
    elif number > guess:
        print(" --->  ", guess, "is too Low ...\n")
        return False

    # If user input was the same as random generated number
    elif guess == number:
        print("\nCongratulations ... You guessed the Mistery Number!")
        return True


if __name__ == '__main__':

    # Intro
    print("Guess the Mystery number ... \n")

    # Some variables defined
    round = 1
    choice = 'y'
    first = 1
    last = 100

    # While loop which executes until user inputs "n"
    while choice != 'n':

        # Random number from import random  
        randomNum = random.randint(first, last) 

        # Loops for 7 rounds
        for round in range(7): 
            print("Round", round + 1, "of 7")
            print("--------------------------------")


            # Calls function getGuess to validate user input
            guess = getGuess(first, last) 

            # Calls function guessWin to check if value is within range (1-100)
            result = guessWin(randomNum, guess)  

            # Loop breaks if user guess is the same as random number
            if result == True:
                break

        # Asks if user would like to try again
        print("Would you like to try again (y/n)? ", end="")  
        choice = input() 

        