#Name: Joseph E> Black, Jr.
#Class: CSCI220
#Assignment:coffee.py

def main ():

    perLb = 10.5
    shipPerLb = .86
    overhead = 1.5
    n = eval(input("How many orders to process? "))
    
    for i in range(n):
        weight = eval(input("How many pounds? "))
        orderShip = shipPerLb*weight
        weightCost = perLb*weight
        orderTotal = weightCost+orderShip+overhead
        print("Order Total: ", orderTotal)

main()
        
        

    

    

        

        
   
