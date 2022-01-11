import tkinter
from tkinter import ttk, IntVar, StringVar, messagebox
from tkinter.constants import OUTSIDE
import random

mainWindow = tkinter.Tk()
mainWindow.configure(pady=30, padx=50)

characters = {
    "hero":{
        "maxHealth": 15
    },

    "villain":{
        "maxHealth": 30
    }
}
health = 0
damageMultiplier = 1

content = [[],[]]

# todo: remake room system from original file to be more dynamic and easier to work with,
# expand on options menu with current region, cheatcodes and some other stuff,
# make health system,
# reintroduce question generator,
# make battle system,
# support for items (maybe)

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

    if playerAnswer.get() == None:
        messagebox.showerror(message="Please select a character!")
        return

    for character in list(characters.keys()):
        if character == playerAnswer.get(): 
            health = characters[character]["maxHealth"]
            currentCharacter = character
            currentRegion = [list(rooms[character].keys())[0], 0]
            contentCreator([["button", ["Options"]]])
            contentCreator(rooms[character][list(rooms[character].keys())[0]][0]["content"])
            break

#----------------------------------------------------------------------------------Room gen functions

def nextRoom():
    global currentRegion
    goto = False

    if rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["go to"]:
        for currentGoTo in rooms[currentCharacter][currentRegion[0]][currentRegion[1]]["go to"]:
            if currentGoTo[2] == playerAnswer.get():
                currentRegion = [currentGoTo[0], currentGoTo[1]]
                goto = True
                break
    if goto == False:
        currentRegion[1] += 1

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
    "Submit": nextRoom
}

mainWindow.mainloop()