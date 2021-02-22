state = False
for i in range(4):
    for j in range(10):
        print(i + j, end="")
        if i + j == 8:
            state =  True
            break
    if state:
        break
    print()

print("koniec")