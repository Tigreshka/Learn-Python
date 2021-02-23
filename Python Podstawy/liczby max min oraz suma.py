n = int(input("ile liczb podasz : "))
data = []
for i in range(n):
    l = int(input("Podaj liczbę:"))
    data.append(l)

print("podałęs :")
print(data)

sum_result = 0 #
for i in data: #
    sum_result += i # policz sume danych w tablicy

print("Suma: ", sum_result)

min_result = data[0]
for i in data[1:]:
    if i < min_result:
        min_result = i
print("minimalny : ", min_result)

max_result = data[0]
for i in data[1:]:
    if i > min_result:
        max_result = i
print("minimalny : ", max_result)

