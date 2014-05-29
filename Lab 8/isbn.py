##Assignment: isbn.py
##Name: Joseph Black

def main():

    isbn = input("Please input the ISBN: ")

    if len(isbn) != 10:
        print("This is not a valid ISBN.")
    else:
        
        newIsbn = isbn[::-1]
 
        sumMultiples = 0
        for i in range(len(newIsbn)):
            newI = (i+1) * eval(newIsbn[i])
            sumMultiples += newI

        checkSum = sumMultiples % 11
    
        if checkSum == 0:
            print("This is a valid ISBN.")
        else:
            print("This is not a valid ISBN.")


main()
        
