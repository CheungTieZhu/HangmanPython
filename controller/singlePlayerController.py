import random
import linecache
from View.gameView import gameStart
from Model.word import wordArray as modelArray


def selectCategory():
    categorySelect = input("select the category!")
    if categorySelect == "1":
        fileName = "animal.txt"
        theCategory = "animal"
        readFromFile(fileName,theCategory)
    elif categorySelect == "2":
        fileName = "celebrity.txt"
        theCategory = "celebrity"
        readFromFile(fileName,theCategory)
    elif categorySelect == "3":
        fileName = "animation.txt"
        theCategory = "animation"
        readFromFile(fileName,theCategory)
    elif categorySelect == "4":
        fileName = "fruit.txt"
        theCategory = "fruit"
        readFromFile(fileName,theCategory)
    else:
        print("wrong category")
        selectCategory()

def readFromFile(fileName,theCategory):
    file = open(fileName,"r")
    count = len(file.readlines())
    answerLine = random.randint(1,count)
    answer = linecache.getline(fileName,answerLine)
    answer = answer.strip()
    for i in answer:
        modelArray.append(i)
    randomTheWord(answer,theCategory)


def randomTheWord(word,theCategory):
    theWordArray = []
    EnglishWord = "abcdefghijklmnopqrstuvwxyz"
    #set the word into list
    for i in word:
        sameTime = 0
        for j in theWordArray:
            if i == j:
                sameTime += 1
        if sameTime == 0:
            theWordArray.append(i)
    lenght = len(theWordArray)
    #append random word into list
    while len(theWordArray) < lenght+10:
        sameTime = 0
        MaybeInsertWordIndex = random.randint(0,25)
        MaybeInsertWord=EnglishWord[MaybeInsertWordIndex]
        for i in theWordArray:
            if MaybeInsertWord == i:
                sameTime += 1
        if sameTime == 0:
            theWordArray.append(MaybeInsertWord)
    theDisplayArray = random.sample(theWordArray,len(theWordArray))

    gameStart(theCategory,theDisplayArray,word)
