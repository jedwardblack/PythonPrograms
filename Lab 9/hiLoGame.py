#Name: Joseph Black & Hudson Jones
#hiLoGame.py

from random import randint

def main():
    i = 1
    integer = randint(1,100)
    guess = eval(input("Guess a number between 1 and 100: "))
    print(integer)
    while guess != integer and i < 7:
        if guess > integer:
            print("Your guess is too high!")
        if guess < integer:
            print("Your guess is too low!")
        i += 1
        guess = eval(input("Guess again!: "))

    if guess == integer:
        print("You gessed in " + str(i) + " guesses.")
        
