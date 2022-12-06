lizt = []
while True:
    inp = input("Введите MAC аддрес в формате: XXXX:XXXX:XXXX:XXXX: ")
    lizt.append(inp.replace(":","."))
    if inp != "exit":
        print(lizt)
    elif inp == "exit":
        lizt.remove("exit")
        print(lizt)
        break