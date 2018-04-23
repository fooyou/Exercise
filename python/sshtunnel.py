#!/usr/bin/env python
# coding: utf-8
# @File Name: jumpserver.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-23 11:04:51
# @Last Modified: 2018-04-23 12:04:41
# @Description:
import sshtunnel
import MySQLdb

# ssh server
ssh_server = "101.201.56.80"
ssh_port = 5999
ssh_user = "liuchaozhen"
ssh_passwd = "VXx1lDKcPwGNKobg"
ssh_key = "/Users/joshua/lczai.pem"

# mysql server
mysql_host = "192.168.9.12"
mysql_user = "reader"
mysql_passwd = "miaodata"
mysql_db = "report"
mysql_port = 3306

# bind to local
local_host = "127.0.0.1"
local_port = 13306

with sshtunnel.SSHTunnelForwarder(
    (ssh_server, ssh_port),
    ssh_username=ssh_user,
    ssh_pkey=ssh_key,
    ssh_private_key_password=ssh_passwd,
    remote_bind_address=(mysql_host, mysql_port),
    local_bind_address=(local_host, local_port)) as tunnel:
    db = MySQLdb.connect(
            user=mysql_user,
            password=mysql_passwd,
            host=local_host,
            database=mysql_db,
            port=local_port)
    c = db.cursor()
    results = c.execute("SHOW tables;")
    print(results)
    for i in c.fetchall():
        print(i)
