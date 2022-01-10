import tkinter
from tkinter import ttk, IntVar, StringVar, messagebox
from tkinter.constants import OUTSIDE
import random

mainWindow = tkinter.Tk()
mainWindow.configure(pady=30, padx=50)

characters = {
    "hero":{
        "maxHealth": 15
    }
}
health = 0
damageMultiplier = 1

content = [[],[]]

# todo: remake room system from original file to be more dynamic and easier to work with,
# expand on options menu with current region, cheatcodes and some other stuff,
# create a better characters array

# This is to help visualize what the new room system might look like
rooms = {
    "hero":{
        "village":{
            0: {"content": [],
                "go to": [["forest", 0, "forest"]]},
            1: {"content": []}
        },

        "forest":{
            0: []
        }
    },



    "villain":{
        "overlord's castle":{
            0: []
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
    functionToUse = []

    theContentDestroyer9000()

    for info in newContent:

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
                playerAnswer = StringVar()
                content[0].append(ttk.Radiobutton(
                    text=value,
                    variable=value
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

def funcExecute(functionToUse):
    functionList[functionToUse]()

def options():
    theContentDestroyer9000(True)
    contentCreator([["button", ["Region", "Cheatcodes", "Exit"]]])

def exit():
    contentCreator([["button", ["Options"]]])

functionList = {
    "Options": options,
    "Exit": exit
}

#----------------------------------------------------------------------------------Room gen functions

def nextRoom():
    pass

def roomGen():
    pass

def chooseCharacter():
    contentCreator([["label", ["Choose a character"]], ["radio", list(characters.keys())]])

#----------------------------------------------------------------------------------Start

contentCreator([["button", ["Options"]]])
chooseCharacter()
            

mainWindow.mainloop()