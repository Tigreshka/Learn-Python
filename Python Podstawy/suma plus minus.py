"""
Poprosić użytkownika o podanie liczby naturalnej, a następnie policzyć sumę
1 + 2 - 3 + 4 +5 -6 -7 + 8 +9 +10 - 11 - 12 -13 + ......n, gdzie n jest podaną
 liczbą przez użytkownika.
"""

liczba = int(input("Podaj liczbe "))

suma = 0
for i in range(1,liczba+1,1):
   suma = suma + i

print(f"Suma wynosi: {suma}")