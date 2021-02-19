n = int(input("Szerokość prostokąta: "))
m = int(input("Wysokość prostokąta: "))
o, p , r, s = "+ ", "- ", "| ", "  "
if n < 0 or m <0:
    print("Wpisz wartość większą od zera")
else:
    print(o, p * (n - 2), o)
    for i in range(m - 2):
        print(r, s * (n - 2), r)
    print(o, p * (n - 2), o)




