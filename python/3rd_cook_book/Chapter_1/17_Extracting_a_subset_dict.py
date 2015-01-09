#  1.16.Filtering_Sequence_Elements.py
#  
# 从字典中截取新字典

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 200 以上的组成新字典
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)

# 做一个科技股的字典
tech_names = ['AAPL', 'IBM', 'HPQ', 'MSFT']
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)

# 也可以用dict()函数来生成字典
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# 有多种写法来组成字典
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)
