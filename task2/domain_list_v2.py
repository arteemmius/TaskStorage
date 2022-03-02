# Created by Samohin Artem
# Date 2019-12-21
# Task Description: http://www.hostedredmine.com/issues/803176

import re

emailList = list(input().split(","))
domainList = list()
for i in range(0, len(emailList)):
    if re.compile(r'(\S+)([.]|[@])(\w+)[.](\w+)$').match(emailList[i].replace(" ", ""))\
            is not None:
        domainList = domainList + \
                     [str(x) for x in
                      reversed(re.search(r'([.]|[@])(\w+)[.](\w+)$',
                                         emailList[i].replace(" ", "")).group()[1:].split("."))]
    if re.compile(r'(\S+)[@](\w+)$').match(emailList[i].replace(" ", "")) is not None:
        domainList = domainList + \
                     [str(x) for x in
                      reversed(
                          re.search(r'[@](\w+)$',
                                    emailList[i].replace(" ", "")).group()[1:].split("."))]

for i in range(0, len(domainList)):
    if i % 2 == 1:
        print(domainList[i] + "." + domainList[i - 1])
    else:
        print(domainList[i])
