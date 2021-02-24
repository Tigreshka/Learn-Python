#Napisz program, ktory na podstawie zmiennych: kwota - amount (float) oraz liczby rat - number_of_installments (int),
#obliczac bedzie miesieczna kwote raty pozyczki i wypisywac ja w konsoli. Parametry posiadaja ograniczenia:
#
#kwota pozyczki musi miescic sie w przedziale od 100,00 zl do 10.000,00 zl,
#liczba rat musi miescic sie w przedziale od 6 do 48.
#W przypadku wykroczenia kwoty pozyczki poza akceptowalny przedzial, kwota pozyczki powinna byc ustawiona na 5.000,00 zl.
#W przypadku wykroczenia ilosci rat poza akceptowalny przedzial, ilosc rat powinna byc ustawiona na 36.
#
#Obliczona miesieczna rata powinna zawierac rowniez odsetki. Dla uproszczenia obliczen, przyjmij,
#ze do kwoty pozyczki doliczasz X procent w zaleznosci od ilosci rat:
#6-12 rat - 2,5%,
#13-24 rat - 5,0%,
#25-48 rat - 10,0%,
#a nastepnie obliczasz kwote raty na podstawie ilosci rat.
#Dane pobierz od uzytkownika w konsoli za pomoca funkcji input().

amount = float(input("Podaj kwotę pożyczki: "))
number_of_installments = int(input("podaj iłość rat: "))

if 100 <= amount <= 10000 and 6 <= number_of_installments <= 48:
    print("kredyt możliwy! ")
    if 6 ==  number_of_installments == 12:
        print(f"Kwota pozyczki {amount} zł, na {number_of_installments} rat")
        raty = float("{:.2f}".format(amount * 1.025 / number_of_installments))
        print(f"miesięczna rata pozyczi {raty} zł.")
    elif 13 == number_of_installments == 24:
        print(f"Kwota pozyczki {amount} zł, na {number_of_installments} rat")
        raty = float("{:.2f}".format(amount * 1.05 / number_of_installments))
        print(f"miesięczna rata pozyczi {raty} zł.")
    else:
        print(f"Kwota pozyczki {amount} zł, na {number_of_installments} rat")
        raty = float("{:.2f}".format(amount * 1.1 / number_of_installments))
        print(f"miesięczna rata pozyczi {raty} zł.")


else:
    amount = 5000
    number_of_installments = 36
    raty = float("{:.2f}".format(amount * 1.1 / number_of_installments))
    print(f"niestety nie możemy nadać taki kredyt, możemy zaproponować kredyt na, {amount} zł, na {number_of_installments} rat")
    print(f"Kwota rat wynosi {raty} na miesiąc")