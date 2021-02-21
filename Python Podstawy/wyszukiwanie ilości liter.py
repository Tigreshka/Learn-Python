msg = input("Wpisz ciąg znaków: ")
# TODO - opic o co chodzi
letter = input("wpisz znak który chcesz znaleźć: ")

counter = 0
for c in msg:
    if c == letter:
        counter += 1

print("masz", counter, "wystąpeń")
