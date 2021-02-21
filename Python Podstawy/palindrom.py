msg = input("podaj napis : ")
msg_r = msg[::-1]
if msg == msg_r:
    print("Palinfrom")
else:
    print("Niestety")