a, b = map(int,input("enter 2 number: ").split())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)