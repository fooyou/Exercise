#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Description: 
#   本脚本旨在转换考呀呀的除大题外的数据内容到excel中，方便数据导入。
# @Usage:
#   1. 

import requests
import time

def get_question(url, headers, delstr):
    result = requests.get(url, headers=headers)
    result = result.text
    result = result.replace(delstr, '')
    result = result[:len(result) - 1]
    return result

headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'user_id=185628; username=18640436501; PHPSESSID=4pqdmrcke1cv9g7u95i2vp7sj4; font-cursize=14px; pagesize=1; SID=4pqdmrcke1cv9g7u95i2vp7sj4; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1424001436; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424001546',
    # 'Cookie': 'user_id=185628; username=18640436501; font-cursize=14px; pagesize=1; PHPSESSID=krgtet76jlk43b05oe271tqq50; SID=krgtet76jlk43b05oe271tqq50; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1424001436,1424003659; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424003711',
    'Cookie': 'user_id=185628; username=18640436501; font-cursize=14px; pagesize=1; PHPSESSID=q77o3rk47k142p4h0nitfh01a3; SID=q77o3rk47k142p4h0nitfh01a3; p=6; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1423888423,1424093396; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424093396',
    'Host': 'www.kaoyaya.com',
    'Referer': 'http://www.kaoyaya.com/ksoft2/?f=pc&id=4327&p=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 第一章
#   URL: http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=2&order=2&tixingId=0&id=4336&isError=0&callback=jQuery110201557095842435956_1424001545406&_=1424001545408
#   'Cookie': 'user_id=185628; username=18640436501; PHPSESSID=4pqdmrcke1cv9g7u95i2vp7sj4; font-cursize=14px; pagesize=1; SID=4pqdmrcke1cv9g7u95i2vp7sj4; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1424001436; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424001546',
#   
# 第二章
#   URL: http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=1&order=1&tixingId=0&id=4337&isError=0&callback=jQuery110206358644084539264_1424003709876&_=1424003709877
#   'Cookie': 'user_id=185628; username=18640436501; font-cursize=14px; pagesize=1; PHPSESSID=krgtet76jlk43b05oe271tqq50; SID=krgtet76jlk43b05oe271tqq50; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1424001436,1424003659; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424003711',
#   
# 第三章
#   URL: http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=1&order=1&tixingId=0&id=4338&isError=0&callback=jQuery110209024331497494131_1424093395451&_=1424093395452
#   Cookie:user_id=185628; username=18640436501; font-cursize=14px; pagesize=1; PHPSESSID=q77o3rk47k142p4h0nitfh01a3; SID=q77o3rk47k142p4h0nitfh01a3; p=6; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1423888423,1424093396; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1424093396
try:
    with open('tikuch3.json', 'w+') as f:
        f.write('[')
        for i in range(329):
            url = 'http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=' + str(i + 1) + '&order=' + str(i + 1) + '&tixingId=0&id=4338&isError=0&callback=jQuery110209024331497494131_1424093395451&_=' + str(1424093395452 + i)
            # http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=1&order=1&tixingId=0&id=4337&isError=0&callback=jQuery110206358644084539264_1424003709876&_=1424003709877
            # http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=2&order=2&tixingId=0&id=4336&isError=0&callback=jQuery110201557095842435956_1424001545406&_=1424001545408
            try:
                result = get_question(url, headers, 'jQuery110209024331497494131_1424093395451(')
                print(i)
                f.write(result)
                f.write(',')
            except Exception as e:
                time.sleep(20)
                result = get_question(url, headers, 'jQuery110209024331497494131_1424093395451(')
                print(i)
                f.write(result)
                f.write(',')
                continue
        f.write(']')
except Exception as e:
    print(e)