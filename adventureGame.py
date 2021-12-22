import tkinter
from tkinter import ttk, IntVar, StringVar, messagebox
from tkinter.constants import ANCHOR, OUTSIDE
import random

mainWindow = tkinter.Tk()
mainWindow.configure(pady=20, padx=50)

characters = ["hero"]
maxHealth = 15
health = 15
damageMultiplier = 1

content = [[],[]]

# todo: Create a function that goes through a list of functions it can use (would be useful for buttons created with the contentCreator),
# remake room system from original file to be more dynamic and easier to work with,
# make options menu in gui

def theContentDestroyer9000(removeAll=False): # theContentDestroyer9000 is back in stock yet again. Now for 30% off for you and your family to destroy content with during the holidays!
    global content
    for box in content[0]:
        box.destroy()
    content[0] = []
    if removeAll:
        for box in content[1]:
            box.destroy()
        content[1] = []

def contentCreator(newContent=[]):
    global content, playerAnswer
    num = [0, 0]
    functionToUse = []

    theContentDestroyer9000()

    for info in newContent:

        try:
            gridOrPlace = info[2][0]
        except:
            gridOrPlace = "grid"

        for value in info[1]:
            if info[0] == "label":
                content[0].append(tkinter.Label(text=value))
            elif info[0] == "spinbox":
                playerAnswer = IntVar()
                content[0].append(ttk.Spinbox(
                    from_=float("-inf"),
                    to=float("inf"),
                    value=playerAnswer
                ))
            elif info[0] == "radio":
                playerAnswer = StringVar()
                content[0].append(ttk.Radiobutton(
                    text=value,
                    variable=value
                ))
            elif info[0] == "button":
                functionToUse = value

                content[1 if gridOrPlace == "place" else 0].append(tkinter.Button(
                    text=value,
                    command = lambda toUse = functionToUse : funcExecute(toUse)
                ))
            else:
                raise Exception("Widget provided is not a valid widget type")

            if gridOrPlace == "place":
                content[1][num[1]].place(bordermode=OUTSIDE, anchor=info[2][1])
                num[1] += 1
            else:
                content[0][num[0]].grid(row=num[0])
                num[0] += 1

def funcExecute(functionToUse):
    functionList[functionToUse]()

def options():
    theContentDestroyer9000(True)
    contentCreator([["button", ["Exit"]]])

def exit():
    theContentDestroyer9000()
    contentCreator([["button", ["Options"], ["place", "nw"]]])

functionList = {
    "Options": options,
    "Exit": exit
}

contentCreator([["button", ["Options"], ["place", "nw"]]])
            

mainWindow.mainloop()