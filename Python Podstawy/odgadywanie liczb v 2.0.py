import random
start = 1
stop = 100
actual_start = start
actual_stop = stop
n = random.randint(start, stop)
tries = 0
#answer = n - 1
answer = start -1
while answer != n:
    answer = random.randint(actual_start, actual_stop)
    tries += 1
    if answer > n:
        actual_stop = answer
    elif answer < n:
        actual_start = answer
print("Za ", tries, " razem")