#  write a program that for given number n prints
#  1 - n and next to if "FIZZ" if 3|n, "BUZZ" if 5|n
#  and "FIZZBUZZ" if 5|n and 3|n.

count_text = input("Do ilu mam wypisać?")
count = int(count_text)

i = 0
while i < count:
    n = i + 1
    print(n)
    if (n % 5 == 0 and n % 3 == 0):
        print("FIZZBUZZ")
    elif (n % 3 == 0):
        print("FIZZ")
    elif (n % 5 == 0):
        print("BUZZ")
    else:
        pass
    i += 1
