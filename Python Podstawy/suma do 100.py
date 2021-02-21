# Pobieramy z klawiatury liczby całkowite aż do moentu,
# gdy ich suma nie przekroczy liczby 100.
# Na zakończenie wypisujemy ostatnią poprawną sumę oraz ile liczb zostało dodanych (do poprawnej sumy)

result = 0
while result < 100:
    n = int(input("podaj liczbę: "))
    old_result = result
    result += n

print("Suma : ", old_result)