ignore = ["duplex", "alias", "configuration"]
file_sw = open("../config_sw1.txt", mode="r+", encoding="utf-8")
file_wr = open("../config_wr1.txt", mode="w", encoding="utf-8")

for line in file_sw:
    if "!" not in line and ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
        file_wr.write(line)
    else:
        continue
file_sw.close()
file_wr.close()