#Name: Joseph Black and Hudson Jones
#Assignment: numDigits.py

def main():

    num = eval(input("Enter a positive integer: "))
    i = 0
    while num > 0:
        while num > 0:
            num = num // 10
            i += 1
        print("The number of digits is " + str(i))
        num = eval(input("Enter a positive integer: "))
        i = 0
        
main()
