import random
start = 1
stop = 100
n = random.randint(start, stop)
tries = 0
answer = n - 1
actual_stop = stop + 1
actual_start = start
while answer != n:
    answer = int((actual_stop + actual_start) * 0.5)
    tries += 1
    if answer > n:
        actual_stop = answer
    elif answer < n:
        actual_start = answer
print("Za ", tries, " razem !!!")