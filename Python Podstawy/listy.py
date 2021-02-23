print("1......................")
l = [1, 3, 5, 6, 7]
print(l[0])
print(l[:3])
print(l[2:52])


print("2......................")
l = [1, 3, 5, 6, 7]
k = [10, 20, 30]
l.append(k[0])
l.append(k[1])
l.append(k[2])
print(l)
print(id(l))
print(id(k))


print("3......................")
l = [1, 3, 5, 6, 7]
t = [10, 20, 30]
l.extend(t)
print(l)
print(id(l))
print(id(k))


print("4......................")
l = [1, 3, 5, 6, 7]
t = [10, 20, 30]
for i in "abc":
    l.append(i)
print(l)
print(id(l))
print(id(k))


print("5......................")
l = [1, 3, 5, 6, 7]
k = l
print(l)
print(k)
l[0] = 100
k[1] = -20
print("l = ", l)
print("k = ", k)
print(id(l))
print(id(k))


print("6......................")
l = [1, 3, 5, 6, 7]
k = []
for i in l:
    k.append(i)

k[0] = 100
print(l)
print(k)
print(id(l))
print(id(k))


print("7......................")
l = [1, 3, 5, 6, 7]
k = l.copy()
k[0] = 100
print(l)
print(k)
print(id(l))
print(id(k))


print("8......................")