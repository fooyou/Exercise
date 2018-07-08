#!/usr/bin/env python
# coding: utf-8
# @File Name: bh_sshcmd.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-04 13:04:24
# @Last Modified: 2018-04-04 13:04:47
# @Description:
#   使用 paramiko 完成 ssh 命令的功能
import threading
import paramiko
import subprocess


def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # client.load_host_keys('~/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return


if __name__ == '__main__':
    ssh_command('10.0.11.206', 'joshua', 'joshua', 'id')
