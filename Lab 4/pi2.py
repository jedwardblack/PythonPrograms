## Name: Joseph Black
## File: pi2.py

from math import*

def main():

    n = eval(input("How many terms? "))
    num = -4
    fractSum = 0
    denConst = 1
    fract = 0

    for i in range(n):

        num = -1*num
        den = denConst+(2*i)
        fract = (num/den)
        fractSum = fractSum + fract

    accuracy = pi-fractSum
    print("\nDifference:", accuracy)

main()

        

        

        
