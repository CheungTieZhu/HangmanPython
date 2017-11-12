#controller
import random
from View.gameView import gameStart
from Model.word import wordArray as modelArray

def inputTheWord():
    theCategory = input("input the category:")
    theWordToGuess = input("the word you want your friends to guess:")
    for i in theWordToGuess:
        modelArray.append(i)
    randomTheWord(theWordToGuess,theCategory)

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




