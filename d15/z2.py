infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


def create_network_map(filenames):
    for file in filenames:
        with open(file, mode="r+") as f:
            file = f.read()
            file = file.split()
            q = {}

    return q


if __name__ == "__main__":
    q = create_network_map(infiles)
    print(q)

