# Poproś o podanie numeru tygodnia i na ekranie wypisz odpowiednią
# nazwę, np. dla
# 1 - Poniedziałek, dla
# 2 - Wtorek
# itd.
# !--- Z tego co rozumiem w zadaniu trzeba wybrać nie numer tygodnia a numer dnia w tygodniu?

print("Wybierz numer dnia tygodnia odpowiednio do listy")
print("1. Poniedziałek")
print("2. Wtorek")
print("3. Sroda")
print("4. Czwartek")
print("5. Piątek")
print("6. Sobota")
print("7. Niedziela")
choice = input("Wybieram: ")
if choice == "1":
    print("wybrałeś: Poniedziałek")
elif choice == "2":
    print("wybrałeś: Wtorek")
elif choice == "3":
    print("wybrałeś: Środę")
elif choice == "4":
    print("wybrałeś: Czwartek")
elif choice == "5":
    print("Wybrałeś: Piątek")
elif choice == "6":
    print("wybrałeś: Sobotę")
elif choice == "7":
    print("wybrałeś: Niedziele")
else:
    print("Prosze wpisać poprawny numer dnia tygodnia")