"""
Napisz program, ktory pobiera od uzytkownika dwie liczby calkowite A - a (int) oraz B - b (int), gdzie A < B,
a nastepnie oblicza sume ciagu liczb od A do B (A, A + 1, A + 2, . . . , B) i wypisuje ja w konsoli.
Gdy warunek A < B nie zostaje spelniony, program konczy prace wypisujac w konsoli "Robota skonczona".
Przykladowo dla A = 4 i B = 11 program powinien wypisac w konsoli liczbe 60.
Dane pobierz od uzytkownika w konsoli za pomoca funkcji input(). Nie podawaj do niej zadnego argumentu.
"""

a = int(input())
b = int(input())
sum = 0

if a >= b:
    print("robota skończona")
else:
    for i in range(a, b + 1):
        sum += i
    print(sum)