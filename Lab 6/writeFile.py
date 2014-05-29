## writeFile.py
#If the file does not exist, opening it for writing will cause it
# to be created in the local folder.  If it does exist, the open
# function will cause the file to be wiped clean.

def main():
    print ("Executing writeFile.py")

    numNames = 5 #number of times to loop
    print("Enter " + str(numNames) + " names to write to a file.\n")

    # Name of the output file    
    outFileName = "familyNames.txt"
    outfile = open(outFileName, "w")
    
    #Simple loop to ask the user for names then write these to the file
    for i in range(numNames):
        name = input("What name to write?: ")
        print(name, file = outfile)

    print("Names have been written to " + outFileName)

    outfile.close()

main()
