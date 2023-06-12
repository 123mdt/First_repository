# def pizza(price, **kwargs):
    print(kwargs)
#
# pizza(12, pepperoni='kolbasa', pizza='masliny')

# def name(*args):
#    n = 0
#   for i in args:
        print(f'#{n+1} {i}')
#
# name('Nazar', 'Dawut', 'Medet') 
def name(*args, **kwargs):
    for keys, values in kwargs.items():
        print(f'his name {keys}\nhis sername {values}')

name(seyran='dov', nazar='ag', geldi='del')