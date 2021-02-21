a = 1
b = 20.12345677
msg = "Zmienna a to %05d, a zmienna b to %.3f ." % (a, b)
msg_1 = "Zmienna a to {}, a zmienna b to {}".format(a, b)
msg_2 = f"Zmienna a to {a:05d}, a zmienna b to {b:.3f}"
print(msg_2)