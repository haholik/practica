import re
ip = input("Введите ip: ")
lizt_ip = re.split("[.]",ip)
if int(lizt_ip[0]) in range(1,223):
    print("unicast")
elif int(lizt_ip[0]) in range(224,240):
    print("local broadcast")
elif ip == "255.255.255.255":
    print("unassigned")
else:
    print("unused")

