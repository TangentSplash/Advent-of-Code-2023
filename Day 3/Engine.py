import re
INPUT ='Day 3/input.txt'
BLANK='.'

def FindNeighbour(match,line,startpos):
    start = match.start()+startpos
    end = match.end()+startpos-1
    for j in range(line-1,line+2):
        if(j>=0 and j<len(Input)):
            for i in range(start-1,end+2):
                if (i>=0 and i<len(Input[0]) and not(j==line and i>=start and i<=end) and Schematic[j][i]!=BLANK and Schematic[j][i]!='\n'):
                    return True
    return False
                    
    


Fileinput = open(INPUT,"r")
Input = Fileinput.readlines()
Schematic = []
for line in Input:
    Schematic.append(list(line))

sum = 0
for j in range(0,len(Schematic)):
    array = Schematic[j]
    string = Input[j]
    i=0
    length=len(line)
    while i < length:
        num = re.search("\d+",string[i:])
        if (num!=None):
            neighbour = FindNeighbour(num,j,i)
            sum += neighbour*(int(num.group()))
            i+=num.end()+1
        else:
            break
print("The sum of part numbers is: ",sum)