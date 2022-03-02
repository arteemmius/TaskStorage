# Created by Samohin Artem
# Date 2018-10-31
# Task Description: http://www.hostedredmine.com/issues/781008


def listInput():
    inData = input()
    parseData = list()
    seqList = inData.split(" ")
    for index in range(0, len(seqList)):
        if seqList[index] == "":
            continue
        try:
            parseData.append(float(seqList[index]))
        except ValueError:
            print("Ошибка! Последовательность содержит не только" +
                  " числа!")
            exit(0)
    if len(parseData) > 100000:
        print("Количество элементов последовательности превышает 100000!")
        exit(0)
    return parseData

diffList = listInput()

print(len(set(diffList)))
