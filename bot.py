from tkinter import *

FONT = 'bahnschrift 13'

def send():
       send = "Вы -> " + input.get()
       txt.insert(END, "\n" + send)
       user = input.get()
       if (user == 'zdarov'):
             txt.insert(END,"\n" "Bot ->  ku yept")     
       elif (user == 'how are you?' or 'как дела'):
            txt.insert(END,"\n" "Bot ->  da norm") 
       elif (user == 'how are you?' or 'как дела'):
            txt.insert(END,"\n" "Bot ->  da norm")
       else:
             txt.insert(END, "\n")

       input.delete(0, END)       

display  = Tk() #вкладываем интерфейс в переменную
display.title("TupoBot")  #заголовок
display.resizable(0, 0) #запрещает менять размер
display.geometry("300x500") #geometry это размер
display['bg'] = 'lightgreen' #background color
input = Entry(display, bg="gray", fg="blue", width=39) #ввод
input.place(x = 2, y = 460) #ввод расположение
txt = Text(display, bg="red", fg="white", width=40, height=20) #текст
txt.place(x = 0, y = 0)
txt.insert(END, "Bot -> привет, это бот который бот :)")
send = Button(display, font = FONT, text="Send", command=send).place(x=245, y=445)

display.mainloop() #запускает
