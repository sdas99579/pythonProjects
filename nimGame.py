from random import randrange
numStones = int(input("How many number of stones you want to take for play NIM: "))
def playerTurn():
    global numStones
    howMany = int(input("Do you want 1,2 or 3 stone?"))
    while(howMany<1 or howMany>3 or howMany>numStones):
        howMany = int(input("Enter a legal input: "))
    numStones = numStones - howMany
    print(f"Stone remaining: {numStones}\n")
    if(numStones==0):
        print("You : +1")
        print("Computer : -1")
def computerTurn():
    global numStones
    max=0
    #if(numStones<4):
    #    max = numStones
    #else:
    max = numStones % 4
    if(max==0):
        compStone = randrange(1,max+2)
    elif(max!=0):
        compStone = numStones%4
    numStones = numStones - compStone
    print(f"Computer picked up {compStone} stones")
    print(f"Stones remaining {numStones}\n")
    if(numStones==0):
        print("Computer : +1")
        print("You: -1")

def playNim():
    print("Let's play Nim!!!")
    while(numStones>0):
        playerTurn()
        if(numStones>0):
            computerTurn()

playNim()