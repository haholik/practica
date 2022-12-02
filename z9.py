work = input("Введите режим работы интерфейса (access/trunk):")
number = input("Введите тип и номер интерфейса: ")
interface = ""
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
    interface = input("Введите номер VLAN ")
    print(access_template)

elif work == "trunk":
    interface = input("Введите разрешенные VLANы ")
    print(trunk_template)
