#! /usr/bin/env python
# coding: utf-8

'''
使用内联函数join()来连接多个字符成一个字符串
'''
parts = ['九月', '三号', '北京', '天安门', '广场', '海陆空', '三军', '全民', '大阅兵']

print(' '.join(parts))
# 九月 三号 北京 天安门 广场 海陆空 三军 全民 大阅兵

print(','.join(parts))
# 九月,三号,北京,天安门,广场,海陆空,三军,全民,大阅兵

print(''.join(parts))
# 九月三号北京天安门广场海陆空三军全民大阅兵

'''
这么用也可以
'''

def yield_gen():
    yield '草泥马'
    yield '河蟹'
    yield '狗日的'
    yield '网络文学'

text = ''.join(yield_gen())
print(text)
# 草泥马河蟹狗日的网络文学

