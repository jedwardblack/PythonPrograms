#Name: Joseph E> Black, Jr.
#Class: CSCI220
#Assignment:pi.py

def main ():

    n = eval(input("What is n: "))
    den = 1
    num = 0
    answer = 1
    
    for i in range(n):
        den = den+((i%2)*2)
        num = num+(((i+1)%2)*2)
        answer = answer*(num/den)
##        print(num, "/", den)

    print((answer)*2)
        

main()

    

    

        

        
   
