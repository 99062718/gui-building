import tkinter
from tkinter import Variable, ttk, StringVar, IntVar, messagebox

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=10)
content = []
amountBolletjes = 0
hoorntjes = 0
bakjes = 0

textLabel = tkinter.Label()
textLabel.grid(column=0, row=0)

contentBox = tkinter.Frame()
contentBox.grid(column=0, row=1)

submitBtn = tkinter.Button(text="Start")
submitBtn.grid(column=0, row=2)

def contentCreator(labelText, toCreate="", radioValues=[]):
    global answer
    textLabel.configure(text=labelText)

    if toCreate == "radio":
        num = 0
        answer = StringVar(mainWindow, "")
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
        answer = IntVar(mainWindow, 1)
        content.append(
            ttk.Spinbox(
                contentBox,
                from_=1,
                to=float("inf"),
                textvariable=answer
            )
        )
        content[0].grid(column=0, row=0)

def theContentDestroyer9000(moreToDestroy=[]): # Hey, you! Yeah, you! Have you ever felt like the world would be better without all that stupid content? Well i've got just the thing for you. Introducing: theContentDestroyer9000! Now that pesky content cant bother us anymore!
    global content
    for box in content:
        box.destroy()
    for box in moreToDestroy:
        box.destroy()
    content = []

def beginScreen():
    submitBtn.configure(text="Submit")
    contentCreator("Hoeveel bolletjes wilt u?", "spinbox")
    submitBtn.configure(command=howManyBolletjes)

def howManyBolletjes():
    global amountBolletjes
    
    if answer.get() < 9:
        amountBolletjes += answer.get()
        theContentDestroyer9000()
        if answer.get() < 4:
            contentCreator("Wilt u deze {} bolletje(s) in een hoorntje of een bakje?".format(answer.get()), "radio", ["hoorntje", "bakje"])
            submitBtn.configure(command=hoorntjeOfBakje)
        elif answer.get() > 3:
            contentCreator("Wilt u nog meer bestellen?", "radio", ["ja", "nee"])
            submitBtn.configure(command=againBestellen)
            messagebox.showinfo(message="Dan krijgt u van mij een bakje met {} bolletjes".format(answer.get()))
    else:
        messagebox.showerror(message="Sorry, zulke grote bakken hebben we niet")
    
def hoorntjeOfBakje():
    global hoorntjes, bakjes

    if answer.get() != "":
        if answer.get() == "hoorntje":
            hoorntjes += 1
        elif answer.get() == "bakje":
            bakjes += 1
        theContentDestroyer9000()
        contentCreator("Wilt u nog meer bestellen?", "radio", ["ja", "nee"])
        submitBtn.configure(command=againBestellen)
    else:
        messagebox.showerror(message="Sorry, dat snap ik niet...")

def againBestellen():
    if answer.get() == "ja":
        theContentDestroyer9000()
        beginScreen()
    elif answer.get() == "nee":  
        theContentDestroyer9000([submitBtn])          
        contentCreator("Bedankt en tot ziens!")
    else:
        messagebox.showerror(message="Sorry, dat snap ik niet...")

contentCreator("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
submitBtn.configure(command=beginScreen)

mainWindow.mainloop()