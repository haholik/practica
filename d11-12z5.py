file = open("CAM_table.txt", mode="r+", encoding="utf-8")

for i, line in enumerate(file):
    if i > 3:
        print(line,end="")