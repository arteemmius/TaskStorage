# Created by Samohin Artem
# Date 2018-11-14
# Task Description: http://www.hostedredmine.com/issues/782531

import sys

countWord = 0
inText = ""
for line in open('input.txt', 'r', encoding='utf8'):
    inText = inText + line

wordList = list(inText.split())
dicList = {}
for i in range(0, len(wordList)):
    if dicList.get(wordList[i]) is None:
        addData = {wordList[i]: int(1)}
        dicList.update(addData)
    else:
        updData = {wordList[i]: int(dicList.get(wordList[i])) + int(1)}
        dicList.update(updData)

print(dicList)
