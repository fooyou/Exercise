# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2018-05-04 10:35:08
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2018-05-04 10:38:28
import os

cmd = "ps -eaf | grep sync_miaouser | grep -v grep | awk '{print $2}'"
ret = os.system(cmd)
print()
print(ret)