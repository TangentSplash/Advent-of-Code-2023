class Game():
    def __init__(self,number):
        self.number=int(number.split("Game ")[1])
        self.grabbed={
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }
        
    def lessThan(self,default):
        sR = self.grabbed["red"]
        dR = default.grabbed["red"]
        sG = self.grabbed["green"]
        dG = default.grabbed["green"]
        sB = self.grabbed["blue"]
        dB = default.grabbed["blue"]
        return (sR<=dR and sG<=dG and sB<=dB)
    
    def pulled(self,colour,number):
        if (self.grabbed[colour]<number):
            self.grabbed[colour]=number
        
        
DIGIT="\d+"
import re

def readInput(line):
    line=re.sub("\n","",line)
    lines=line.split(':')
    number=lines[0]
    game = Game(number)
    lines=lines[1].split(';')
    for draw in lines:
        pulled=draw.split(',')
        for cube in pulled:
            amount = re.search("\d+ ",cube)
            colour = cube[amount.end():]
            amount = int(amount.group())
            game.pulled(colour,amount)
    return game

INPUT='Day 2/input.txt'
Fileinput= open(INPUT,"r")
Input=Fileinput.readlines()

defaultGame = Game("Game 0")
defaultGame.grabbed["red"] = 12
defaultGame.grabbed["green"] = 13
defaultGame.grabbed["blue"] = 14

gameIDs = 0
for line in Input:
    game = readInput(line)
    if(game.lessThan(defaultGame)):
        gameIDs += game.number
        
print("Sum of IDs: ",gameIDs)
  
# Tried values      
# 2137 - Too low