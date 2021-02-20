# Poprosić użytkownika o podanie 3 liczby,
# a następnie wypisać komunikat (w zależności od liczb):
# trzy różne, dwie różne, trzy równe

a = input("Proszę podać pierwszą liczbę: ")
b = input("Proszę podać drugą liczbę: ")
c = input("Proszę podać trzecią liczbę: ")
same_three = "Podano 3 takie same liczby"
same_two = "Podano 2 takie same liczby"
if a == b == c:
    print(same_three)
elif a == b != c:
    print(same_two)
elif a == c != b:
    print(same_two)
elif b == c != a:
    print(same_two)
else:
    print("wszystkie różne")