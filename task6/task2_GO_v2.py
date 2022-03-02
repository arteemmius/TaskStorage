# Created by Samohin Artem
# Date 2018-10-24
# Task Description: http://www.hostedredmine.com/issues/779631


# Функция listInput() служит для ввода и проверки входных данных

def listInput():
    inData = input()
    parseData = list()
    seqList = inData.split(" ")
    for index in range(0, len(seqList)):
        try:
            parseData.append(int(seqList[index]))
            if parseData[index] > 109:
                raise ValueError
        except ValueError:
            print("Ошибка! Последовательность содержит не только" +
                  " целые положительные числа не превышающие 109!")
            exit(0)
    return parseData


# Функция valueInput() служит для проверки входных данных
def valueInput():
    inData = input()
    if inData.isdigit():
        parseData = int(inData)
        if parseData <= 100000 and parseData >= 1:
            return parseData
    print("Недопустимый ввод! " + "'" + inData +
          "'" + " не является целым положительным числом от 1 до 100000!")
    return exit(0)


pCount = valueInput()
pList = listInput()
if pCount != len(pList):
    print("Неверный размер введенной последовательности!")
    exit(0)
bCount = valueInput()
bList = listInput()
if bCount != len(bList):
    print("Неверный размер введенной последовательности!")
    exit(0)

myList = list()
for i in range(0, len(pList)):
    minDif = abs(pList[0] - bList[0])
    for j in range(0, len(bList)):
        if abs(pList[i] - bList[j]) <= minDif:
            minDif = abs(pList[i] - bList[j])
            difIndex = j + 1
    myList.append(difIndex)
print(" ".join(str(x) for x in myList))
