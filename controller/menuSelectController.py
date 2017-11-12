#Controller
from controller.multiplePlayController import inputTheWord
from View.categoryView import printCateGory

def menuSelect():
    theItemSelected = input("select:")
    if theItemSelected == "1":
        inputTheWord()
    elif theItemSelected == "2":
        printCateGory()
    elif theItemSelected == "3":
        print("Hangman is used often by teachers to practice spelling, vocabulary and just for fun.","\n"
              " The most popular way to play hangman games offline is to draw blank letters for the ","\n"
              "chosen word on a paper or on the blackboard and let the players guess the letters.","\n"
              " For each incorrect guess, another part of the man is drawn.","\n"
              " If the print is complete before the word is revealed the hangman game is lost and the character is hanged,","\n"
              " if the word is revealed before the execution the game is won.","\n")
        print("--------Hang Man---------")
        print("=========================")
        print("1.play game together!")
        print("2.play game single!")
        print("3.how to play the game ?")
        print("4.Exit")
        print("=========================")
        menuSelect()
    elif theItemSelected == "4":
        print("goodBye!!!")
    else:
        print("Please input the correct number!")


