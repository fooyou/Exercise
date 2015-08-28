#! /usr/bin/env python
# coding: utf-8

'''
按照一些对齐标准格式化文本，这种小接口都有，python真药逆天了。
'''

text = 'Hello World'
print(text.ljust(20)) 
# 'Hello World         '

print(text.rjust(20))
# '         Hello World'

print(text.center(20))
# '    Hello World     '

'''
还可以自己指定填充字符：
'''
print(text.center(20, '*'))
# ****Hello World*****

'''
format()函数也可以用来做对齐处理，可以使用<,>和^来对齐处理。
'''
print(format(text, '>20'))
# '         Hello World'

print(format(text, '<20'))
# 'Hello World         '

print(format(text, '^20'))
# '    Hello World     '

print(format(text, '*^20'))
# ****Hello World*****

'''
多个值的对齐操作也可以用format()实现。
'''
ret = '{:>10s}{:>10s}'.format('Hello', 'World')
print(ret)
# '     Hello     World'

'''
使用format()喊出的好处是，它适用于任何value
'''
x = 1.23456
print(format(x, '>10'))
# '   1.23456'

'''
旧的代码也使用这种格式
'''
print('%-20s' % text)
# 'Hello World         '

print('%20s' % text)
# '         Hello World' 

'''
但是不建议这么写代码，还是使用format()函数要好，它能干的活比这些多的多。
'''

