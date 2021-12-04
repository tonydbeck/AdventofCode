#----------------------------------------------------#
#         Day 3 Part 1 Advent of Code!  T.Beck       #
#----------------------------------------------------#


#Going to comment this one properly!

#https://adventofcode.com/2021/day/3

#Will use bitiwse operators/ bit masking to isolate individual bit locations
#each line is 12 bits, so will use the following bit masks (will us :

#Constants:
BM1 = 1     #bit 1
BM2 = 2     #bit 2
BM3 = 4     #bit 3
BM4 = 8     #bit 4
BM5 = 16    #bit 5
BM6 = 32    #bit 6
BM7 = 64    #bit 7
BM8 = 128   #bit 8
BM9 = 256   #bit 9
BM10 = 512   #bit 10
BM11 = 1024  #bit 11
BM12 = 2048  #bit 12

#Variables:

#these variables hold the total number of 1's in the corresponding bit position
bit1Count = 0
bit2Count = 0
bit3Count = 0
bit4Count = 0
bit5Count = 0
bit6Count = 0
bit7Count = 0
bit8Count = 0
bit9Count = 0
bit10Count = 0
bit11Count = 0
bit12Count = 0

#to hold the final result
result = 0

f = open("day3.txt", "r")  #Open input file
ar = f.readlines()         #Create arrary (ar) with each element as a line of the input file
lineCount = len(ar)        #Count the total number of values, this is useful as can be used later on to calculate if the total 1's for a bit position is great than half the total values or not 

for x in ar:        #iterate through list of values
    #Formula to give a 1 if there is a bit present at a certain location.
    #Step1: Convert string binary value to integer
    #step2: AND the bits with the bitmask for the relevant bit; bit masks defined above..... BM1, BM2 etc.   BM5=16=10000.  Eg.  10110 & 10000 = 10000,   01010 & 10000 = 00000
    #Step3: For all bit locations other than 1, shift the bits right by the number of bits equivalent to its location.  This ensures result is either 0 or 1 in decimal rather than say 1000 which would be 8 in dec.
    #Step4: Add the reult (either 1 or 0) to the bit total counter
    
    bit1Count += (int(x,2) & BM1)
    bit2Count += ((int(x,2) & BM2) >> 1)
    bit3Count += ((int(x,2) & BM3) >> 2)
    bit4Count += ((int(x,2) & BM4) >> 3)
    bit5Count += ((int(x,2) & BM5) >> 4)
    bit6Count += ((int(x,2) & BM6) >> 5)
    bit7Count += ((int(x,2) & BM7) >> 6)
    bit8Count += ((int(x,2) & BM8) >> 7)
    bit9Count += ((int(x,2) & BM9) >> 8)
    bit10Count += ((int(x,2) & BM10) >> 9)
    bit11Count += ((int(x,2) & BM11) >> 10)
    bit12Count += ((int(x,2) & BM12) >> 11)

#purely for testing:    
print (str(bit12Count) + " " + str(bit11Count) + " " + str(bit10Count) + " " + str(bit9Count) + " " + str(bit8Count) + " " + str(bit7Count) + " " + str(bit6Count) + " " + str(bit5Count) + " " + str(bit4Count) +" " + str(bit3Count) + " " + str(bit2Count) + " " + str(bit1Count))

#Calculate the total as a product of if there are more 1's than 0's for that bit position.  As the result is a binary number, the value for each bit location needs to be added to the result
if bit1Count > lineCount/2: result += 1
if bit2Count > lineCount/2: result += 2 
if bit3Count > lineCount/2: result += 4
if bit4Count > lineCount/2: result += 8
if bit5Count > lineCount/2: result += 16
if bit6Count > lineCount/2: result += 32
if bit7Count > lineCount/2: result += 64
if bit8Count > lineCount/2: result += 128
if bit9Count > lineCount/2: result += 256
if bit10Count > lineCount/2: result += 512
if bit11Count > lineCount/2: result += 1024
if bit12Count > lineCount/2: result += 2048

#print statement for testing
print(str(lineCount) + " " + str(result) +" " + str(~result & 0xFFF))

#The actual result is the value * the value with bits inverted
#the ~ operator inverts bits, but as Python uses 32bit ints, all of the bits from bit 13 to 32 also get inverted and changed to 1's which gives an incorrect result.
#to Overcome this, AND the inverted result with a bit mask where only the first 12 bits are set ie. FFF (hex) or 111111111111
print(str(result * (~result & 0xFFF)))
    
