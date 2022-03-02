# Created by Samohin Artem
# Date 2018-10-26
# Task Description: http://www.hostedredmine.com/issues/780923

import re

phoneNum = list()
reg = re.compile('[^0-9]')
for line in open('input.txt', 'r', encoding='utf8'):
    line = line.replace('\n', '').split(' ')
    if len(reg.sub('', str(line))) == 7:
        phoneNum.append("495" + reg.sub('', str(line)))
    else:
        phoneNum.append(reg.sub('', str(line))[1:])

for i in range(1, len(phoneNum)):
    if reg.sub('', str(phoneNum[0]))[1:] == reg.sub('', str(phoneNum[i]))[1:]:
        print("YES")
    else:
        print("NO")
