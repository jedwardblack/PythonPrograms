# Name: Joseph Black
# Assignment: hangman.py
# Apology: Sorry, I didn't have time to write in comments.


from random import *
from graphics import *

def display(word):
    s = " "
    return "Secret word: "+s.join(word)+"\n"

def game(guesses, word):
    winWidth = 400
    winHeight = 600
    win = GraphWin("Hangman", winWidth, winHeight)
    secretWordBox = Text(Point(winWidth/2, winHeight-60), "")
    secretWordBox.draw(win)
    guessesBox = Text(Point(winWidth/2, winHeight-80), "")
    guessesBox.draw(win)
    guessBox = Entry(Point(winWidth/2, winHeight-20), 2)
    prompt = "Please guess a letter in the box,\nthen click the window."
    guessPrompt = Text(Point(winWidth/2, winHeight-45), prompt)
    guessBox.draw(win)
    guessPrompt.draw(win)
    i = 0
    blankWord = blank(word)
    while i < guesses:
        imageName = "Gallows"+str(i)+".gif"
        image = Image(Point(winWidth/2, 225), imageName)
        image.draw(win)
        remainingGuesses = "You have "+str(guesses-i)+" guesses remaining."
        guessesBox.setText(remainingGuesses)
        blankWordCheck = blankWord*1
        wordDisplay = display(blankWord)
        secretWordBox.setText(wordDisplay)
        if didWin(blankWord, word):
            youWon = "Congratulations, You won!"
            guessPrompt.setText("Click to close.")
            guessBox.undraw()
            guessesBox.setText(youWon)
            win.getMouse()
            win.close()
            return True
        win.getMouse()
        guess = guessBox.getText()
        j = 0
        while j < len(word):
            if word[j] == guess:
                blankWord[j] = guess
                j += 1
            else:
                j += 1
        if blankWordCheck == blankWord:
            i += 1
        else:
            i += 0
    if i == guesses:
        imageName = "Gallows"+str(i)+".gif"
        image = Image(Point(winWidth/2, 225), imageName)
        image.draw(win)
        youWon = "Sorry, you lose. The secret word was "+str(word)+"."
        guessPrompt.setText("Click to close.")
        guessBox.undraw()
        guessesBox.setText(youWon)
        win.getMouse()
        win.close()
        return False

def didWin(word1, word2):
    s = ""
    word1Str = s.join(word1)
    if word1Str == word2:
        return True
    else:
        return False

def getWordList(file):
    infile = open(file, "r")
    linesList = infile.readlines()
    return linesList

def pickRandomWord(linesList):
    randomWord = linesList[randint(0, (len(linesList)-1))]
    word = randomWord[:-1]
    return word

def blank(word):
    blankWord = []
    for i in range(len(word)):
        blankWord += ["_"]
    return blankWord

def main():
    wordList = "wordlist.txt"
    numGuesses = 7
    linesList = getWordList(wordList)
    randomWord = pickRandomWord(linesList)
    game(numGuesses, randomWord)
    
main()
