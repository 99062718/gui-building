import tkinter
from tkinter import ttk, IntVar, StringVar, messagebox
from tkinter.constants import OUTSIDE
import random

mainWindow = tkinter.Tk()
mainWindow.configure(pady=30, padx=50)

characters = { # list of characters and stats
    "hero":{
        "maxHealth": 15
    },

    "villain":{
        "maxHealth": 30
    }
}

difficulties = { #list of difficulties. array includes: numberOfOperators, additionSubtractionNumber, multiplicationNumber, damage enemies will deal
    "easy": [4, 100, 20, 3],
    "medium": [4, 1000, 100, 5],
    "hard": [5, 5000, 500, "max"]
}
damageMultiplier = 1

content = [[],[]]

# todo: remake room system from original file to be more dynamic and easier to work with,
# expand on options menu with current region, cheatcodes and some other stuff (font size and font customization if able to),
# allow for battles that continue until the health bar reaches 0,
# support for items (maybe),
# implement "optional":{"boss": [region to go to once boss health is 0, room to go to once boss health is 0, boss health]}}

# This is to help visualize what the new room system might look like
rooms = {
    "hero":{
        "village":{
            0: {"content": [["label", ["Where would you like to go?"]], ["radio", ["forest", "stay"]], ["button", ["Submit"]]],
                "go to": [["forest", 0, "forest"], ["village", 0, "stay"]]},
            1: {"content": []}
        },

        "forest":{
            0: {"content": []}
        }
    },



    "villain":{
        "overlord's castle":{
            0: {"content": []}
        }
    }
}

#----------------------------------------------------------------------------------Content functions

def theContentDestroyer9000(removeAll=False): # theContentDestroyer9000 is back in stock yet again. Now for 30% off for you and your family to destroy content with during the holidays!
    global content
    for box in content[0]:
        box.destroy()
    content[0] = []
    if removeAll:
        for box in content[1]:
            box.destroy()
        content[1] = []

def contentCreator(newContent=[]): # the only reason theContentDestroyer9000 still sells
    global content, playerAnswer
    num = [0, 0]

    theContentDestroyer9000()

    for info in newContent:

        if info[0] in ("radio", "spinbox"):
            playerAnswer = StringVar() if info[0] == "radio" else IntVar()

        for value in info[1]:

            gridOrPlace = "place" if value == "Options" else "grid"
            value = mathQuestionCreator() if value == "mathQuestion" else value

            if info[0] == "label": # creates label
                content[0].append(tkinter.Label(text=value))
            elif info[0] == "spinbox": # creates spinbox
                playerAnswer = IntVar()
                content[0].append(ttk.Spinbox(
                    from_=float("-inf"),
                    to=float("inf"),
                    value=playerAnswer
                ))
            elif info[0] == "radio": # creates radiobutton
                content[0].append(ttk.Radiobutton(
                    text=value,
                    value=value,
                    variable=playerAnswer
                ))
            elif info[0] == "button": # creates button
                functionToUse = value

                content[1 if gridOrPlace == "place" else 0].append(tkinter.Button(
                    text=value,
                    command = lambda toUse = functionToUse : funcExecute(toUse)
                ))
            else: # throws exception if given widget type is not supported by the program
                raise Exception("{} is not a valid widget type".format(info[0]))

            if gridOrPlace == "place":
                content[1][num[1]].place(bordermode=OUTSIDE, anchor="nw")
                num[1] += 1
            else:
                content[0][num[0]].grid(row=num[0])
                num[0] += 1

def mathQuestionCreator(): #makes math questions by choosing an operator based on a random number
    global isAlternate, currentAnswer, higherOrLower, isMath
    randomNumber = random.randint(1, numberOfOperators)
    isAlternate = True
    isMath = True

    if randomNumber is not(3 or 4):
        isAlternate = False
    
    if randomNumber == 1 or randomNumber == 2:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        randomNumber3 = random.randint(1, additionSubtractionNumber)
        currentAnswer = randomNumber2 + randomNumber3 if randomNumber == 1 else randomNumber2 - randomNumber3
        return "What is {} + {}?".format(randomNumber2, randomNumber3) if randomNumber == 1 else "What is {} - {}?".format(randomNumber2, randomNumber3)
    elif randomNumber == 3 or randomNumber == 4:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        currentAnswer = randomNumber2
        higherOrLower = "higher" if randomNumber == 3 else "lower"
        return "Name a number higher than {}".format(randomNumber2) if randomNumber == 3 else "Name a number lower than {}".format(randomNumber2)
    elif randomNumber == 5:
        randomNumber2 = random.randint(1, multiplicationNumber)
        randomNumber3 = random.randint(1, multiplicationNumber)
        currentAnswer = randomNumber2 * randomNumber3
        return "What is {} * {}?".format(randomNumber2, randomNumber3)

