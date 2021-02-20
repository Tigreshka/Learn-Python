age_text = input("Ile masz lat?")
age = int(age_text)

if age >= 18:
    answer = "- Masz {} lat. Jesteś pełnoletni.".format(age)
    print(answer)
    print("Sprzedano alkohol!")
elif age >= 16:
    answer = "- Masz {} lat. Jesteś prawie pełnoletni.".format(age)
    print(answer)
    print("Sprzedano piwo!")
elif age >= 14:
    answer = "- Masz {} lat. Kup lemoniadę.".format(age)
    print(answer)
    print("Sprzedano lemoniadę!")
else:
    answer = "- Masz {} lat. Jesteś niepełnoletni".format(age)
    print(answer)
    print("Nie sprzedano alkoholu.")


maxhello = 0
while age >= 18:
    maxhello = maxhello + 1
    if maxhello % 2 == 0:
        continue
    print("Hello")
    if maxhello >= 10:
        break

print("- Miłego dnia!")
