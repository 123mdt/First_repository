import random

choose = input("Выбирай - камень, ножницы, бумага")
objects = ["камень", "ножницы", "бумага"]
action = random.choice(choose)
print(f"\nВы выбрали {objects}, компьютер выбрал {action}.\n")

if choose == action:
    print(f"Оба пользователя выбрали {choose}. Ничья!!")
elif choose == "камень":
    if action == "ножницы":
        print("Камень бьет ножницы! Вы победили!")
    else:
        print("Бумага оборачивает камень! Вы проиграли.")
elif choose == "бумага":
    if action == "камень":
        print("Бумага оборачивает камень! Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли.")
elif choose == "ножницы":
    if action == "камень":
        print("Ножницы режут бумагу! Вы победили!")
    else:
        print("Камень бьет ножницы! Вы проиграли.")
