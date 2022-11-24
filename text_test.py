import sys

ip_file_name = sys.argv[1]

ip_f = open(ip_file_name, "r")
ips = ip_f.readlines()
ips = [ip.rstrip("\n") for ip in ips]
ip_f.close

# ips = [ip.rstrip("\n") for ip in ips]

for ip in ips:
    if ip != '' and ip != '\n':
            ip = ip.rstrip()
    print(ip)

print(ips)