#  1.16.Filtering_Sequence_Elements.py
#  
# 

from collections import namedtuple
subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = subscriber('joshua@example.com', '2014-10-26')
print(sub, '\nsub.addr', sub.addr, 'sub.joined', sub.joined)
print('len(sub):', len(sub))

addr, joined = sub
print(addr)
print(joined)

# 普通的写法
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# namedtuple写法

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 123, 123.45)

# 因为是元组，所以不能通过变量重新赋值
try:
    s.price = 100
except Exception as e:
    print(e)

# 但是其提供了_replace()方法来修改数值
s._replace(shares=75)
print(s)