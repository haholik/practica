file_sw = open("../config_sw1.txt", mode="r+", encoding="utf-8")

for line in file_sw:
    if "!" not in line:
        print(line, end="")
    else:
        continue
