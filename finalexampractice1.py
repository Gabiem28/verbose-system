# File Name: 
# Author: 
# Date: 
# Program Description
#
# Input:
#
# Processing:
#
# Output: 
#

print ("Purchases Items Input")
print ("=" * 21)

NEWLINE = "\n"
itemNumber = 0

fileObject = open ("items.txt","w")
i = 0

while True:
    



    
    for i in range (1,i + 1):
        print ("Item ",i)
        itemName = str(input("Enter item name:"))
        itemCount = float(input("Enter " + itemCount + " quantity:"))
        itemPrice = float(input("Enter " + itemPrice + " price: "))

        print (itemName,itemCount,itemPrice)


        fileObject.write(str(itemName))
        fileObject.write(NEWLINE)
        fileObject.write(str(itemCount))
        fileObject.write(NEWLINE)
        fileObject.write(str(itemNumber))
        fileObject.write(NEWLINE)


        addMoreItems = input ("More items? (y,n)?")
        if addMoreItems.lower() == "y":
            continue
        # Can also item name,quantity and price here so item number would not increase when user has invalid choice
        elif addMoreItems.lower() == "n":
            break
        else:
            print ("Invalid Choice")

    fileObject.close()
    


