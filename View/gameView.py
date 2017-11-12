from Model.word import wordArray

hideWordArray = []
hintArray = []
wrongTime = 0
isWin = False
def gameStart(categoryInfo,displayArray,Answer):
    # os.system('cls') in windows
    global hintArray
    global correctTime
    print ("\n" * 40)
    print("Okay game start!!!")
    print("category is ",categoryInfo)
    hintArray = displayArray
    for i in displayArray:
        print(i,end=",")
    print('\n',len(Answer)*"_,")
    gameJudge()

def gameJudge():
    global hintArray
    print('\n')
    word = input("guess")
    match = False
    i = 0
    matchIndex = []
    for index in wordArray:
        if index == word:
            match = True
            matchIndex.append(i)
        i += 1
    try:
        hintArray.remove(word)
    except:
        print(word,"doesn't in the list")
        for i in hintArray:
            print(i, end=",")
        gameJudge()
    if match == True:
            showTheCorrect(matchIndex,word)
    else:
        showWrong()

def showTheCorrect(matchIndex,word):
    global hideWordArray
    blankNum = 0
    while len(hideWordArray) != len(wordArray):
        hideWordArray.append("_")
    for i in matchIndex:
        hideWordArray[i] = word
    for i in hideWordArray:
        print(i,end=",")
        if i == "_":
            blankNum += 1
    print('\n')
    for i in hintArray:
        print(i, end=",")
    if blankNum == 0:
        print('\n')
        print("Congraduation!You WIN!!!")
        global isWin
        isWin = True
    else:
        gameJudge()

def showWrong():
    global hintArray
    global wrongTime
    if isWin == False:
        if wrongTime == 0 :
            wrongTime += 1
            print('\n')
            for i in hintArray:
                print(i, end=",")
            print('\n')
            print("=====================")
            gameJudge()
        elif wrongTime == 1:
            wrongTime += 1
            print('\n')
            for i in hintArray:
                print(i, end=",")
            print('\n')
            print("=====================")
            print("          |          ")
            gameJudge()
        elif wrongTime == 2:
            print('\n')
            for i in hintArray:
                print(i, end=",")
            print('\n')
            print("=====================")
            print("          |          ")
            print("          O          ")
            wrongTime += 1
            gameJudge()
        elif wrongTime == 3:
            for i in hintArray:
                print(i, end=",")
            print('\n')
            print("=====================")
            print("          |          ")
            print("          O          ")
            print("         /|\         ")
            wrongTime += 1
            gameJudge()
        elif wrongTime == 4:
            for i in hintArray:
                print(i, end=",")
            print('\n')
            print("=====================")
            print("          |          ")
            print("          O          ")
            print("         /|\         ")
            print("         /           ")
            wrongTime += 1
            gameJudge()
        else:
            print("=====================")
            print("          |          ")
            print("          |          ")
            print("          |          ")
            print("          |          ")
            print("          O          ")
            print("         /|\         ")
            print("         / \         ")
            print("Game OVER!!!")
