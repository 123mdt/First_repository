try:
       import pyperclip
except ImportError:
       print("You should install pyperclip")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
       print('Do you want to (e)ncrypt or (d)ecrypt')
       response = input('>').lower()
       if response.startswith('e'):
              mode = 'encrypt'
              break
       elif response.startswith('d'):
              mode = 'decrypt'
              break
       print('Please enter letter e or d')

while True:
       maxkey = len(SYMBOLS) - 1
       print(f'Please enter the key (0 to {maxkey}) to use')
       response = int(input('>'))

       if 0 <= response < len(SYMBOLS):
              key = response
              break

print(f'Enter the message to {mode}')
message = input('>')

message = message.upper()

translated = ''

for symbol in message:
       if symbol in SYMBOLS:
           num = SYMBOLS.find(symbol)
           if mode == 'encrypt':
               num += key
           elif mode == 'decrypt':
               num -= key
              
       if num >= len(SYMBOLS):
              num -= len(SYMBOLS)
       elif num < 0:
              num += len(SYMBOLS)

       translated += SYMBOLS[num]
else:
       translated += symbol


print(translated)

try:      
       pyperclip.copy(translated)
       print(f'Full {mode}ed text copied to clipboard')
except:
       pass