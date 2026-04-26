import socket

target = "scanme.nmap.org"

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))
    
    if result == 0:
        try:
            banner = s.recv(1024).decode()
        except TimeoutError:
            banner = 'banner is not availabe!'
        print(f'[+] {port} is open! {banner}')
    s.close()