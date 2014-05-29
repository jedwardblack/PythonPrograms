def decToBin(n):

    numStr = str(n)
    numStrList = numStr.split(".")
    print(numStrList)

    # Change number to left of decimal to binary
    toLeft = eval(numStrList[0])
    binLeft = bin(toLeft)
    
    # Change number to right of decimal to binary
    toRight = len(numStrList[1])        
        
            

def main():

    dec = input("Please enter a decimal number: ")

    binRep = decToBin(dec)

    print(binRep)

main()
