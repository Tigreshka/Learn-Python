"""
Napisz program, ktory pobiera od uzytkownika liczbe calkowita dodatnia - number (int),
a nastepnie wypisuje w konsoli kolejno wszystkie dodatnie liczby niepatrzyste nie wieksze od podanej liczby.
Przykladowo dla liczby 15 program powinien wypisac w konsoli liczby: 1, 3, 5, 7, 9, 11, 13, 15.
Dane pobierz od uzytkownika w konsoli za pomoca funkcji input(). Nie podawaj do niej zadnego argumentu.
"""

number = int(input())
for i in range(1, number+1):
    if i % 2 != 0:
        print(i)