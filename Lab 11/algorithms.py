# Name: Joseph Black
# Asignment: algorithms.py
# Search Observations:  We can clearly see the advantage of a binary search
#       in the worst-case scenario with a large list. Though the best-case
#       scenario runs 5 times slower on the large list, the amount
#       of time is so infinitesimal, it is negligible.
# Sort Observations:    Wow. That was embarassing. My sort algorithm took
#       over 16 seconds and Python's took .006s. We should analyze Python's
#       sort algorithm in class.

def readData(filename):

    infile = open(filename, "r")
    linesList = infile.readlines()
    dataList = []
    for line in linesList:
        line = line.split()
        for num in line:
            num = eval(num)
            dataList.append(num)         
    return dataList

def isInLinear(searchVal, values):
    i = 0
    while searchVal != values[i] and i < len(values)-1:
        i += 1
    if searchVal == values[i]:
        return True
    if i == len(values):
        return False

def isInBinary(searchVal, values):
    low = 0
    high = len(values)-1
    pos = -1
    while low <= high and pos == -1:
        mid = int((low+high)/2)
        if searchVal == values[mid]:
            pos = mid
        elif searchVal < values[mid]:
            high = mid-1
        else:
            low = mid+1
    if pos == -1:
        return False
    else:
        return True

def insertionSort(values):
    i = 1
    for i in range(len(values)):
        minVal = values[i]
        j = i-1
        while j >= 0 and minVal < values[j]:
            values[j+1] = values[j]
            j = j-1
        values[j+1] = minVal
    return values


    
def main():

    file = "dataSorted.txt"
    dataList = readData(file)
    unSortedList = [4, 2, 3, 1, 5]
    sortedList = insertionSort(unSortedList)
    print(sortedList)

main()
    
