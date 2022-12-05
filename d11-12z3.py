ignore = ["duplex", "alias", "configuration"]
file_sw = open("config_sw1.txt", mode="r+", encoding="utf-8")

for line in file_sw:
    if "!" not in line and ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
        print(line, end="")
    else:
        continue