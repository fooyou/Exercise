#!/usr/bin/env python
# coding: utf-8
# @File Name: tofile.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-05-03 10:05:22
# @Last Modified: 2018-05-03 18:05:21
# @Description:

import os
import logging

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.INFO)

# 创建文件句柄
# handler = logging.FileHandler("log.log")
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# 创建日志格式
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 添加句柄到 logger
logger.addHandler(handler)

logger.info("Hello baby!")

