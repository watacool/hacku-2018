# coding: utf-8
import socket
from datetime import datetime

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 65535))
    while True:
        data, addr = s.recvfrom(1024)
        output = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        output += "\nreceive data: {}, addr: {}\n".format(data, addr)
        print(output)
        with open("server.txt", mode='a') as f:
            f.write(output)