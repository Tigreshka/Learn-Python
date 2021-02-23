n1 = int(input("podaj liczbe startowa "))
n2 = int(input("podaj liczbe koncowa "))

if n1 > n2:
    start = n2
    stop = n1
else:
    start = n1
    stop = n2

result = 0
for i in range(start, stop + 1):
    result += i

print("Suma = ", result)