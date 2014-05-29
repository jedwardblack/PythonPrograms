## Name: Josh Cox and Joseph Black
## Program: sumFunctions.py
## Problem: Sum and cube of n natural numbers.

def sumN(n):
    total = 0
    for i in range(n):
        total += 1 + i
    return total

def sumNCubes(n):
    total = 0
    for i in range(n):
        total += (1 + i) ** 3
    return total

def main():
    numNatural = eval(input("How many natural numbers for n? "))
    answer1 = sumN(numNatural)
    answer2 = sumNCubes(numNatural)
    print(answer1)
    print(answer2)

main()
