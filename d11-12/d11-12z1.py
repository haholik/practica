file_sw = open("../ospf.txt", mode="r+", encoding="utf-8")

suff = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound", "Interface"]
lizt = file_sw.readline().split()

print(f"\t {suff[0]} \t {lizt[1]} ", end="")
print(f"\n\t {suff[1]} \t {lizt[2]}", end="")
print(f"\n\t {suff[2]} \t {lizt[4]}", end="")
print(f"\n\t {suff[3]} \t {lizt[5]}", end="")
print(f"\n\t {suff[4]} \t {lizt[6]}", end="")
print(f"\n {suff[-1]}", end="")



