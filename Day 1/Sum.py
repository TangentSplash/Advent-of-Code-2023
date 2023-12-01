import math
INPUT='Day 1/input.txt'
Fileinput= open(INPUT,"r")
Input=Fileinput.readlines()

sum = 0
for line in Input:
    FoundStart= False
    FoundEnd = False
    for i in range(0,len(line)):
        if (line[i].isdigit()):
            a=int(line[i])
            FoundStart=True
            break
    for j in range(len(line)-1,-1,-1):
        if (line[j].isdigit()):
            b=int(line[j])
            FoundEnd=True
            break
    if(not(FoundStart and FoundEnd)):
        print("Values not found in ", line)
    sum += (a*10)+b
print("The sum is ", sum)
