#! /usr/bin/env python
# coding: utf-8

'''
字符串的插值操作，可以使用format()函数
'''

s = '{name} has {n} messages.'
out = s.format(name='Joshua', n=31)
print(out)

'''
同时，如果要替换的值在变量中被发现，也可以使用format_map()和vars()方法的组合来完成功能，如下：
'''
name = 'Esther'
n = 30
out = s.format_map(vars())
print(out)
# 不过感觉这玩意很诡异啊～～～～

'''
vars()函数一个微妙的特点是，它也可以和实例Instance一起工作，比如：
'''
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Joshua', 31)
out = s.format_map(vars(a))
print(out)

'''
format()和format_map()函数的一个劣势是它不能很好的处理缺失值，比如：
'''
# s.format(name='Joshua')

# Traceback (most recent call last):
#    File "2.15.Interpolating-Variables-in-Strings.py", line 36, in <module>
# KeyError: 'n'

'''
可避免这个错误的一个方法是定义一个包含有__missing__()方法的字典类，如下：
'''
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n # 确保n被删除了
out = s.format_map(safesub(vars()))
print(out)
# Esther has {n} messages.
# 感觉又很无厘头。。。

'''
如果你频繁执行这几步代码，你可以把变量替换过程隐藏到一个被称为“frame hack”小工具函数中。如下：
'''
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

'''
然后可以这样操作：
'''
name = 'Joshua'
n = 31
print(sub('Hello {name}'))
# Hello Joshua
print(sub('You are {n} years old.'))
# You are 31 years old.
print(sub('Your favorite color is {color}'))
# Your favorite color is {color}

'''
由于Python缺失真正的变量替换，这些年出现了很多的解决方案，除了上面的还有以下的方法：
'''

'''
name = 'Esther'
n = 31
print('%(name) has %(n) messages' % vars())
'''

''' 还有使用字符串模板的 '''
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

'''
format_map()和format()是推荐使用的，使用format()函数的好处是能获得string格式化的所有功能。

本篇还阐释了一些有趣的高级功能。鲜为人知的mapping/classes的__missing__()方法可以处理丢失的值，在safesub类中被用来返回丢失的值的占位。

sys._getframe(1)：返回深度为1的堆栈，f_locals属性可得到本地变量。

'''
