# Created by Samohin Artem
# Date 2018-11-14
# Task Description: http://www.hostedredmine.com/issues/782468


# Функция wordInput() служит для инициализации словаря Васи


def wordInput(dWord):
    inData = input()
    upperLetter = list()
    letterList = {}
    i = 0
    while i != int(inData):
        inWord = input()
        for j in range(0, len(inWord)):
            if inWord[j].isupper():
                letterList = {inWord[j]: j}
                upperLetter.append(letterList)
        addWord = {inWord: upperLetter.copy()}
        dWord.update(addWord)
        upperLetter.clear()
        i += 1


# Функция textInput() служит для инициализации текста Пети


def textInput(dWord):
    inText = input()
    wordList = list()
    upperLetter = list()
    wordList = inText.split(" ")
    letterList = {}
    for i in range(0, len(wordList)):
        for j in range(0, len(wordList[i])):
            if wordList[i][j].isupper():
                letterList = {wordList[i][j]: j}
                upperLetter.append(letterList)
        addWord = {wordList[i]: upperLetter.copy()}
        dWord.update(addWord)
        upperLetter.clear()


wordDictionary = {}
textDictionary = {}
errorCounter = 0

wordInput(wordDictionary)
textInput(textDictionary)

errorCheck = True
for keyText in textDictionary:
    for keyWord in wordDictionary:
        if keyText.lower() == keyWord.lower() and len(textDictionary.get(keyText)) == 1:
            if textDictionary.get(keyText)[0] in wordDictionary.get(keyWord):
                pass
            else:
                errorCheck = False
        elif len(textDictionary.get(keyText)) == 1:
            pass
        else:
            errorCheck = False
    if not errorCheck:
        errorCounter += 1
        errorCheck = True

print(errorCounter)
