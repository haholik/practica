
inp = input("Введите имя устройства: ")
par = input("Введите имя параметра: ")

slovar = dict()
slovar["r1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.1'}
slovar["r2"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.2'}
slovar["sw1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                 'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.3'}

for items in slovar.get("r1").keys():
    if inp.__contains__("r1"):
        if items in par:
            print(slovar["r1"][items])
    elif inp.__contains__("r2"):
        if items in par:
            print(slovar["r2"][items])
    elif inp.__contains__("sw1"):
        if items in par:
            print(slovar["sw1"][items])

