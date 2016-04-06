#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhenyu@gmail.com
# @Date:   2016-03-14 17:03:33
# @About stringio.py

import json
import csv
from io import StringIO, BytesIO
from zipfile import ZipFile

content = '''
{
    "response": {
        "users": [{
            "sex": "m",
            "tags": [{
                "id": "2508917",
                "name": "\u738b\u7f8e\u73b2"
            }, {
                "id": "2508918",
                "name": "\u6e24\u6d77\u5927\u5b66"
            }, {
                "id": "2541430",
                "name": "\u6d3b\u52a8\uff1a\u7fa4\u53d1\u9001\u660e\u4fe1\u7247"
            }, {
                "id": "2600754",
                "name": "\u6210\u4ea4\u611f\u8c22\u4fe1-\u626b\u7801"
            }, {
                "id": "2677254",
                "name": "\u731c\u731c\u731c\u5355\u54c1\u5238"
            }, {
                "id": "2709164",
                "name": "\u601d\u793c\u4f17\u62a2"
            }, {
                "id": "2733226",
                "name": "\u5168\u5458\u5f00\u5e97"
            }, {
                "id": "2833122",
                "name": "2015\u5723\u8bde\u5730\u63a8"
            }],
            "union_id": "",
            "is_follow": true,
            "points": 93,
            "traded_num": 16,
            "traded_money": "23.92",
            "level_info": {},
            "user_id": "89393507",
            "weixin_openid": "oXG9xt27321DKCcL8SjjhY2C0Bvc",
            "nick": "\u5929\u60c5\uff5c\u4e3a\u601d\u793c",
            "avatar": "http:\/\/wx.qlogo.cn\/mmopen\/PiajxSqBRaEKQmQd30GYoZERic9TibebkLwSRh3hVkRGuCewGCNibow9KmkpySSBTy6u49dmKibRJoW2VC6K2uia07gw\/0",
            "follow_time": "2015-12-31 17:12:21",
            "province": "\u8fbd\u5b81",
            "city": "\u6c88\u9633"
        }, {
            "sex": "m",
            "tags": [],
            "union_id": "",
            "is_follow": false,
            "points": 90,
            "traded_num": 0,
            "traded_money": "0.00",
            "level_info": {},
            "user_id": "89825622",
            "weixin_openid": "oXG9xtzcf_OTo_Qh3WcVWUS_xIf8",
            "nick": "\u5c0f\u7fbd\u98de\u626c",
            "avatar": "http:\/\/wx.qlogo.cn\/mmopen\/VNMic85jx3X67HKBmA84TiblEeWDT4O9sGiaY9MCA4n0q2icKds7KmzONvUUTWLEiaAPbaPHsDgSaMQFfSTPWDhicZoJGFgia0ibHa7g\/0",
            "follow_time": "2014-12-12 17:15:17",
            "province": "\u5e7f\u897f",
            "city": "\u6765\u5bbe"
        }, {
            "sex": "m",
            "tags": [],
            "union_id": "",
            "is_follow": true,
            "points": 90,
            "traded_num": 0,
            "traded_money": "0.00",
            "level_info": {},
            "user_id": "89836959",
            "weixin_openid": "oXG9xt9ucHLxECsy_8ksIhR-aTPA",
            "nick": "\u5218\u5f3a",
            "avatar": "http:\/\/wx.qlogo.cn\/mmopen\/jpTSeXcRRc3oia6XY8GDd8ibqPFFE2NwvMFib4LYarw1vv2OiaicicbXDb8icuKMyOe3egovcOiczXu6mF7qHmgHlEqLicqPh4CRyzjrz\/0",
            "follow_time": "2014-12-12 17:33:33",
            "province": "\u8fbd\u5b81",
            "city": "\u6c88\u9633"
        }]
    }
}
'''

jsonobj = json.loads(content)

buf = StringIO()
fieldnames = ['sex', 'tags', 'union_id', 'is_follow', 'points', 'traded_num',
    'traded_money', 'level_info', 'user_id', 'weixin_openid', 'nick', 'avatar',
    'follow_time', 'province', 'city']
csvwriter = csv.DictWriter(buf, fieldnames=fieldnames)
csvwriter.writeheader()
for fans in jsonobj['response']['users']:
    csvwriter.writerow(fans)

buf.seek(0)

zbuf = BytesIO()
with ZipFile(zbuf, 'w') as f:
    f.writestr('hello.csv', buf.read())

zbuf.seek(0)

with open('hello.zip', 'wb') as f:
    f.write(zbuf.read())