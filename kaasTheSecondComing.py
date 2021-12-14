import tkinter
from tkinter import BooleanVar, Radiobutton, ttk, messagebox, StringVar

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=20)

#--------------------------------------------------------------

vragenNummer = 0

kaasVragen = [
    "Is de kaas geel?",
    "Zitten er gaten in?",
    "Is de kaasbelachelijk duur?",
    "Is de kaas hard als steen?",
    "Heeft de kaas blauwe schimmel?",
    "Heeft de kaas een korst?",
    "Heeft de kaas een korst?"
]

kaasSoorten = [
    "Emmenthaler",
    "Leerdammer",
    "Parmigiano Reggiano",
    "Goudse kaas",
    "Bleu de Rochbaron",
    "Fourme d'Ambert",
    "Camembert",
    "Mozzarella"
]

#--------------------------------------------------------------

questionText = StringVar(mainWindow, "gagd")
questionLabel = tkinter.Label(textvariable=questionText)
questionLabel.grid(column=0, row=0, pady=10)

radiobuttons = []
trueOrFalse = StringVar()
for num in range(2):
    radiobuttons.append(
        ttk.Radiobutton(text="Ja" if num == 0 else "Nee", value="ja" if num == 0 else "nee", variable=trueOrFalse)
    )
    radiobuttons[num].grid(column=0, row=num+1)

#--------------------------------------------------------------

def vragenMaker(jaNummer, neeNummer, kaasJa, kaasNee):
    global kaasJaAndNee
    global nummerJaAndNee
    kaasJaAndNee = [kaasJa, kaasNee]
    nummerJaAndNee = [jaNummer, neeNummer]

    questionText.set(kaasVragen[vragenNummer])

def answerCheck():
    global vragenNummer

    if trueOrFalse.get() == "ja":
        vragenNummer += nummerJaAndNee[0]
        kaas = kaasJaAndNee[0]
    elif trueOrFalse.get() == "nee":
        vragenNummer += nummerJaAndNee[1]
        kaas = kaasJaAndNee[1]
    else:
        messagebox.showerror(message="Je moet op een van de knoppen klikken!")

    if kaas is not None:
        kaasAntwoord(kaas)

    if vragenNummer == 1 or vragenNummer == 4:
        vragenMaker(1, 2, None, None)
    elif vragenNummer == 2:
        vragenMaker(0, 0, 0, 1)
    elif vragenNummer == 3:
        vragenMaker(0, 0, 2, 3)
    elif vragenNummer == 5:
        vragenMaker(0, 0, 4, 5)
    elif vragenNummer == 6:
        vragenMaker(0, 0, 6, 7)

def kaasAntwoord(kaas):
    messagebox.showinfo(message="Uw beschreven kaas is: " + kaasSoorten[kaas] + "!")
    mainWindow.destroy()

#--------------------------------------------------------------

submitButton = tkinter.Button(text="Submit", bg="white", fg="black", command=answerCheck)
submitButton.grid(column=0, row=3)

vragenMaker(1, 4, None, None)

mainWindow.mainloop()