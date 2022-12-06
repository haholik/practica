
inp = input("Введите имя устройства: ")

slovar = dict()
slovar["r1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}
slovar["r2"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4', 'ip': '10.255.0.2'}
slovar["sw1"] = {"location": "21 New Globe Walk","vendor": "Cisco",
                 "model": "3850","ios": "3.6.XE","ip": "10.255.0.101",
                 "vlans": "10,20,30","routing": True}

par = input(f"Введите имя параметра: {slovar.get(inp).keys()} ")

for items in slovar.get("sw1").keys():
    if inp.__contains__("r1"):
        if items in par:
            print(slovar["r1"][items])
            break
    elif inp.__contains__("r2"):
        if items in par:
            print(slovar["r2"][items])
            break
    elif inp.__contains__("sw1"):
        if items in par:
            print(slovar["sw1"][items])
            break



