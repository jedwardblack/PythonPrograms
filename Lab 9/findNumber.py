#Name: Joseph Black and Hudson Jones
#Assignment: findNumber.py

def main():

    myList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    num = eval(input("Please enter a number: "))
    i = 0

    while i < len(myList)and num != myList[i]:
        i += 1

    if i >= len(myList):
        print("Number not in list.")

    else:
        print(i)

main()


    
        

    
