from tabulate import tabulate

file = open("CAM_table.txt", mode="r+", encoding="utf-8")
lizt = []
keyer = {}

for i, line in enumerate(file):  # присвоение каждой строке числа
    if "DYNAMIC" in line:
        lizt = str(line).split()  # разбить строки на слова в список
        lizt.insert(0, int(lizt[0]))  # в начало строки добавляется копия 1 слова из листа, но в виде числа
        lizt.remove(lizt[1])  # удаление числа в формате строки
        keyer[i] = lizt  # добавление в словарь строчку
        del keyer[i][2]  # удалить строку "DYNAMIC" из листа
print(tabulate(sorted(list(keyer.values()))))  # сортировка по значению и вывод числа в виде таблицы
