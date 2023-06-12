# a = int(input(":"))
# b = int(input(":"))
# while a >= b:
#      a-=b
#
#print(a)
# 
n = int(input("n = "))
# st = 1
# while st<n:
#       st=st*3
# print(st==n)

#for3
a=int(input())
b=int(input())
k=0
for i in range(a+1,b):
    print(i,end=' ')
    k+=1
print()
print(k)

#for4
n = float(input())
for i in range(10):
    i = i*n
    print(i)

#for6
price = float(input('1.0 кг = '))
for i in range(2, 10+1, 2):
print(1 + i/10, 'кг =', price + price * i/10