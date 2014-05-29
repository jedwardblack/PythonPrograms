#Name: Joseph Black and Hudson Jones
#Assignment: goodInput.py

def main():

    num = eval(input("Enter a number inclusively between 1 and 10: "))

    while num < 1 or num > 10:
        
        print("Did you read the instructions? Try again.")
        num = eval(input("Enter a number inclusively between 1 and 10: "))
        

    print(num)
main()
        
