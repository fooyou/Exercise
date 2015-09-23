#! /usr/bin/env python
# coding: utf-8

'''
如何替换HTML或者XML的标记呢？使用html.escape()函数来替换>或者<：
'''
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
# Elements are written as "<tag>text</tag>".
print(html.escape(s))
# Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

# 取消引用quote
print(html.escape(s, quote=False))
# Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

'''
如果想以ASCII发送并嵌入非ASCII内容，可以使用 errors='xmlcharrefreplace' 参数对应大量的I/O相关的函数，比如：
'''
s = 'Spicy 家拉牌呢'
asci = s.encode('ascii', errors='xmlcharrefreplace')
print(asci)
# b'Spicy &#23478;&#25289;&#29260;&#21602;'

