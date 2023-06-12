import random
number=random(1,10)
question=int(input("Угадай число от 1 до 10:"))
while question!=number:
    question=int(input("Повторите попытку:"))
    if question<number:
        print("Ваше число меньше чем загаданное")
    elif question>number:
        print("Ваше число больше чем загаданное")
    else:
        print("Вы угадали число")
print(question)
print(number)