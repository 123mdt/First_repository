from tkinter import *
from tkinter import messagebox

tictactoe = Tk()

tictactoe.title("KrestikiNoliki")

Clicked = True
count = 0 

def checked():
    global winner
    winner = False

    if button1["text"] == "O" and button2 ["text"] == "O" and button3 ["text"] == "O":
        button1.config(bg="lime") #{X}{X}{X}
        button2.config(bg="lime") #{O}{O}{O}
        button3.config(bg="lime") #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button4["text"] == "O" and button5 ["text"] == "O" and button6 ["text"] == "O":
        button1.config(bg="lime") #{O}{O}{O}
        button2.config(bg="lime") #{X}{X}{X}
        button3.config(bg="lime") #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button7["text"] == "O" and button8 ["text"] == "O" and button9 ["text"] == "O":
        button1.config(bg="lime") #{O}{O}{O}
        button2.config(bg="lime") #{O}{O}{O}
        button3.config(bg="lime") #{X}{X}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="lime") #{X}{O}{O}
        button2.config(bg="lime") #{X}{O}{O}
        button3.config(bg="lime") #{X}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button1.config(bg="lime") #{O}{X}{O}
        button2.config(bg="lime") #{O}{X}{O}
        button3.config(bg="lime") #{O}{X}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button1.config(bg="lime") #{O}{O}{O}
        button2.config(bg="lime") #{O}{O}{X}
        button3.config(bg="lime") #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="lime") #{X}{O}{O}
        button2.config(bg="lime") #{O}{X}{O}
        button3.config(bg="lime") #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button1["text"] == "O" and button2 ["text"] == "O" and button3 ["text"] == "O":
        button1.config(bg="lime") #{X}{X}{X}
        button2.config(bg="lime") #{O}{O}{O}
        button3.config(bg="lime") #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
    elif button3["text"] == "X" and button5["text"] == "O" and button7["text"] == "O":
        button1.config(bg="lime") #{X}{O}{O}
        button2.config(bg="lime") #{O}{X}{O}
        button3.config(bg="lime") #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")            

def checkedDraw():
    global count, winner

    if count == 9 and winner == False: #если все блоки заняты и победителя нет
        messagebox.showerror("Nichya", "Zanovo blet")
        nachalo()


def Clicked(button):
    global count, winner

    if button["text"] == " " and Clicked  == True:
       button["text"] = "X"
       Clicked = False
       count += 1 #после каждого клика добавляется счет
       checkedWinner()


    elif button["text"] == " " and Clicked  == True:
        button["text"] = "O"
        Clicked = False
        count += 1 #после каждого клика добавляется счет
        checkedWinner()

    else:
        messagebox.showerror("Ne ta knpka", "Vybirayte drug blok")    
    

def nachalo():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global cliked, count #объявляем глобально чтобы был доступ в других функциях
    clicked = True #кнопки можно нажимать
    count = 0 #счет ноль в начале
button1 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button2 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button3 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button4 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button5 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button6 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button7 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button8 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))
button9 = Button(tictactoe, text = " ", height=3, width=7, command=lambda: Clicked(button1))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

nachalo()
tictactoe.mainloop()