# Created by Samohin Artem
# Date 2018-10-31
# Task Description: http://www.hostedredmine.com/issues/780965

countWord = 0
tS = ""
for line in open('input.txt', 'r', encoding='utf8'):
    tS = tS + line
countWord = len(set(tS.split()))
print(countWord)
