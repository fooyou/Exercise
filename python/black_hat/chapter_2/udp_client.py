#!/usr/bin/env python
# coding: utf-8
# @File Name: udp_client.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-28 10:03:11
# @Last Modified: 2018-03-28 10:03:07
# @Description:
import socket

target_host = '127.0.0.1'
target_port = 8088

# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
client.sendto(b'AABBCCDD', (target_host, target_port))

# 接收一些数据
data, addr = client.recvfrom(4096)

print(data, addr)
