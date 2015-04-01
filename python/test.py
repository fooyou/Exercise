
import re

def RemoveNums(content):
    content = content.replace(' ', '')

    # 年份的处理
    content = re.sub(r'\d+年\d+月\d+日|\d+年\d+月|\d+月\d+日', '_DATE_', content)

    # 百分比，数字的处理
    content = re.sub(r'\d+.\d+%', '_PERCENT_', content)
    content = re.sub(r'\d+/\d+', '_PERCENT_', content)
    content = re.sub(r'\d+%', '_PERCENT_', content)
    content = re.sub(r'\d+', '_NUM_', content)
    return content

content = '2008年4月20日，800名中学生约2 / 3聚集在地铁2号线里面，98%~96.12435%向1230名外国友人讲述1948的故事。'

print(content)

content = RemoveNums(content)

print(content)