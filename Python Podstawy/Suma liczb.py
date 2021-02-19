msg = "podaj liczbe != 0 "
sum = 0
number = 1
while number != 0:
    number = int(input(msg))
    print("podałeś :", number)
    sum = sum + number
print("Suma liczb to ", sum)