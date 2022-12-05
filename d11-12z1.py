import re
filetxt = open("ospf.txt", mode="r+", encoding="utf-8")
lizt = []
for line in filetxt:
    lizt.append(line.split())
print("\tPrefix", lizt[0][1])
print("\tAD/Metric", lizt[0][2])
print("\tNext-Hop", lizt[0][4])
print("\tLast update", lizt[0][5])
print("\tOutbound", lizt[0][6])
print("Interface")

filetxt.close()