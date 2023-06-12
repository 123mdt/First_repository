name = ['Imir', 'Davud', 'Nazar', 'Geldy', 'Medet']
print(name[2])
print(name[-2])
print(name[::2])
# text = 'Hello, world'
# print(text.split(', '))
name.append('Seyran')
name.insert(2, 'Sasha')
print(name)
text = ['bing']
text = 10
print(text)
name.extend(text)
print(name)
del name[2]
print(name)
name.remove('Imir')
name.pop()
# name.clear()
print(name.index('Geldy'))
print(name.count('Imir'))
name.sort()
name2 = name.sorted()
len(name)