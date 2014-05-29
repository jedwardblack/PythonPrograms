## Name: Joseph Black

def main():

    n = eval(input("How many terms? "))

    current = 1
    oneBack = 1
    twoBack = 1
    

    for i in range(2,n):

        oneBack = current
        current = oneBack + twoBack
        twoBack = oneBack
        
    print(current)
        

main()
        

             

