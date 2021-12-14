import tkinter
from tkinter import IntVar, Radiobutton, StringVar, ttk
from tkinter import messagebox

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=10)

pizzaSmall = 4
pizzaMedium = 7
pizzaLarge = 10
smallAmount = mediumAmount = largeAmount = 0
labelText = StringVar()
QuestionLabel = tkinter.Label(textvariable=labelText)
QuestionLabel.grid(column=0, row=0)

contentFrame = tkinter.Frame()
contentFrame.grid(column=0, row=1)

def validateInputs():
    global smallAmount
    global mediumAmount
    global largeAmount

    if inputAmount.get() >= 1:
        if pizzaType.get() == "small":
            smallAmount += inputAmount.get()
            meerBestellen()
        elif pizzaType.get() == "medium":
            mediumAmount += inputAmount.get()
            meerBestellen()
        elif pizzaType.get() == "large":
            largeAmount += inputAmount.get()
            meerBestellen()
        else:
            messagebox.showerror(message="Klik op een van de pizza's!")
    else:
        messagebox.showerror(message="Vul een geldige hoeveelheid pizza's in!")

def bestellingMaker():
    global pizzaType
    global inputAmount

    labelText.set("Wat voor pizza wilt u? ")
    radiobuttons = []
    usableTypes = ["small", "medium", "large"]
    pizzaType = StringVar()
    
    for num in range(3):
        radiobuttons.append(
            ttk.Radiobutton(contentFrame, text=usableTypes[num], variable=pizzaType, value=usableTypes[num])
        )
        radiobuttons[num].grid(column=0, row=num)

    inputAmount = IntVar()
    inputLabel = tkinter.Label(text="Hoeveel van deze pizza wilt u?")
    inputLabel.grid(column=0, row=2)
    amountSpinbox = ttk.Spinbox(from_=1, to=float("inf"), textvariable=inputAmount)
    amountSpinbox.grid(column=0, row=3)

    submitButton = tkinter.Button(text="Submit", command=validateInputs)
    submitButton.grid(column=0, row=4)

def meerBestellen():
    meerVraag = messagebox.askyesno(message="Wilt u nog meer bestellen?")

    if meerVraag == False:
        rekeningMaker()

def rekeningMaker():
    smallPrice = smallAmount * pizzaSmall
    mediumPrice = mediumAmount * pizzaMedium
    largePrice = largeAmount * pizzaLarge
    totalPrice = smallPrice + mediumPrice + largePrice

    messagebox.showinfo(message="----------------------------------------------------\n{}{}{}Uw totale bedrag is   : ".format(str(smallAmount) + " small pizza's      : " + str(smallPrice) + " euro\n" if smallPrice > 0 else "", str(mediumAmount) + " medium pizza's      : " + str(mediumPrice) + " euro\n" if mediumPrice > 0 else "", str(largeAmount) + " large pizza's      : " + str(largePrice) + " euro\n" if largePrice > 0 else "") + str(totalPrice) + " euro\n----------------------------------------------------")

    mainWindow.destroy()


bestellingMaker()

mainWindow.mainloop()