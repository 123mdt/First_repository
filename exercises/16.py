a = float(input(":"))
b = float(input(":"))
c = float(input(":"))
if a < b and a < c and b > a and b < c:
    print(a * 2, b * 2, c * 2)
else:
    print(a * -1, b * -1, c * -1)