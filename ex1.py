counter = 0
a = 0
b = 0
f = open("input.log", "r")
noOfIncrease = 0
noOfDecrease = 0
for x in f:
    
    if counter > 0:
        b = a       
        a = int(x)
        if a > b:
            noOfIncrease = noOfIncrease + 1
            print(str(a) + " (increased)  Increases: " + str(noOfIncrease))
            
        else:
            noOfDecrease = noOfDecrease + 1
            print(str(a) + " (decreased)  Decreases: " + str(noOfDecrease))
            
    else:
        print(str(int(x)) + "(N/A - no previous measurement)")
    counter = counter + 1
    