#----------------------------------------------------------------------------------Button functions

def funcExecute(functionToUse): #executes whatever function we put into it. useful for dynamically creating buttons
    functionList[functionToUse]()

class optionMenu: #everything related to the options menu
    def options():
        theContentDestroyer9000(True)
        contentCreator([["button", ["Region", "Cheatcodes", "Exit"]]])

    def showRegion():
        messagebox.showinfo(message="Your current region is: {}".format(currentRegion[0]))

    def exitMenu():
        contentCreator([["button", ["Options"]]])
        contentCreator(rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["content"])

def characterSubmit(): #sets all stats for character once chosen and sends them to first room of their respective story
    global currentCharacter, currentRegion, health
    currentCharacter = playerAnswer.get()

    if currentCharacter in list(characters.keys()):
        health = characters[currentCharacter]["maxHealth"]
        currentRegion = [list(rooms[currentCharacter].keys())[0], 0]

        contentCreator([["label", ["Select a difficulty"]], ["radio", list(difficulties.keys())], ["button", ["Choose difficulty"]]])
    else:
        messagebox.showerror(message="Please select a character!")

def diffSubmit():
    global numberOfOperators, additionSubtractionNumber, multiplicationNumber, damageToPlayer, currentDiff
    currentDiff = playerAnswer.get()

    if currentDiff in list(difficulties.keys()):
        numberOfOperators = difficulties[currentDiff][0]
        additionSubtractionNumber = difficulties[currentDiff][1]
        multiplicationNumber = difficulties[currentDiff][2]
        damageToPlayer = difficulties[currentDiff][3] if difficulties[currentDiff][3] != "max" else health

        contentCreator([["button", ["Options"]]])
        contentCreator(rooms[currentCharacter][list(rooms[currentCharacter].keys())[0]][0]["content"])

def healthCheck(deathMessage=""): # if player get hit. player get hurt. if player doesnt have health left. player die
    global health

    health -= damageToPlayer

    if health <= 0:
        theContentDestroyer9000(True)
        contentCreator([["label", [deathMessage, "Game over!"]]])
        
#----------------------------------------------------------------------------------Room gen functions

def mathAnswerCheck(input):
    if isAlternate == False and currentAnswer == input:
        return True
    elif isAlternate == True:
        if input > currentAnswer and higherOrLower == "higher":
            return True
        elif input < currentAnswer and higherOrLower == "lower":
            return True
    return False

def nextRoom():
    global currentRegion, playerAnswer, isMath
    goto = False
    
    playerAnswer = mathAnswerCheck(playerAnswer.get()) if isMath else playerAnswer.get()

    if rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["optional"]:
        if rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["optional"]["battle"] == playerAnswer:
            healthCheck(rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["optional"]["death message"])

    if rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["go to"]:
        for currentGoTo in rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["go to"]:
            if playerAnswer in currentGoTo or len(currentGoTo) == 2:
                currentRegion = [currentGoTo[0], currentGoTo[1]]
                goto = True
                break
    if goto == False:
        currentRegion[1] += 1

    isMath = False
    roomGen()

def roomGen():
    contentCreator(rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["content"])

def chooseCharacter():
    contentCreator([["label", ["Choose a character"]], ["radio", list(characters.keys())], ["button", ["Choose character"]]])

#----------------------------------------------------------------------------------Start

chooseCharacter()
            
functionList = {
    "Options": optionMenu.options,
    "Region": optionMenu.showRegion,
    "Exit": optionMenu.exitMenu,
    "Choose character": characterSubmit,
    "Choose difficulty": diffSubmit,
    "Submit": nextRoom
}

mainWindow.mainloop()