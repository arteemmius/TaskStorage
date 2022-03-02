# Created by Samohin Artem
# Date 2018-10-26
# Task Description: http://www.hostedredmine.com/issues/780965

import re
from collections import Counter

countWord = 0
for line in open('input.txt', 'r', encoding='utf8'):
    c = Counter(re.split(r'\s+', line))
    countWord = countWord + len(re.split(r'\s+', line)) - c['']

print(countWord)
