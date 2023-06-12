from tkinter import *
from tkinter import messagebox

tictactoe = Tk()

tictactoe.title("KrestikiNoliki")

Clicked = True
count = 0 


def Clicked():
    global count, winner

    # if button["text"] == " " and Clicked  == True:
    #    button["text"] = "X"
    #    Clicked = False
    #    count += 1


button1 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button1))
button2 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button2))
button3 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button3))
button4 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button4))
button5 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button5))
button6 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button6))
button7 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button7))
button8 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button8))
button9 = Button(tictactoe, bg='#ccc', height=3, command=lambda: Clicked(button9))

button1.grid(row=0, column=0)
button2.grid(row=0, column=0)
button3.grid(row=0, column=0)

button4.grid(row=0, column=0)
button5.grid(row=0, column=0)
button6.grid(row=0, column=0)

button7.grid(row=0, column=0)
button8.grid(row=0, column=0)
button9.grid(row=0, column=0)