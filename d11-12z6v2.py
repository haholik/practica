from tabulate import tabulate
file = open("CAM_table.txt", mode="r+", encoding="utf-8")
lizt = []
keyer = {}

for i, line in enumerate(file):
    if "DYNAMIC" in line:
        lizt = str(line).split()
        lizt.insert(0, int(lizt[0]))
        lizt.remove(lizt[1])
        keyer[i] = lizt
        del keyer[i][2]
print(tabulate(sorted(list(keyer.values()))))
