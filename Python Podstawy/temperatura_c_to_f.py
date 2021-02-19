#Napisz program, ktory na podstawie zmiennej temperatura w stopniach Celsjusza - temp_in_celsius (float), obliczac bedzie temperature w stopniach Farhenheita
#(stopnie Fahrenheita = 1.8 * stopnie Celsjusza + 32.0) i wypisywac ja w konsoli.
#Temperature pobierz od uzytkownika w konsoli za pomoca funkcji input(). Nie podawaj do niej zadnego argumentu.

temp_in_celsius = float(input())
a = temp_in_celsius * 1.8 + 32.0
print(a)

