# n  = 5
#
# 1
# 22
# 333
# 4444
# 55555

n = int(input("podaj liczbę : "))

for row in range(n):
    for col in range(row + 1):
        print(row + 1, end="")
    print()
