#Name: Joseph E> Black, Jr.
#Class: CSCI220
#Assignment:triangleArea.py

import math
def main ():

    sideA = eval(input("What is the length of side A? "))
    sideB = eval(input("What is the length of side B? "))
    sideC = eval(input("What is the length of side C? "))

    s = (sideA+sideB+sideC)/2
    
    area = math.sqrt(s*((s-sideA)*(s-sideB)*(s-sideC)))

    print("Area: ", area)

main()
        
        

    

    

        

        
   
