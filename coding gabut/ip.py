import socket

hostname = input('masukkan url:')
ip_address = socket.gethostbyname(hostname)

print(f'Domain Name: {hostname}')
print(f'IP Address: {ip_address}')
