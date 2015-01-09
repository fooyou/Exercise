#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-26 15:13:49
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-27 16:02:38

import os, sys
import xlrd
import getopt
import barcode
from bs4 import BeautifulSoup

def modify_order_info(btsp, order_no, order_date):
    tag = btsp.find('h2', id='order_no')
    tag.string.replace_with('订单号：' + order_no)
    print(tag)

    tag = btsp.find('h2', id='order_date')
    tag.string.replace_with('订购日期：' + order_date)
    print(tag)

def modify_customer_info(btsp, name, tel):
    tag = btsp.find('p', id='receiver_name')
    tag.string.replace_with('收货人：' + name)
    print(tag)

    tag = btsp.find('p', id='receiver_tel')
    tag.string.replace_with('电话：' + tel)
    print(tag)

def modify_barcode(btsp, path):
    tag = btsp.find('img', id='img_barcode')
    tag['src'] = path
    print(tag)

def modify_receive_address(btsp, address):
    tag = btsp.find('p', id='receiver_address')
    tag.string.replace_with('收货人地址：' + address)
    print(tag)

def modify_intersaction(btsp):
    pass

def modify_detail_info(btsp, total_cost, total_num, kuaidi_cost, manu_cost, saved_money):
    tag = btsp.find('p', id='total_cost')
    tag.string.replace_with('商品总价：￥' + str(total_cost))
    print(tag)
    tag = btsp.find('p', id='total_num')
    tag.string.replace_with('商品总数：' + str(int(total_num)) + '  件')
    print(tag)
    tag = btsp.find('p', id='kuaidi_cost')
    tag.string.replace_with('配送费用：￥' + str(kuaidi_cost))
    print(tag)
    tag = btsp.find('p', id='manu_cost')
    tag.string.replace_with('支付手续费：￥' + str(manu_cost))
    print(tag)
    tag = btsp.find('p', id='saved_money')
    tag.string.replace_with('订单优惠：￥' + str(saved_money))
    print(tag)

def add_product(btsp, no, pid, name, guige, p_price, num, cost):
    tag = btsp.find('tbody', id='product_list')

    tr = btsp.new_tag('tr')
    no_td = btsp.new_tag('td', )
    no_td.string = str(no)
    no_td.attrs = {'height':'25'}
    tr.append(no_td)
    pid_td = btsp.new_tag('td')
    pid_td.string = str(pid)
    tr.append(pid_td)
    name_td = btsp.new_tag('td')
    name_td.string = name
    tr.append(name_td)
    guige_td = btsp.new_tag('td')
    guige_td.string = guige
    tr.append(guige_td)
    p_price_td = btsp.new_tag('td')
    p_price_td.string = '￥' + str(p_price)
    tr.append(p_price_td)
    num_td = btsp.new_tag('td')
    num_td.string = str(int(num))
    tr.append(num_td)
    cost_td = btsp.new_tag('td')
    cost_td.string = '￥' + str(cost)
    tr.append(cost_td)
    tag.append(tr)
    print(tr)

def generate_barcode(outdir, code):
    # 类型列表 ['code39', 'ean', 'ean13', 'ean8', 'gs1', 'gtin', 'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']
    # 生成SVG矢量条形码
    ean = barcode.get('ean13', code)
    with open(outdir + '/' + code + '.svg', 'wb') as f:
        ean.write(f)

def modify_next_page(btsp, url):
    print(url)
    tag = btsp.find('a', id='next_page')
    tag['href'] = url
    print(tag)

