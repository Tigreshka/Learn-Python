#1) Dolar
#2) Euro
#3) Funt
#4) koniec
# co wybierasz?
# wybraełeś Euro

print("1) Euro")
print("2) Dolar")
print("3) Funt")
print("4) Koniec")

choice = int(input("Co wybierasz"))

if choice == 1:
    print("Wybrałeś Euro")
else:
    if choice == 2:
        print("Wybrałeś Dolar")
    else:
        if choice == 3:
            print("Wybrałeś Funt")
        else:
            print("Ok, nie to nie")


#Version 2:
print("1) Euro")
print("2) Dolar")
print("3) Funt")
print("4) Koniec")

choice = int(input("Co wybierasz"))
if choice == "1":
    print("Wybrałęś Euro")

elif choice == 2:
    print("Wybrałeś dolar")

elif choice == 3:
    print("Wybrałeś Funt")

else:
    print("nie to nie")