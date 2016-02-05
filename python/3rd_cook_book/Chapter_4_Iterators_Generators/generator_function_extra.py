#!/usr/bin/env python
# coding: utf-8
# @File Name: generator_function_extra.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-01-28 11:01:24
# @Last Modified: 2016-01-28 19:01:01
# @Description:
'''
## 问题

定义一个生成器函数，让它对用户暴露额外的数据

## 方案

如果想要生成器暴露额外的数据给用户，可以简单的在类里实现 __iter__() 方法，例如：
'''

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()

'''
要使用这个类，把它当做正常的生成器函数就可以。然而既然创建了实例，就可以访问它的内部属性，比如 history 或者 clear() 方法。
'''

with open('/etc/passwd') as f:
    lines = linehistory(f)
    for line in lines:
        if 'joshua' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

'''
## 讨论

有了生成器（generator），就容易陷入在其内做任何事情的陷阱，如果生成器函数需要和其他模块有交互就会产生相当多的复杂代码（暴露属性，允许通过方法调用控制，等等）如果是这些需要，只需要使用类定义，正像上述代码一样。

在 __iter__() 函数中定义 generator 不会影响算法的编写。事实是它是类的一部分，这使得你更容易的提供供用户交互的属性或者方法。

下面的代码展示了这样写代码比 for 循环不好的一个潜质。
'''

f = open('/etc/passwd')
lines = linehistory(f)
next(lines)

'''
是的，有异常。
'''

