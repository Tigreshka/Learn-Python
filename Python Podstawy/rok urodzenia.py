# Poproś o podanie roku urodzenia i wypisz na ekranie aktualny
# wiek, oraz czy osoba jest pełnoletnia.
# Aktualny tok zapisz jako wartość odpowiedniej zmiennej w Twoim programie

age = int(input("Podaj rok urodzenia: "))
current_year = 2020
current_age = current_year - age
print("Twój wiek to: ", current_age)
if current_age < 18:
    print("jesteś nie pełnoletni")
else:
    print("Jestem pełnoletni")
