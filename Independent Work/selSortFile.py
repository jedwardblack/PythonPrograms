

def listSwap(someList, a, b):

    temp = someList[a]
    someList[a] = someList[b]
    someList[b] = temp

def selSort(values):

    n = len(values)
    for i in range(n):
        minPos = i
        for j in range(i+1, n):
            if values[j] < values[minPos]:
                minPos = j
        listSwap(values, minPos, i)

def processFile():

    fileName = input("Filename: ")
    infile = open(fileName, "r")
    linesList = infile.readlines()
    toProcess = []
    processed = []
    for line in linesList:
        line = line[:-1]
        toProcess.append(line)
    for line in toProcess:
        subStrList = line.split()
        evalList = []
        for i in range(len(subStrList)):
            evalList.append(eval(subStrList[i]))
        selSort(evalList)
        processed.append(evalList)
    return processed

def main():

     sortedData = processFile()

main()

    
