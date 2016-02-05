#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2015-02-07 11:56:13
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-02-08 16:14:55
# 示例excel写操作，所用插件xlwt

import xlwt

# 新建Excel文件
excelfile = xlwt.Workbook()

# 新建一个sheet
table = excelfile.add_sheet('15_ab_01.json')

# 写入数据table.write(行，列，value)
table.write(0, 0, "1\"")

# 如果对一个单元格重复操作，需要这样：
table = excelfile.add_sheet('15_ab_02.json', cell_overwrite_ok=True)

# 写入数据table.write(行，列，value)
table.write(0, 0, 2)

# 保存文件
excelfile.save('demo.xls')
