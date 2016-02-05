#!/usr/bin/env python
# coding: utf-8
# @File Name: 1_text_file_read_write.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-03 10:02:15
# @Last Modified: 2016-02-03 16:02:13
# @Description:
'''
文本文件的读写

open() 函数

读取整个文本到一个字符串里，（哦，shit，我竟然一直在这么用！）
'''

with open('/etc/passwd', 'rt') as f:
    data = f.read()
    print(data)

'''
迭代读取文件中的行，（这么用才是正解）
'''
with open('/etc/passwd', 'rt') as f:
    for idx, line in enumerate(f):
        print(idx, line, end='')


'''
正像读取一样，可使用 wt 来写文本
'''

with open('1.log', 'wt') as f:
    f.write('其实有句话老早就想对你说了，关你屁事！！！')

'''
重定向到 print 写
'''
with open('1_print.log', 'wt') as f:
    print('1. 床前明月光，', file=f)
    print('2. 疑是地上霜；', file=f)
    print('3. 举头望明月，', file=f)
    print('4. 低头思故乡。', file=f)

'''
好了，到了该讨论 encoding 文本编码的时间了，提到这个就不得不提到汉字，至今不明白为啥中国非得定义那么多的编码格式都是同一个字，又是GB2312，又是GB这，GB那，上学时有些猥琐的老师还笑谈中国汉字占用了那么多的Unicode空间，好像占了多大便宜，可是当了程序员没觉得这有什么便宜，给人感觉就是中文编码一片混乱，往往花费很大的力气去对应中文编码，这本应该不需要费力气的。难怪大名鼎鼎的 Sublime Text不支持中文的那些 encoding。

open() 函数提供了参数  encoding 来指定文本的编码类型，常见的有 ascii， latin-1， utf-8， utf-16。

ascii：     U+0000 -- U+007F
latin-1:    把 0～255映射到Unicode字符
Unicode:    U+0000 -- U+00FF

值得注意的是，latin-1 编码不会产生解码错误，即便是有非 latin-1 编码的情况也不会有错误。使用latin-1解码任何编码格式的文本，在保存回去都不会改变原来的数据


## 讨论

读写文本很直观，但有些事情要注意：

1. 注意文件的打开与关闭，open() 后，要关闭 close()，使用 with 关键字的除外
    f = open('/etc/passwd', 'rt')
    data = f.read()
    f.close()

2. newline的识别也就是所谓的 linux 回车和 windows回车符的区别，linux默认为 \n，windows上默认为 \r\n，默认情况下 Python 开启 “universal newline” 模式，能识别所有形式的 newline 符号，并在读取时统一转化为 \n，同样的在保存的时把 \n 转换成系统默认的 newline 符号。如果想取消这种行为，提供参数 newline='' 来取消这种功能，例如：

>>> # Newline translation enabled (the default)
>>> f = open('hello.txt', 'rt')
>>> f.read()
'hello world!\n'
>>> # Newline translation disabled
>>> g = open('hello.txt', 'rt', newline='')
>>> g.read()
'hello world!\r\n'
>>>


非常多的是时候，当你读取一个文本文件时，你会得到如下异常：

>>> f = open('sample.txt', 'rt', encoding='ascii')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
12: ordinal not in range(128)
>>>

这说明，你没有用正确的编码打开该文本，解决方法是找到合适的编码格式，或者替换错误，如下：

>>> # Replace bad chars with Unicode U+fffd replacement char
>>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
>>> f.read()
'Spicy Jalape?o!'
>>> # Ignore bad chars entirely
>>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
>>> g.read()
'Spicy Jalapeo!'
>>>
'''
