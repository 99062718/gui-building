import tkinter
from tkinter import BooleanVar, StringVar, IntVar, messagebox, ttk

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=10)

punten = 0

# this array has all the data needed to generate the questions, boxes, ect
dataArray = [
    ["Hoeveel jaren ervaring heeft met dieren-dressuur, jongleren of acrobatiek?", 3],
    ["Wat voor school diploma heeft u?", "mbo-4 ondernemen"],
    ["Heeft u ervaring in het rijden van een voertuig? Zo ja, welk voertuig?", "vrachtwagen"],
    ["Draagt u hoge hoeden?", ["ja", "nee"]],
    ["Wat is uw geslacht?", ["man", "vrouw"]],
    [["Hoe breed is uw snor?", "Hoe lang is uw haar?"], [9, 19]],
    ["Bent u ooit naar een circus geweest?", ["ja", "nee"]],
    ["Hoeveel cm lang bent u?", 150],
    ["Heeft u hiervoor een baan in het circus gehad?", ["ja", "nee"]],
    ["Hoe zwaar bent u?", 90],
    ["Heeft u een certificaat 'Overleven met gevaarlijk personeel'?", ["ja", "nee"]],
    ["Vind u clowns leuk?", ["ja", "nee"]]
]

# this array will contain all the questions, boxes, ect that the function creates
dataCreated = []

# these are variables that will later be used to check answers
toCheck = []

if punten >= 8:
    print("Gefeliciteert! U heeft de baan!")
else:
    print("Helaas! U heeft niet alle qualificaties voor de baan.")

def dataSifter():
    global num
    num = 0

    for data in dataArray:
        toCheck.append([])
        toCheck[num].append(data[1])

        dataCreated.append([])
        dataCreated[num].append(tkinter.Frame())
        dataCreated[num][0].grid(column=0, row=num, pady=5)

        dataCreated[num].append(tkinter.Label(dataCreated[num][0], text=data[0] if type(data[0]) != type([]) else data[0][1]))
        dataCreated[num][1].grid(column=0, row=0)

        # checks dataArray to see what widget it needs to use
        if type(data[1]) == type(1) or type(data[0]) == type([]):
            questionCreator("spinbox")
        elif type(data[1]) == type([]):
            questionCreator("radio")
        elif type(data[1]) == type("According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don't care what humans think is impossible."):
            questionCreator("entry")

        num += 1

def questionCreator(widgetType): # creates widgets
    if widgetType == "spinbox":
        toCheck[num].append(IntVar())
        dataCreated[num].append(
            ttk.Spinbox(
                dataCreated[num][0],
                from_=1,
                to=float("inf"),
                textvariable=toCheck[num][1]
            )
        )

        if type(dataArray[num][0]) == type([]):
            currentNum = num
            for x in range(2):
                dataCreated[num - 1][2 + x].bind("<Button-1>", lambda possibleQuestions=dataArray[num][0], changeCondition=dataArray[num - 1][1][0], currentCondition=toCheck[num - 1][1].get(), currentNum=currentNum: questionChanger(possibleQuestions, changeCondition, currentCondition, currentNum))

        dataCreated[num][2].grid(column=0, row=1)
    elif widgetType == "radio": # I could, in theory, make this have the ability to have as many radiobuttons as id want. But do i want to?
        toCheck[num].append(BooleanVar())
        for subNum in range(2):
            dataCreated[num].append(
                ttk.Radiobutton(
                    dataCreated[num][0],
                    text=toCheck[num][0][subNum],
                    value=True if subNum == 0 else False,
                    variable=toCheck[num][1]
                )
            )
            dataCreated[num][subNum + 2].grid(column=0, row=subNum + 1)
    elif widgetType == "entry":
        toCheck[num].append(StringVar())
        dataCreated[num].append(ttk.Entry(dataCreated[num][0], textvariable=toCheck[num][1]))
        dataCreated[num][2].grid(column=0, row=1)

def questionChanger(possibleQuestions, changeCondition, currentCondition, currentNum):
    if changeCondition == currentCondition:
        dataCreated[currentNum][1].configure(text=possibleQuestions[0])
    else:
        dataCreated[currentNum][1].configure(text=possibleQuestions[1])


dataSifter()

mainWindow.mainloop()