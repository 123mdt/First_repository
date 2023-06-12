nm1 = int(input(":"))
nm2 = int(input(":"))
nm3 = int(input(":"))

if (nm1>nm2) and (nm1>nm3):
    print(nm1)
elif (nm2>nm3) and (nm2>nm1):
    print(nm2)
elif (nm3>nm2) and (nm3>nm1):
    print(nm3)

if (nm1<nm2) and (nm1>nm3):
    print(nm1)
elif (nm2<nm3) and (nm2>nm1):
    print(nm2)
elif (nm3<nm2) and (nm3>nm1):
    print(nm3)