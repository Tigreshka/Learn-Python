# Poprosić użytkownika o podanie roku oraz aktualnego miesiąca,
# a następnie ile miesięcy chcemy dodać.
# Wynik powinien wyświetlić nowy rok i miesiąc wynikający z odpowiedniego dodania.
# Przykładowo: rok 2020, miesiąc 10, dodajemy 3 miesiące to wynik 2021

#Version - 1
current_year = int(input("wpisz rok"))
current_months = int(input("wpisz miesiąc"))
#rach = (12 - current_months)
plus = int(input("Ile miesięcy mam dodać"))
years = int((current_months + plus) / 12)
print("Będzie rok: ", current_year + years)
month = int((current_months) + plus) - (years * 12)
print("Będzie miesiąć: ", month)

#Version - 2
year = int(input("Podaj rok: "))
month = int(input("Podaj miesiąc: "))
add_month = int(input("Ile miesięcy dodać: "))
temp_month = month+add_month
final_month = temp_month % 12
final_year = temp_month // 12
print("Rok:", year+final_year)
print("Miesciac:", final_month)
