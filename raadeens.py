import random
import tkinter
from tkinter import StringVar, ttk, IntVar, messagebox
from tkinter.constants import OUTSIDE, Y

mainWindow = tkinter.Tk()
mainWindow.configure(padx=100, pady=10)

x = 1
score = 0
aantalGeraden = 0

def newRound():
    global randomNum
    global x
    global y

    y = 0
    x += 1
    randomNum = random.randint(1, 1000)
    rondeText.set("ronde " + str(x))

def continuePlaying():
    if x > 19:
        messagebox.showinfo(message="U heeft " + str(aantalGeraden) + " keer geraden\nU heeft " + str(score) + " keer goed geraden!")
        mainWindow.destroy()
    
    KeepPlaying = messagebox.askyesno(message="Wilt u nog een ronde spelen?")

    if not KeepPlaying:
        messagebox.showinfo(message="U heeft " + str(aantalGeraden) + " keer geraden\nU heeft " + str(score) + " keer goed geraden!")
        mainWindow.destroy()

def checkGuess():
    global score
    global aantalGeraden
    global y

    aantalGeraden += 1
    
    if guessVar.get() == randomNum:
        score += 1
        messagebox.showinfo(message="U heeft het antwoord geraden!")
        continuePlaying()
    elif guessVar.get() - randomNum <= 20 and guessVar.get() - randomNum > 0 or randomNum - guessVar.get() <= 20 and randomNum - guessVar.get() > 0:
        messagebox.showwarning(message="U bent heel warm")
    elif guessVar.get() - randomNum <= 50 and guessVar.get() - randomNum > 0 or randomNum - guessVar.get() <= 50 and randomNum - guessVar.get() > 0:
        messagebox.showwarning(message="U bent warm")
    elif guessVar.get() > randomNum:
        messagebox.showwarning(message="U moet lager raden")
    else:
        messagebox.showwarning(message="U moet hoger raden")
    y += 1
    if y > 9:
        messagebox.showerror(message="U heeft geen pogingen meer.")
        continuePlaying()

rondeText = StringVar()
rondeLabel = tkinter.Label(textvariable=rondeText)
rondeLabel.place(bordermode=OUTSIDE)

textLabel = tkinter.Label(text="Voer een getal in tussen 1 en 1000")
textLabel.grid(column=0, row=0)

guessVar = IntVar(mainWindow, 1)
guessSpinbox = ttk.Spinbox(textvariable=IntVar, from_=1, to=1000, wrap=True)
guessSpinbox.grid(column=0, row=1)

submitButton = tkinter.Button(command=checkGuess, text="Submit")
submitButton.grid(column=0, row=2)

newRound()

mainWindow.mainloop()