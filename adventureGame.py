import tkinter
from tkinter import ttk, IntVar, StringVar, messagebox
import random

mainWindow = tkinter.Tk()
mainWindow.configure(pady=20, padx=50)

characters = ["hero"]
maxHealth = 15
health = 15
damageMultiplier = 1
playerAnswer = ""

content = [[],[]]

# todo: Create a function that goes through a list of functions it can use (would be useful for buttons created with the contentCreator),
# remake room system from original file to be more dynamic and easier to work with,
# make options menu in gui

def theContentDestroyer9000(removeAll="no"): # theContentDestroyer9000 is back in stock yet again. Now for 30% off for you and your family to destroy content with during the holidays!
    global content
    for box in content[0]:
        box.destroy()
    content[0] = []
    if removeAll == "yes":
        for box in content[1]:
            box.destroy()
        content[1] = []

def contentCreator(newContent=[], gridOrPack="grid"):
    global content
    num = [0, 0]

    theContentDestroyer9000()

    for info in newContent:
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
                functionToUse = info[2]
                content[0 if gridOrPack == "grid" else 1].append(tkinter.Button(
                    text=value,
                    command=lambda: functionFinder(functionToUse)
                ))
            else:
                raise Exception("Widget provided is not a valid widget type")

            if gridOrPack == "grid":
                content[0][num].grid(row=num)
                num[0] += 1
            else:
                content[1][num].pack()
                num[1] += 1

def functionFinder(functionToUse)
            

mainWindow.mainloop()