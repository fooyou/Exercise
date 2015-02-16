
import re

def RemoveNums(content):
    return re.sub(r'\d+', 'NUM', content)


content = '2008年4月20日，800名中学生聚集在地铁2号线里面，向1230名外国友人讲述1948的故事。'

print(content)

content = RemoveNums(content)

print(content)