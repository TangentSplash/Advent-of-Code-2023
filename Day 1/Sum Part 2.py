import math
import re
INPUT='Day 1/input.txt'
Fileinput= open(INPUT,"r")
Input=Fileinput.readlines()
NUMBERSTRINGS = "one|two|three|four|five|six|seven|eight|nine" # Regex to find the numbers

numberDict = {  # Dictionary to convert to integer
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9 
}

def findNumber(i):
    if (line[i].isdigit()):
            return int(line[i])
    return -1
                

sum = 0
for line in Input:
    i=0
    FoundStart=False
    FoundEnd=False
    nums=[]
    while i <len(line):
        num=re.search(NUMBERSTRINGS,line[i:])
        if (num!=None):
            last=num.end()+i
            nums.append(num)
            i+=num.start()+1
        else:
            break
    if(nums):
        first=nums[0].start()
    else:
        first=len(line)
        last=0
    
    for i in range(0,first):
        a=findNumber(i)
        if (a!=-1):
            FoundStart=True
            break
    for j in range(len(line)-1,last-1,-1):
        b=findNumber(j)
        if(b!=-1):
            FoundEnd=True
            break
        
    if(not nums and not FoundStart and not FoundEnd):
        print("Values not found in ", line)
        
    if(not FoundStart):
        a=numberDict[nums[0].group()]
    if (not FoundEnd):
        b=numberDict[nums[-1].group()]
    if(len(nums)<=1 or a==b):
        print(line[:-1],a,b)
    sum += (a*10)+b
print("The sum is ", sum)