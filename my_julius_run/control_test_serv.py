# coding: utf-8
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 65535))
    while True:
        data, addr = s.recvfrom(1024)
        print("receive data: {}, addr: {}".format(data, addr))