print ("Bug Collector")

numOfBugs = 0
DAYS = 5



while numOfBugs < 1:
    print ("Invalid. Number of bugs cannot be less than 0.")
    numOfBugs = int(input('How many bugs did you collect today?: '))

    for days in range(DAYS):
        print ("How many bugs did you collect for day",(days+1))
        numOfBugs = int(input())

    
