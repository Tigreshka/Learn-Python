#Napisz program, ktory na podstawie zmiennych: wzrost - height (int) oraz waga - weight (float) sprawdza, czy dana osoba moze jechac kolejka gorska.
#W przypadku kiedy osoba jest wyzsza niz 150cm oraz nie przekracza wagi 180kg, program wypisze w konsoli "Zapnij pasy!", w przeciwnym wypadku wypisze w konsoli "Przykro mi, nie mozesz jecha?!".
#Dane pobierz od uzytkownika w konsoli za pomoca funkcji input(). Nie podawaj do niej zadnego argumentu.



height = int(input())
weight = float(input())

if height >= 150 and weight < 180:
    print("Zapnij pasy!")
else:
    print("Przykro mi, nie możesz jechać!")