import random

#list of possible fruits, rooms and containers
fruit = ["apple", "banana", "watermelon", "lemon", "strawberry"]
room = ["bedroom", "living room", "classroom", "storage room", "garage"]
containers = ["box", "bag", "carton", "suitcase", "purse"]

#asks for name
name = input("Whats your name_")

#asks table wants to study
table = int(input("What times table do you want to study?"))

#var for score and first
score =0
first =0

#chekcs if answer is correct
def checkAnswer(input, num, tab):
    if input == num*tab:
        return True
    else:
        return False


def question(table):
    points = 0
    fruitx = random.choice(fruit)
    roomx = random.choice(room)
    number = random.randint(2,12)

    containersx = random.choice(containers)
    print(f"In the {roomx}, you see {table} {containersx}s containing {number} {fruitx}s \n How many {fruitx}s are there in the {roomx} in total?")
    response = int(input("Answer_ "))


    if checkAnswer(response, number, table):
        print("That's correct!")
        points += 2
        #if checkAnswer returns true, points += 2; prints That's correct
    else:
        #if checkAnswer returns false, tells user to try again, 
        print("Try again")
        #repeats, but if correct this time only add 1
        response = int(input("Answer_ "))
        if checkAnswer(response, number, table):
            print("That's correct!")
            points += 1
        else:
            print(f"No, the correct answer is {number*table}")
    
    return points

#repeats execution of question class 5 times
for i in range(5):
    points = question(table)
    #score << points
    score += points
    if points == 2:
        first += 1


#returns feedback
def feedback():
    #prints user name, score, and amt of questions right on first attempt
    print(f"Hey {name}, you got {score} points and got {first} question(s) right on the first attempt!")
    if score >= 8:
        print(f"Congrats you know your {table} times table!")
    elif score >= 5:
        print(f"Good effort! you know parts of your {table} times table")
    else:
        print(f"You need to practice mroe of your {table} times table")

#executes feedback
feedback()