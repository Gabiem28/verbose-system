




def menu_Options():
    menuChoice = 0
    SEE_RULES = 1
    PLAY_GAME = 2
    SEE_HISTORY = 3
    QUIT_GAME = 4

    while menuChoice != QUIT_GAME:
        print ("Choose from the following options:")
        print ("1. See Rules of the game")
        print ("2. Play Vingt-et-un")
        print ("3. See history")
        print ("4. Quit game")

        menuChoice = int(input("Option: "))

        if menuChoice == SEE_RULES:
            print ("The rules are.....")
            break
        elif menuChoice == PLAY_GAME:
            print ("You are now playing the game.....")
            break
        elif menuChoice == SEE_HISTORY:
            print ("The history is....")
            break
        elif QUIT_GAME:
            print("Thanks for playing!!!")
            break
        else:
            print ("Error. Choose from the options above")    

menu_Options()
