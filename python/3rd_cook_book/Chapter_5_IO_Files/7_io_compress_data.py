#!/usr/bin/env python
# coding: utf-8
# @File Name: 7_io_compress_data.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-05 10:02:26
# @Last Modified: 2016-02-05 14:02:24
# @Description:
'''
读写使用gzip或者bz2加密的数据文件。

使用python的内建的 gzip 和 bz2 模块
'''

import gzip

words_in_night_river = '''旅夜书怀
[作者] 杜甫

细草微风岸，危樯独夜舟。星垂平野阔，月涌大江流。
名岂文章著，官因老病休。飘飘何所似，天地一沙鸥。
'''

with gzip.open('gzip_test.gz', 'wt') as f:
    f.write(words_in_night_river)

with gzip.open('gzip_test.gz', 'rt') as f:
    test = f.read()
    print(test)

import bz2

with bz2.open('bz2_test.gz', 'wt') as f:
    f.write(words_in_night_river)

with bz2.open('bz2_test.gz', 'rt') as f:
    test = f.read()
    print(test)

'''
上述代码做的是文本的读写，使用unicode编解码，如果读写二进制数据，使用rb或者wb。

大多数时候，读写压缩文件非常直接明了，然而，要留心选择正确的文件模式。如果你没有指定一个模式，那么默认模式是二进制 b 模式。

gzip.open() 和 bz2.open() 都接受和内建 open() 函数相同的参数，包括 encoding、newline、errors 等等。

当写压缩文件时，可通过`compresslevel`指定压缩级别，例如：
'''

with gzip.open('gzip_test_compress_level.gz', 'wt', compresslevel=5) as f:
    f.write(words_in_night_river)

'''
这个参数的默认值是9，9是最高压缩级别，压缩比高，性能差。

最后关于 gzip.open(() 和 bz2.open() 的一个不太为人知的特性是，在二进制模式打开已存在的文件时，它们可以在最高层使用，比如下面的代码：
'''

f = open('gzip_test.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
    print(text)

'''
（点赞，这就是我为什么那么喜欢Python的原因，让你只专注在你关心的事情上，不用为不必要的事情烦心。）

这使得 gzip 和 bz2 模块可以和多种类文件对象一起协作，比如 sockets, pipes, 内存中的文件等。
'''
