# Created by Samohin Artem
# Date 2018-10-26
# Task Description: http://www.hostedredmine.com/issues/780944


def setBias(firstPoint, secondPoint):
    if int(firstPoint) < int(secondPoint):
        biasValue = 1
    else:
        biasValue = -1
    return biasValue


def initArray():
    parseData = list()
    inData = input()
    myList = inData.split(" ")
    for index in range(0, len(myList)):
        try:
            parseData.append(int(myList[index]))
        except ValueError:
            print("Неверный ввод! Последовательность содержит не только числа")
            exit(0)
    return parseData


stopPoints = initArray()

firstStop = set()
for i in range(stopPoints[0], stopPoints[1] + setBias(stopPoints[0], stopPoints[1]),
               setBias(stopPoints[0], stopPoints[1])):
    firstStop.add(i)

secondStop = set()
for j in range(stopPoints[2], stopPoints[3] + setBias(stopPoints[2], stopPoints[3]),
               setBias(stopPoints[2], stopPoints[3])):
    secondStop.add(j)

print(len(firstStop.intersection(secondStop)))
