# num1 = 2
# num2 = 4

# summa = num1 + num2

# print("Summa etih dolb, to yest {0} i {1} eto {2}".format(num1, num2, summa))

def slojit(a, b): #add
    return a + b
#функция для сложения

def vycitat(a, b): #substract
    return a - b

def umnojat(a, b): #multiply
    return a * b    

def delit(a, b): #divide
    return a / b

print("Vyberite pojalusta odno iz etih operatorov:") #Choose one of this operators
print("1.Slojenie") #1.Add
print("2.Vycitanie") #2.Substract
print("3.Umnojenie") #3.Multiple
print("4.Deleniye") #4.Divide

while True:
    variant = input("Vvedite variant(1, 2, 3, 4): ")
    if variant in ('1', '2', '3', '4'):
        try:
            nomer1 = float(input("Vashe pervoe chislo: "))
            nomer2 = float(input("Vashe vtoroe chislo: "))
        except ValueError:
            print("vvedi pj chislo")
            continue
        
        if variant == '1':
            print(nomer1, '+', nomer2, '=', slojit(nomer1, nomer2))
            
        elif variant == '2':
            print(nomer1, '-', nomer2, '=', vycitat(nomer1, nomer2))
            
        elif variant == '3':
            print(nomer1, '*', nomer2, '=', umnojat(nomer1, nomer2))
            
        elif variant == '4':
            print(nomer1, '/', nomer2, '=', delit(nomer1, nomer2))
            
        next_operaciya = input("hatiti isho raz? (kanishna/netblat): ")
        if next_operaciya == "netblat":
            break
    
    else:
        print("ty mne vtiraesh kakuyu to dic")