## Average.py
## Joseph E. Black, Jr.

def main():
    print("This program calculates the average of 10 numbers.")

    numValues = 4
    total = 0      
    for number in range (numValues):
        value = eval(input("Number: "))
        total = total+value

    average = total/numValues

    print("Average =", average)

main()
