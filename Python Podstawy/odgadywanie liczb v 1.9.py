import random

start = 1
stop = 100
# n = random.randint(start, stop)
n = 100
tries = 0
answer = n -1
stop = stop + 1
while answer != n:
    answer = int((stop + start) * 0.5)
    tries += 1
    if  answer > n:
        stop = answer
    elif answer < n:
        start = answer
    print(start, stop)
print("Za ", tries, "razem ")