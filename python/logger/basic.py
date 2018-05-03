#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2018-05-03 09:54:03
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2018-05-03 18:00:49
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(os.path.basename(__file__))

# logger.setFormatter(formatter)
logger.info("Start reading database")
records = {"john": 55, "tom": 66}
logger.debug("Records : %s", records)
logger.info("Updating records ...")
logger.info("Finish updating records")

