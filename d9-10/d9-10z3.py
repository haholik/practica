import re
ip = input("Введите ip: ")
lizt_ip = re.split("[.]",ip)
z=int(0)
x=int(256)


for i in lizt_ip:
    if int(i) not in range(z, x):
        print(i)
        print("Неправильный IP-адрес")
        break
    elif len(lizt_ip) == 4 and re.split(ip, ".."):
        if int(lizt_ip[0]) in range(1, 223):
            print("unicast")
            break
        elif int(lizt_ip[0]) in range(224, 240):
            print("local broadcast")
            break
        elif ip == "255.255.255.255":
            print("unassigned")
            break
        else:
            print("unused")