# [0'订单号', 1'交易号', 2'交易金额', 3'商品名称', 4'商品编号', 5'单价', 6'数量', 7'小计', 8'规格', 9'收款人姓名',
# 10'收款人地址', 11'收款人电话', 12'收款人手机', 13'收款人邮箱', 14'收货人姓名', 15'收货人省份', 16'收货人城市',
# 17'收货人地址', 18'收货人电话', 19'收货人手机', 20'收货人邮箱', 21'快递方式', 22'发货公司', 23'收据单', 24'邮费',
# 25'当前状态', 26'买家留言', 27'支付方式', 28'优惠券名称', 29'优惠券金额', 30'订单来源', 31'订单经手人',
# 32'下单时间', 33'付款时间', 34'发货时间']
def perform_order(same_order_list, samplehtml, outdir, next_html, index):
    try:
        code = str(int(same_order_list[0][0]))
        print('\n订单号：' + code, len(same_order_list), '件商品')
        generate_barcode(outdir, code)
        sampledata = ''
        with open(samplehtml, 'r', encoding='utf-8', errors='ignore') as f:
            sampledata = f.read()
        # print(sampledata)
        btsp = BeautifulSoup(sampledata, from_encoding='utf-8')
        # print(btsp)

        modify_next_page(btsp, next_html)
        modify_order_info(btsp, str(int(same_order_list[0][0])), same_order_list[0][32])
        modify_customer_info(btsp, same_order_list[0][14], same_order_list[0][18])
        modify_barcode(btsp, code + '.svg')
        modify_receive_address(btsp, same_order_list[0][17])

        no = 1
        total_num = 0
        for p in same_order_list:
            add_product(btsp, no, p[4], p[3], p[8], p[5], p[6], p[7])
            no += 1
            total_num += p[6]

        modify_detail_info(btsp, same_order_list[0][2], total_num, same_order_list[0][24], 0, same_order_list[0][29])

        if index == 0:
            outhtmlname = outdir + '/' + '0_' +  str(int(same_order_list[0][0])) + '.html'
        else:
            outhtmlname = outdir + '/' + str(int(same_order_list[0][0])) + '.html'
        with open(outhtmlname, 'w') as f:
            tag = btsp.find('meta')
            tag['content'] = 'text/html; charset=gb2312'
            content = str(btsp)
            content = content.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
            f.write(content)
    except Exception as e:
        print('Error perform:', same_order_list[0][0], e)
def main(xlspath, samplehtml, outdir):
    try:
        xlrd.Book.encoding = "utf-8"
        xls = xlrd.open_workbook(xlspath)
        sheets = xls.sheets()
        next_row = []   # 读取下一行以判断是否是相同订单号
        same_order_list = []    # 打印当前相同订单的产品
        all_order_list = []     # 存储所有的订单列表
        for sheet in sheets:
            # print(sheet.row_values(0))
            for i in range(1, sheet.nrows):        # 行数
                row = sheet.row_values(i)   # 获取一行信息
                # print(row)
                if i < sheet.nrows - 1:
                    next_row = sheet.row_values(i + 1)
                else:
                    next_row = ['none']

                if (row[0] == next_row[0]):
                    same_order_list.append(row)
                    continue
                elif len(same_order_list) == 0:
                    all_order_list.append([row])
                    # perform_order([row], samplehtml, outdir)
                else:
                    same_order_list.append(row)
                    all_order_list.append(same_order_list)
                    # perform_order(same_order_list, samplehtml, outdir)
                    same_order_list = []

            for i in range(len(all_order_list)):
                next_html = ''
                if i + 1 < len(all_order_list):
                    next_html = str(int(all_order_list[i + 1][0][0])) + '.html'
                perform_order(all_order_list[i], samplehtml, outdir, next_html, i)
            # for j in range(sheet.ncols):    # 列数

    except Exception as e:
        print('Error in open', xlspath, e)

if __name__ == "__main__":
    xlspath = ''
    outdir = ''
    samplehtml = 'sample.html'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-i: input file; -o: output_dir:")
        # print(opts, args)
        xlspath = ''
        outdir = ''
        for op, value in opts:
            if op == "-i":
                xlspath = value
            elif op == "-o":
                outdir = value

        print('Input file:', xlspath, 'output dir:', outdir)
    except Exception as e:
        print('Error in parameter:', e)

    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    main(xlspath, samplehtml, outdir)
    print('Done!!')

