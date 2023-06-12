file_path = r'D:\LDPlayer\pi_digits.txt'
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birth_day = int(input("When was you born?"))
if birth_day in pi_string:
    print('Your birthday here')
else:
    print('loser')