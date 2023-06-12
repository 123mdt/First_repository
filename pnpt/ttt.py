from tkinter import *
from tkinter import messagebox
import time

tictactoe = Tk()

tictactoe.title("KrestikiNoliki")

Clicked = True
count = 0 

def checkedWinner():
    global winner
    winner = False
    
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="lime")  #{X}{X}{X}
        button2.config(bg="lime")  #{O}{O}{O}
        button3.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
       nachalo()

     elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="lime")  #{O}{O}{O}
        button5.config(bg="lime")  #{X}{X}{X}
        button6.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()

    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="lime")  #{O}{O}{O}
        button8.config(bg="lime")  #{O}{O}{O}
        button9.config(bg="lime")  #{X}{X}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()

    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="lime")  #{X}{O}{O}
        button4.config(bg="lime")  #{X}{O}{O}
        button7.config(bg="lime")  #{X}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="lime")  #{O}{X}{O}
        button5.config(bg="lime")  #{O}{X}{O}
        button8.config(bg="lime")  #{O}{X}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="lime")  #{O}{O}{X}
        button6.config(bg="lime")  #{O}{O}{X}
        button9.config(bg="lime")  #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="lime")  #{X}{O}{O}
        button5.config(bg="lime")  #{O}{X}{O}
        button9.config(bg="lime")  #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="lime")  #{X}{O}{O}
        button5.config(bg="lime")  #{O}{X}{O}
        button7.config(bg="lime")  #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="lime")  #{O}{O}{O}
        button2.config(bg="lime")  #{O}{O}{O}
        button3.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()

    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="lime")  #{O}{O}{O}
        button5.config(bg="lime")  #{O}{O}{O}
        button6.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()

    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="lime")  #{O}{O}{O}
        button8.config(bg="lime")  #{O}{O}{O}
        button9.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()

    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="lime")  #{O}{O}{O}
        button4.config(bg="lime")  #{O}{O}{O}
        button7.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="lime")  #{O}{O}{O}
        button5.config(bg="lime")  #{O}{O}{O}
        button8.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="lime")  #{O}{O}{O}
        button6.config(bg="lime")  #{O}{O}{O}
        button9.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="lime")  #{O}{O}{O}
        button5.config(bg="lime")  #{O}{O}{O}
        button9.config(bg="lime")  #{O}{O}{O}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="lime")  #{X}{O}{O}
        button5.config(bg="lime")  #{O}{X}{O}
        button7.config(bg="lime")  #{O}{O}{X}
        winner = True
        messagebox.showinfo("Pobeditel izvesten!", "Pervyy pobedil")
        nachalo()
        
def checkedDraw(): #ничья
    global count, winner

    if count == 9 and winner == False: #если все блоки заняты И победителя нет
        messagebox.showerror("Nichya", "Zanovo blet") 
        nachalo()


def buttonClicked(button): #нажатие
    global count, winner
    global clicked

    if button["text"] == " " and clicked  == True:
       button["text"] = "X"
       clicked = False #
       count += 1 #после каждого клика добавляется счет
       checkedWinner() #проверяем известен ли победитель
       checkedDraw() #проверяем на ничью


    elif button["text"] == " " and clicked  == False:
       button["text"] = "O"
       clicked = True 
       count += 1 #после каждого клика добавляется счет
       checkedWinner() #проверяем известен ли победитель
       checkedDraw() #проверяем на ничью


    else:
        messagebox.showerror("Ne ta knopka", "Vybirayte drug blok")
       

def nachalo():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, count #обьявляем глобально чтобы был лоступ в других функциях
    clicked = True #кнопки можно нажимать
    count = 0 #счет ноль в начале

    button1 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button1))
    button2 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button2))
    button3 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button3))

    button4 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button4))
    button5 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button5))
    button6 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button6))
    
    button7 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button7))
    button8 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button8))
    button9 = Button(tictactoe, bg='#ccc', font="Symbol, 20", text = " ", height=3, width=7, command=lambda: buttonClicked(button9))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

nazvanie = Menu(tictactoe)
tictactoe.config(menu = nazvanie)

optionMenu = Menu(nazvanie) #создаем опции меню
nazvanie.add_cascade(label="Options", menu = optionMenu) #addCascade добавляет коробочку с названием
optionMenu.add_command(label="Restart", command=nachalo) #addCommand добавляет команду через функциями

nachalo()
tictactoe.mainloop()