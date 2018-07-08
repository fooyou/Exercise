#!/usr/bin/env python
# coding: utf-8
# @File Name: sshserver.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-04 13:04:55
# @Last Modified: 2018-04-08 17:04:20
# @Description:

import socket
import paramiko
import threading
import sys

host_key = paramiko.RSAKey(filename='test_rsa.key')


class Server(paramiko.ServerInterface):
    def _init_(self):
        self.event = threading.Event()
        return

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == 'joshua' and password == 'joshua':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


ssh_server =  sys.argv[1]
ssh_port = sys.argv[2]

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ssh_server, ssh_port))
    sock.listen(10)
    print("[+] Listening for connection ...")
    client, addr = sock.accept()
except Exception as e:
    print("[-] Listen failed: " + str(e))
    sys.exit(1)

print("[+] Got a connection!")


try:
    session = paramiko.Transport(client)
    session.add_server_key(host_key)
    server = Server()
    try:
        session.start_server(server=server)
    except Exception as e:
        print("[-] SSH negotiation failed.")

    chan = session.accept(20)
    print("[+] Authenticated!")
    print(chan.recv(1014))
    chan.send("Welcome to ssh")
    while True:
        try:
            command = input("Enter command: ").strip("\n")
            if command != "exit":
                chan.send(command)
                print(chan.recv(1024) + "\n")
            else:
                chan.send("exit")
                print("exiting")
                session.close()
                raise Exception("exit")
        except KeyboardInterrupt:
            session.close()
except Exception as e:
    print("[-] Caught exception: " + str(e))
    try:
        session.close()
    except:
        pass
    sys.exit(1)

