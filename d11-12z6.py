import operator

from tabulate import tabulate

keyer = {}
sotr = []
file = open("CAM_table.txt", mode="r+", encoding="utf-8")
for i, line in enumerate(file):
    if "DYNAMIC" in line:
        keyer[i] = line.split()
        del keyer[i][2]
print(tabulate(sorted(list(keyer.values()))))








