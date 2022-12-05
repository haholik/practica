from tabulate import tabulate

file = open("CAM_table.txt", mode="r+", encoding="utf-8")
lizt = []
keyer = {}
tabs = []
inp = int(input("Enter VLAN number: "))

for i, line in enumerate(file):
    if "DYNAMIC" in line:
        lizt = str(line).split()
        lizt.insert(0, int(lizt[0]))
        lizt.remove(lizt[1])
        keyer[i] = lizt
        del keyer[i][2]
        if keyer[i][0] == inp:
            tabs.append(keyer[i])
print(tabulate(tabs))

