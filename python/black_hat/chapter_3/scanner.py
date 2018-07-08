#!/usr/bin/env python
# coding: utf-8
# @File Name: scanner.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-20 11:04:51
# @Last Modified: 2018-04-20 18:04:02
# @Description:
import socket
import os
import struct
import threading
from netaddr import IPAddress, IPNetwork
from ctypes import *

# host to listen on
host = "10.0.20.164"

# subnet to target
subnet = "10.0.21.255/24"

# magic we'll check ICMP reponse for
magic_message = "PYTHONRULLS!"


def udp_sender(subnet, magic_message):
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for ip in IPNetwork(subnet):
        try:
            # print("sending -> %s" % ip)
            # sender.connect((ip, 8080))
            # sender.send(magic_message)
            # # sender.sendto(magic_message, (ip, 25))
            pass
        except:
            print("error   ->: %s" % ip)
            pass


class IP(Structure):
    _fields_ = [
        ("ihl",         c_ubyte, 4),
        ("version",     c_ubyte, 4),
        ("tos",         c_ubyte),
        ("len",         c_ushort),
        ("id",          c_ushort),
        ("offset",      c_ushort),
        ("ttl",         c_ubyte),
        ("protocol_num",c_ubyte),
        ("sum",         c_ushort),
        ("src",         c_uint),
        ("dst",         c_uint)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(Structure):
    _fields_ = [
        ("type",        c_ubyte),
        ("code",        c_ubyte),
        ("checksum",    c_ushort),
        ("unused",      c_ushort),
        ("next_hop_mtu",c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass


# create a raw socket and bind it to the public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))

# we want the IP headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if we're on Windows we need to send some ioctls
# to setup promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# start sending packets
t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
t.start()

try:
    while True:
        # read in a single packet
        raw_buf = sniffer.recvfrom(65565)[0]

        # create an IP header from the first 20 bytes of the buffer
        ip_header = IP(raw_buf[0:20])

        print("Protocol: %s %s -> %s" % (ip_header.protocol,
            ip_header.src_address,
            ip_header.dst_address))

        # if it's ICMP we want it
        if ip_header.protocol == "ICMP":
            # calculate where our ICMP packet starts
            offset = ip_header.ihl * 4
            buf = raw_buf[offset:offset + sizeof(ICMP)]

            # create out ICMP structure
            icmp_header = ICMP(buf)

            print(icmp_header.type, icmp_header.code)

            # now check for the TYPE3 and CODE 3 which indicates
            # a host is up but no port available to talk to
            if icmp_header.code == 3 and icmp_header.type == 3:
                # check to make sure we are receiving the response
                # that lands in our subset
                if IPAddress(ip_header.src_address) in IPNetwork(subnet):
                    # test for our magic message
                    if raw_buf[len(raw_buf) - len(magic_message):] == magic_message:
                        print("Host Up: %s" % ip_header.src_address)
# handle CTRL-C
except KeyboardInterrupt:
    # if we're on Windows turn off promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)



if __name__ == "__main__":
    udp_sender(subnet, magic_message)
