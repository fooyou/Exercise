#!/usr/bin/env python
#

from datetime import datetime
from datetime import timedelta

date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
date_object2 = datetime.strptime('Fri,25-Sep-2015 14:36:00 GMT', '%a,%d-%b-%Y %H:%M:%S %Z')

sn = datetime.now().strftime('%a,%d-%b-%Y %H:%M:%S %Z')

print(date_object)
print(date_object2)
print(sn)

date_cmp1 = datetime.strptime('25-Sep-2015 14:36:00 GMT', '%d-%b-%Y %H:%M:%S %Z')
date_cmp2 = datetime.strptime('25-Sep-2015 15:36:00 GMT', '%d-%b-%Y %H:%M:%S %Z')
print(date_cmp1 > date_cmp2)
print(date_cmp1 < date_cmp2)


def gen_date(start=datetime.strptime('2009-01-01', '%Y-%m-%d'), end=datetime.now()):
    while start + timedelta(days=1) <= end:
        print(start.strftime('%Y-%m-%d'))
        start = start + timedelta(days=1)

gen_date()
