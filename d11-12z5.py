from tabulate import tabulate

keyer = {}
file = open("CAM_table.txt", mode="r+", encoding="utf-8")
for i, line in enumerate(file):
    if "DYNAMIC" in line:
        keyer[i] = str(line).split()
        del keyer[i][2]
        table = [keyer[i]]
        print(tabulate(table, tablefmt="github"))







