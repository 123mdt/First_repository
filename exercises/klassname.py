def mates():
    password = {'Medet' : 2010, 'Dawut' : 2006, 'Nazar' : 2007, 'Geldi' : 2007, 'Emir' : 2007, 'Seyran' : 1900}
    while True:
        name = input("WHAT IS YOUR NAME?")
        if name in password:
            print("YOU ARE IN DICT")
        elif name not in password:
            create_new = input("YOU ARE NOT IN DICT,\nPLEASE REGISTER?\nWRITE YOUR NAME AND PASSWORD : ")
            if create_new == 'YES':
                name1 = input("WHAT IS YOUR NAME?")
                pass1 = int(input("WHAT IS YOUR PASSWORD?"))
                password[name1] = pass1

mates()