# Name: Joseph Black
# Assignment: noDuplicates.py

from random import *

def removeDuplicates(list):

    list.sort()
    i = 0
    while i < len(list)-1:
        count = list.count(list[i])
        if count == 1:
            i += 1
        else:
            for j in range(count-1):
                list.remove(list[i])
    

def main():

    listWithDuplicates = []
    for i in range(randint(5, 20)):
        num = randint(1, 10)
        for j in range(randint(1, 3)):
            listWithDuplicates.append(num)

    print(listWithDuplicates)
    removeDuplicates(listWithDuplicates)
    print(listWithDuplicates)

    
main()
