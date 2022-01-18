import time
import tkinter
from functools import cache

mainWindow = tkinter.Tk()
mainWindow.configure(bg="white")

prevNumber = 0
currentNumber = 1

@cache
def fibonacci(number1, number2):
    global prevNumber, currentNumber, content
    total = number1 + number2
    prevNumber = number2
    currentNumber = total

    label = tkinter.Label(
        text=total,
        fg="black"
    )

    label.pack()

    time.sleep(5)
    if currentNumber > 100000000:
        return ""
    fibonacci(prevNumber, currentNumber)

fibonacci(prevNumber, currentNumber)

mainWindow.mainloop()