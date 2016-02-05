#! /usr/bin/env python
# coding: utf-8

'''
对于一个字符串按指定规律分词，pattern.scanner()可以完成匹配分词。
'''

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner(text)

# 循环匹配
for i in range(11):
    out = scanner.match()
    print((out.lastgroup, out.group()))
# ('NAME', 'foo')

'''
上述功能可以写的更加简洁
'''
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

'''
可以看到上述输出结果中含有可能用不到的'WS'，可以不输出WS，代码如下：
'''
for tok in generate_tokens(master_pat, text):
    if tok.type != 'WS':
        print(tok)
