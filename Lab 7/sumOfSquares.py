## Names: Josh Cox and Joseph Black
## Assignment: sumOfSquares.py
## Problem: Manipulating a list.

def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

def squareEach(nums):

    for i in range(len(nums)):
        nums[i] = nums[i]**2

def toNumbers(strList):

    for i in range(len(strList)):
        strList[i] = eval(strList[i])

def solve():
    fileName = input("What is the file name? ")
    infile = open(fileName, "r")
    contentsList = infile.readlines()
    toNumbers(contentsList)
    squareEach(contentsList)
    answer = sumList(contentsList)
    outFileName = "answer.txt"
    outfile = open(outFileName, "w")
    outfile.write(str(answer))
    outfile.close()
    infile.close()
    
        

def main():
    solve()
    print("data written")

main()
