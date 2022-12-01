from collections import defaultdict

inp = input("Введите имя устройства: ")

slovar = dict()
slovar["r1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.1'}
slovar["r2"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.2'}
slovar["sw1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                 'model': '4451', 'ios': '15.4 ,→', 'ip': '10.255.0.3'}

if inp.__contains__("r1"):
    print(slovar["r1"])
elif inp.__contains__("r2"):
    print(slovar["r2"])
elif inp.__contains__("sw1"):
    print(slovar["sw1"])
