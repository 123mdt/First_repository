word = (input(':'))
print(word.split()) #разбивает строки по раздилителю
print(word.rstrip()) #убирает пробел в правом конце
print(word.lstrip()) #убирает пробел в левом конце
print(word.strip()) #убирает пробел справо и слево
print(word.title()) #первую букву делает заглавной
print(word.upper()) #все буквы делает большими
print(word.lower()) #все буквы делает маленькими
print(word.capitalize()) #первую букву делает заглавной а остальные маленькими
print(word.swapcase()) #переводит маленькие буквы в заглавные а заглавные в маленькие

print(word[0:-1:3])