
work = input("Введите режим работы интерфейса (access/trunk):")
number = input("Введите тип и номер интерфейса: ")
interface = input("Введите номер влан(ов): ")

access_template = [
"switchport mode access", "switchport access vlan {}",
"switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"
]
trunk_template = [
"switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"
]

if work == "access":
    print(access_template)
elif work == "tunk":
    print(trunk_template)
else:
    print("ERROR")

