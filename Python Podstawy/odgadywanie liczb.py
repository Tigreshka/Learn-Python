import random

start = 1
stop = 100

n = random.randint(start, stop)
tries = 0
#answer = n -1 - opcja przy
answer = start - 1 # 2bruteforce
while answer != n:
    answer = int(input("podaj liczbę: "))
    tries += 1
    if answer > n:
        print("Za mało")
    elif answer < n:
        print("Za dużo")
#print("Brawo, to bylo ", number)
#print("Prób: ", tries)

print("Za ", tries, "razem ")




