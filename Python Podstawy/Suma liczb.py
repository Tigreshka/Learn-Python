msg = "podaj liczbe != 0 "
sum = 0
numbers = 0
number = 1
while number != 0:
    number = int(input(msg))
    print("podałeś :", number)
    sum = sum + number
    numbers = numbers + 1

# nie licze ostatniego zera
numbers = numbers - 1

print("Suma liczb to ", sum)
print("podałeś ", numbers, "liczb(y)")