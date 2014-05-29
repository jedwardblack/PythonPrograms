## Names: Marisaa Croop & Joseph Black
## hourlyWages.py

def main():

    infile = open("hourlyWages.txt", "r")
    numEmployees = len(infile.readlines())
    infile.close()
    infile = open("hourlyWages.txt", "r")
    contents = infile.readlines()
    outfile = open("newHourlyWages.txt", "w")
    

    for i in range(numEmployees):

        line = contents[i]
        splitLine = line.split()
        wage = eval(splitLine[2])
        newWage = wage+1.65
        firstName = splitLine[0]
        lastName = splitLine[1]
        hoursWorked = eval(splitLine[3])

        weekPay = round(hoursWorked*newWage, 2)
        outfile.write(str(firstName)+" "+str(lastName)+" "+str(weekPay)+"\n")

    print("Data written.")

        

main()
