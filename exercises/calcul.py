while True:
    calcul1 = int(input("Can you write number1,please?"))
    calcul2 = int(input("Can you write number2,please?"))
    simvol = input("What would you like to do? +, -, *, /")
    if simvol == '+':
        print(calcul1+calcul2)
    elif simvol == '-':
        print(calcul1-calcul2)
    elif simvol == '*':
        print(calcul1*calcul2)
    elif simvol == '/':
        print(calcul1/calcul2)