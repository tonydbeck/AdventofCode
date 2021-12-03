counter = 0
a = 0
b = 0
triple = 0
noOfIncrease = 0
noOfDecrease = 0
noOfNoChange = 0
counter = 0

f = open("input.log", "r")
ar = f.readlines()
#print (ar[0])

for x in ar:
    if counter > 1:
        triple = (int(ar[counter-2]) + int(ar[counter-1]) + int(ar[counter]))
        #print(str(triple))
        b = a
        a = triple
    if counter > 2:
        
        if a > b:
            noOfIncrease = noOfIncrease + 1
            print(str(triple) + " (increased)  Increases: " + str(noOfIncrease))
        elif a == b:
            noOfNoChange = noOfNoChange + 1
            print(str(triple) + " (no change)  No Changes: " + str(noOfNoChange))
        else:
            noOfDecrease = noOfDecrease + 1
            print(str(triple) + " (decreased)  Decreases: " + str(noOfDecrease))
    elif counter > 1:
        print(str(triple) + "(N/A - no previous measurement)")
    counter = counter + 1
    
