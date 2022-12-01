
inp = input("Введите имя устройства: ")

slovar = dict() #словарь
slovar["r1"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}
slovar["r2"] = {'location': '21 New Globe Walk', 'vendor': 'Cisco',
                'model': '4451', 'ios': '15.4', 'ip': '10.255.0.2'}
slovar["sw1"] = {"location": "21 New Globe Walk","vendor": "Cisco",
                 "model": "3850","ios": "3.6.XE","ip": "10.255.0.101",
                 "vlans": "10,20,30","routing": True} #создание словаря r1 r2 sw2, внутри которых ещё словари со значениями

par = input(f"Введите имя параметра: {slovar.get(inp).keys()} ") #из словаря по ключ-значению inp получить ключи ip,vendor и т.д
if par.lower() not in slovar.get("sw1").keys(): # если введённого параметра нету в словаре sw1 с ключами с переводом в нижний регистр
    print("Такого значения нету")
else:
    for items in slovar.get("sw1").keys(): #items будет получать ключи из словаря
        if inp.__contains__("r1"):         #если переменная inp содержит r1
            if items == par.lower():            #если items содержит тоже самое что и par
                print(slovar["r1"][items]) #вывод из словаря по ключу r1 введенного значения пользователем
                break
        elif inp.__contains__("r2"):
            if items == par.lower():
                print(slovar["r2"][items])
                break
        elif inp.__contains__("sw1"):
            if items == par.lower():
                print(slovar["sw1"][items])
                break



