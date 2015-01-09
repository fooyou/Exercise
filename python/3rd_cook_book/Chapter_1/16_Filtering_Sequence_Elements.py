#  1.16.Filtering_Sequence_Elements.py
#  
# Problem: You have data inside of a sequence, and need to extract values or
# reduce the sequence using some criteria.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 取mylist中的正数
positive_num = [n for n in mylist if n > 0]
print(positive_num)

# 取mylist中的负数
negative_num = [n for n in mylist if n < 0]
print(negative_num)

# Sometimes, the filtering criteria cannot be easily expressed in a list comprehension or
# generator expression. For example, suppose that the filtering process involves exception
# handling or some other complicated detail. For this, put the filtering code into its own
# function and use the built-in filter() function. For example:
# 使用list和filter处理更复杂的情况
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

iVals = list(filter(is_int, values))
print(iVals)

# 更深探索list压缩和generator表达式
import math
sqrt_mylist = [math.sqrt(n) for n in mylist if n > 0]
print(sqrt_mylist)

# 把mylist中的负值转为0，而保留正数怎么办？
positive_zero_num = [n if n > 0 else 0 for n in mylist]
print(positive_zero_num)

# 同理
negative_zero_num = [n if n < 0 else 0 for n in mylist]
print(negative_zero_num)

# itertools.compress()函数的应用，它用一个布尔选择器来选择序列里的值。
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
selector = list(compress(addresses, more5))
print(selector)

# The key here is to first create a sequence of Booleans that indicates which elements
# satisfy the desired condition. The compress() function then picks out the items corre‐
# sponding to True values.
# Like filter() , compress() normally returns an iterator. Thus, you need to use list()
# to turn the results into a list if desired.
