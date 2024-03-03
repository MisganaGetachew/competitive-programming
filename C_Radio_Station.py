n, m = map(int, input().split())

name_ip = {}
for _ in range(n):
    name, ip = input().split()
    name_ip[ip] = name


for _ in range(m):
    command, ip = input().split()
    ip = list(ip)
    ip.pop()
    ip = "".join(ip)
    print(f"{command} {ip}; #{name_ip[ip]}")
