

def swap(someList, a, b):

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
        swap(values, minPos, i)

def main():

    nums = [12, 31, 19, 19, 4, 27, 3, 500]
    selSort(nums)
    print(nums)

main()

    
