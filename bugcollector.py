print ("Bug Collector")

numOfBugs = 0
NUM_OF_DAYS = 5




for days in range(NUM_OF_DAYS):
    print ("How many bugs did you collect for day",(days+1),":", end=" ")
    numOfBugs = int(input())

    while numOfBugs < 1:
        print ("Invalid. Number of bugs cannot be less than 0.")
        numOfBugs = int(input('How many bugs did you collect for day'),(days+1))

    
