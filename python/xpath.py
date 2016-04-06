#!/usr/bin/env python
# coding: utf-8
# @File Name: xpath.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-03-15 13:03:46
# @Last Modified: 2016-03-15 13:03:26
# @Description:
from lxml import etree

htmlc = '''
<div class="combox relatedNews clearfix" id="relatedNews">
<div class="title">
<h3 class="tit">相关稿件</h3>
<span><a href="javascript:">总体规划</a></span><span><a href="javascript:">城市规划区</a></span></div>
<div class="content">

</div>
</div>
'''

doc = etree.HTML(htmlc)

relatedNews = doc.xpath('//div[@id="relatedNews"]/div[@class="title"]/span/a/text()')
for node in relatedNews:
    print(node)

