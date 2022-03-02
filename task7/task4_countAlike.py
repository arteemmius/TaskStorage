# Created by Samohin Artem
# Date 2018-10-26
# Task Description: http://www.hostedredmine.com/issues/780986


def listInput():
    inData = input()
    parseData = list()
    seqList = inData.split(" ")
    for index in range(0, len(seqList)):
        try:
            if seqList[index] == " ":
                print("SPACE!!!")
                continue
            parseData.append(int(seqList[index]))
        except ValueError:
            print("Ошибка! Последовательность содержит не только" +
                  " целые положительные числа!")
            exit(0)
    return parseData


firstList = listInput()
secondList = listInput()

print(' '.join(str(e) for e in set(firstList) & set(secondList)))
