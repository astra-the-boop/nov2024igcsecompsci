import math
import random
#define values
grid = [[]]
data = {"difficulty":0,
        "Xlocation":0,
        "Ylocation":0,
        "GoalX":0,
        "GoalY":0,
        "NoMovesLeft": 0
        }
GoalIndicator = "X"


#asks for difficulty
data["difficulty"] = int(input("Difficulty (enter an integer)_"))
#asks whether or not player wants goal hidden
GoalHidden = input("Do you want the goal to be hidden? [y/n]_ ")
#changes goalindicator based on whether or not user wants goal hidden:
if GoalHidden.lower() == "y":
    GoalIndicator = "0"
elif GoalHidden.lower() =="n":
    GoalIndicator = "X"

#initiates game, sets values, draws grid, etc...
def initiate():
    data["NoMovesLeft"]=data["difficulty"]*2

    myGrid = [["0" for i in range(data["difficulty"])] for j in range(data['difficulty'])]

    #creates goal
    data["GoalX"] = random.randint(0,data["difficulty"] - 1)
    data["GoalY"] = random.randint(0,data["difficulty"] - 1)
    #checks if goal is on player spawn location
    while data["GoalX"] == data["GoalY"] == 0:
        data["GoalX"] = random.randint(0,data["difficulty"] - 1)
        data["GoalY"] = random.randint(0,data["difficulty"] - 1)
    
    
    
    return myGrid

#prints grid
def printGrid():
    # for i in range(data["difficulty"]):
    #     print(grid[i])
    print("\n" * 3)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            #MARKS PLAYER
            if (x == data['Xlocation'] and y == data['Ylocation']):
                print("+", end = " ")
            #MARKS GOAL
            elif (x == data['GoalX'] and y == data['GoalY']):
                print(GoalIndicator, end = " ")
            else: print(grid[x][y], end = " ")
        print()
    

#player movement
def playerMovement():
    if userinput.lower() == "w" and data["Ylocation"] > 0:
        grid[data["Xlocation"]][data["Ylocation"]] = "0"
        data["Xlocation"] -= 1
    elif userinput.lower() == "s" and data["Ylocation"] < data["difficulty"]-1:
        grid[data["Xlocation"]][data["Ylocation"]] = "0"
        data["Xlocation"] += 1
    elif userinput.lower() == "d" and data["Xlocation"] < data["difficulty"]-1:
        grid[data["Xlocation"]][data["Ylocation"]] = "0"
        data["Ylocation"] += 1
    elif userinput.lower() == "a" and data["Xlocation"] > 0:
        grid[data["Xlocation"]][data["Ylocation"]] = "0"
        data["Ylocation"] -= 1
    elif userinput.lower() == "hint":
        #calculates distance (Pythagorean theorum)
        print(
            f'''You are {
                math.sqrt(
                    abs(
                        data["Xlocation"]-data["GoalX"]
                    )**2) + abs(
                        data["Ylocation"]-data["GoalY"]
                    )**2
                } meters from the goal'''
            )
        data["NoMovesLeft"] += 1
    else:
        data["NoMovesLeft"] += 1

def checkReachedGoal():
    #if char is at goal location, returns true
    if data["Xlocation"] == data["GoalX"] and data["Ylocation"] == data["GoalY"]:
        return True
    #if not within NoMovesLeft moves, returns false
    elif data["NoMovesLeft"] == 0:
        return False


grid = initiate()


while True:
    
    printGrid()

    #input
    userinput = input("input (Enter 'hint' for a hint)_ ")
    #updates amount of moves left
    data["NoMovesLeft"] -= 1
    playerMovement()
    
    
    if checkReachedGoal() == True:
        print("CONGRATS YOU WON!")
        break
    elif checkReachedGoal() == False:
        print("GAME OVER!")
        break
    else:
        pass
