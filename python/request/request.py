#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-02-14 12:44:58
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-02-14 13:36:38
import requests

headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Connection': 'keep-alive',
    'Cookie': 'user_id=185628; username=18640436501; PHPSESSID=ghu79200qma7vqrmd4s0s7b1k4; SID=ghu79200qma7vqrmd4s0s7b1k4; font-cursize=14px; pagesize=1; curId=4336; Hm_lvt_f21c6444017c25a193c94830de3e7136=1423888423; Hm_lpvt_f21c6444017c25a193c94830de3e7136=1423888451',
    'Host': 'www.kaoyaya.com',
    'Referer': 'http://www.kaoyaya.com/ksoft2/?f=pc&id=4327&p=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.95 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

with open('ab_excecise_1089.json', 'w') as f:
    f.write('[')
    for i in range(1089):
        url = 'http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=' + str(i + 1) + '&order=' + str(i + 1) + '&tixingId=0&id=4336&isError=0&callback=jQuery110208137465096078813_1423888450512&_=' + str(1423888450513 + i)
        r = requests.get(
            url,
            headers = headers
        )

        jsons = r.text.replace('jQuery110208137465096078813_1423888450512(', '')
        jsons = jsons[:(len(jsons) - 1)]
        f.write(jsons)
        f.write(',')
        print(jsons)
    f.write(']')
    # print()

# http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=3&order=3&tixingId=0&id=4336&isError=0&callback=jQuery110208137465096078813_1423888450512&_=1423888450515
# http://www.kaoyaya.com/ksoft2/getChapQuestions.php?perSize=1&page=2&order=2&tixingId=0&id=4336&isError=0&callback=jQuery110208137465096078813_1423888450512&_=1423888450514