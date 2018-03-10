import socket

def portscan(ipadr, maxnum):
    i=1
    while i<=maxnum:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        