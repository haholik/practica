import subprocess

ip_lists = ['192.168.1.1', '192.168.1.100', '8.8.8.8', '1.1.1.1']


def ping_ip_addresses(ip):
    for i in ip:
        if subprocess.run("ping" + " i").returncode == 0:
            print(i + " Пингуется!")
        else:
            print(i + " Не пингуется")

ping_ip_addresses(ip_lists)