import re

get_ip = input("Введите ip в формате xxx.xxx.xxx.xxx/port")
lizt = re.split("[/.]", get_ip)

print("Network: \n", lizt[0],lizt[1],lizt[2],lizt[3])
print(bin(int(lizt[0])).replace("0b",""),bin(int(lizt[1])).replace("0b",""),
      bin(int(lizt[2])).replace("0b",""),bin(int(lizt[3])).replace("0b",""))
print("Mask: \n", lizt[-1])
print("1" * 28 + "0" * 4)