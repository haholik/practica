lizt = []
while True:
    inp = input("Введите MAC аддрес в формате: XXX:XXX:XXX:XXX: ")
    lizt.append(inp.replace(":","."))
    if inp != "exit":
        print(lizt)
    elif inp == "exit":
        lizt.remove("exit")
        print(lizt)
        break