#!/usr/bin/env python
# coding: utf-8
# @File Name: socket.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-28 09:03:02
# @Last Modified: 2018-03-28 10:03:49
# @Description:
import socket

# target_host = "www.baidu.com"
# target_port = 80
target_host = "0.0.0.0"
target_port = 9999

# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host, target_port))

# 发送一些数据
client.send(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# 接收一些数据
response = client.recv(4096)

print(response)
