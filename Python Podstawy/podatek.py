#Napisz program, ktory na podstawie zmiennej: przychod - income (float),
#obliczac bedzie kwote naleznego podatku dochodowego od osob fizycznych i wypisywac ja w konsoli.
#Podatek obliczany jest wedeug nastepujacych regul:
#do 85.528,00 podatek wynosi 18% podstawy minus 556,02 PLN,
#od 85.528,00 podatek wynosi 14.839,02 zl + 32% nadwyzki ponad 85.528,00.
#Przychod pobierz od uzytkownika w konsoli za pomoca funkcji input(). Nie podawaj do niej zadnego argumentu.

income = float(input())

if income <= 85528.0:
    calculated_tax = income * 0.18 - 556.02

    if calculated_tax < 0:
        calculated_tax = 0

    print(calculated_tax)
else:
    print(14839.02 + 0.32 * (income - 85528.0))