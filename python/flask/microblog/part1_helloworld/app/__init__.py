#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-30 14:06:28
# @About __init__.py

import sys
import getopt

def get_opt():
    ''' Use 'getopt' module to get options from from user input. '''
    opts, args = getopt.getopt(sys.argv[1:], "i:o:h", ['input=', 'output=', 'help'])
    usage = 'Usage: python ' + __file__ + ' -i input.json -o output.json'
    in_file = 'in.json'
    out_file = 'out.json'
    
    for op, value in opts:
        if op == "-i":
            in_file = value
        elif op == "-o":
            out_file = value
        elif op == '-h':
            print(usage)
    
    return (in_file, out_file)

if __name__ == '__main__':
    # Get parameters.
    in_file, out_file = get_opt()