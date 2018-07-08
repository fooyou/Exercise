#!/usr/bin/env python
# coding: utf-8
# @File Name: my_debugger_defines.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-27 17:03:54
# @Last Modified: 2018-03-27 17:03:49
# @Description:
from ctypes import *

# 映射微软类型到 ctypes 类型
WORD    = c_ushort
DWORD   = c_ulong
LPBYTE  = POINTER(c_ubyte)
LPTSTR  = POINTER(c_char)
HANDLE  = c_void_p

# 常量
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# Structures for CreateProcessA() function
class STARTUPINFO(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("lpTitle", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", DWORD),
        ("cbReserved2", DWORD),
        ("lpReserved2", DWORD),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE)
    ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]
