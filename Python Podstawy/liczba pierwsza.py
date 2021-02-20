n = int(input("podaj liczbę : "))
for i in range(2, n):
    if n % i == 0:
        print("nie pierwsza")
        break
else:
    print("pierwsza")



Version 2:
#n = int(input("podaj liczbę : "))
for n in range (2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, "pierwsza")