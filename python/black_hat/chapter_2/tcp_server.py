#!/usr/bin/env python
# coding: utf-8
# @File Name: tcp_server.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-28 10:03:47
# @Last Modified: 2018-03-28 10:03:43
# @Description:
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# 最大连接数设为 5
server.listen(5)

print('[*] Listening on %s:%d' % (bind_ip, bind_port))


def handle_clinet(client_socket):
    """
    客户端线程函数
    """
    # 打印出客户端发送得到内容
    request = client_socket.recv(1024)
    print('[*] Received: %s' % request)

    # 返回一个数据包
    client_socket.send(b'ACK!')
    client_socket.close()


while True:
    client, addr = server.accept()

    print('[*] Accepted connection from: %s:%d' % (addr[0], addr[1]))

    # 挂起客户端线程，处理传入的数据
    client_handle = threading.Thread(target=handle_clinet, args=(client,))
    client_handle.start()
