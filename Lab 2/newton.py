#Name: Joseph E> Black, Jr.
#Class: CSCI220
#Assignment:newton.py

import math
def main ():

    x = eval(input("What is the number? "))
    improve = eval(input("How many times to improve the approximation? "))
    appx = x/2

    for i in range(improve):
        appx = (appx+(x/appx))/2

    print(appx)
        


main()

    

    

        

        
   
