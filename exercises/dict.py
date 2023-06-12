users = {'16': 'Seyran', '12': 'Emir', '17': 'Dawid', '13': 'Geldy', '15': 'Nazar'}

while True:
    password = input("What is your password?")
    for key, value in users.items():
        if password == key:
            print(f"Welcome {value}")
        else:
            print("You are not in dictionary,\n please sign up")
            new_user_password = int(input("What is your password?"))
            new_user = input("What is your name?")
            users[new_user_password] = new_user
            print(users) 
        break