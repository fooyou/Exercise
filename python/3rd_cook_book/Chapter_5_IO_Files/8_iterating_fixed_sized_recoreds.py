#!/usr/bin/env python
# coding: utf-8
# @File Name: iterating_fixed_sized_recoreds.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-05 15:02:26
# @Last Modified: 2016-02-05 15:02:12
# @Description:
'''
如何迭代读取一个指定读取大小的集合记录或者是 chunks。
'''

from functools import partial
RECORED_SIZE = 12
with open('./gzip_test.gz', 'rb') as f:
    records = iter(partial(f.read, RECORED_SIZE), b'')
    for r in records:
        print(r)

'''
上述代码按照指定大小迭代读取了一个record对象，直到文件结束。然而要注意如果文件大小不能被指定大小整除的话，最后读取的大小将小于指定的大小。

如上 iter() 函数的一个鲜为人知的特性是，如果你传给它的参数是个可调用的且是 sentinel 值，那么iter返回的迭代器将简单重复调用所提供的可调用函数知道它返回 sentinel（在这个值时迭代结束）。

sentinel 的意思是 “哨兵”

在这段代码中，`functools.partial` 创建了一个可调用的用来从文件中读取固定字节大小的数据函数。第二个参数 b'' 用来指定结束循环时返回的值（本例中即使当读取到文件结尾时返回 b''）。

最后这种方法更适合于读取二进制文件，文本文件的话还是逐行读取的好。
'''

