#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @Date:   2016-03-31 09:20:40
# @About drop.py

import requests
import random
from datetime import datetime
from datetime import timedelta

s = requests.Session()

url = "http://10.10.109.203:8080/DailyReport/Report/Controller.jsp"

def login():
    headers = {
        "Referer": "http://10.10.109.203:8080/DailyReport/Report/Login.jsp",
        "Origin": "http://10.10.109.203:8080",
    }

    form_data = {
        "userAction": "Login_Check",
        "LoginName": "liuchaozhen",
        "LoginPass": "liuSY*&201601",
        "x": 11,
        "y": 8
    }

    r = s.post(url, headers=headers, data=form_data)

def dailysubmit(data):
    headers = {
        "Referer": url,
        "Origin": "http://10.10.109.203:8080",
    }
    s.post(url, headers=headers, data=data)

def gen_date(begin=datetime.strptime(   # 本月 1 号开始
            datetime.now().strftime('%Y/%m/') + '01', '%Y/%m/%d' 
        ),
        end=datetime.now(),             # 至今天结束
        no_weekend=True):               # 不要周末
    '''
    产生指定时间段的日期。格式“2016/03/02”，默认产生当前月的日期
    '''

    # # 指定时间段
    # begin = datetime.strptime('2016-05-01', '%Y-%m-%d')
    # end   = datetime.strptime('2016-05-31', '%Y-%m-%d')
    # #
    
    itr = begin
    while itr < end:
        if no_weekend:
            if itr.strftime('%w') != '0' and itr.strftime('%w') != '6':
                yield itr.strftime('%Y/%m/%d')
        else:
            yield itr.strftime('%Y/%m/%d')
        itr = itr + timedelta(days=1)

if __name__ == '__main__':
    login()
    form_data = {
        "userAction": "ReportWriteCheck",
        "tempovertime": 0,
        "time": "2016/03/30",
        "reportDate": "2016/03/30",
        "reportDuty": "Textrank 提取关键词论文论证".encode('gbk'),
        "reportWorkhour": 8,
        "reportOverTime": 0,
        "reportProjectName": 2115,
        "reportModule": 12291,
        "reportMilestone": 8448,
        "reportGroup": 1,
        "reportWorktype": 5,    # 1: 需求, 5: 编码
        "reportMemo": ""
    }

    tasks = [
        '快速 simhash 专利交底书编写',
        'LDA 关键字提取专利交底书编写',
        'LDA 文章自动摘要专利交底书编写',
        'LDA 关键字提取的实现及实验',
        'LDA 文章自动摘要的实现及实验'
    ]

    for day in gen_date():
        r = random.randint(0, len(tasks) - 1)
        form_data["reportDuty"] = tasks[r].encode('gbk')    # 需要转码为 GBK
        r = random.randint(0, 1)
        form_data["reportWorktype"] = 1 if r == 0 else 5
        form_data["time"] = datetime.now().strftime('%Y/%m/%d')
        form_data["reportDate"] = day
        dailysubmit(form_data)
        print(form_data['reportDate'], 'done')


