import tkinter
from tkinter import Variable, ttk, StringVar, IntVar, messagebox

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=10)
content = []

textLabel = tkinter.Label(text="Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
textLabel.grid(column=0, row=0)

contentBox = tkinter.Frame()
contentBox.grid(column=0, row=1)

def contentCreator(labelText, toCreate, radioValues=[]):
    global answer
    textLabel.configure(text=labelText)

    if toCreate == "radio":
        num = 0
        answer = StringVar()
        for value in radioValues:
            content.append(
                ttk.Radiobutton(
                    contentBox,
                    text=value,
                    value=value,
                    variable=answer
                )
            )
            content[num].grid(column=0, row=num)
            num += 1
    elif toCreate == "spinbox":
        answer = IntVar()
        content.append(
            ttk.Spinbox(
                contentBox,
                from_=1,
                to=float("inf"),
                textvariable=answer
            )
        )
        content[0].grid(column=0, row=0)

def theContentDestroyer9000(): # Hey, you! Yeah, you! Have you ever felt like the world would be better without all that stupid content? Well i've got just the thing for you. Introducing: theContentDestroyer9000! Now that pesky content cant bother us anymore!
    for box in content:
        box.destroy()

def howManyBolletjes():
    contentCreator("Hoeveel bolletjes wilt u?", "spinbox")

howManyBolletjes()

mainWindow.mainloop()