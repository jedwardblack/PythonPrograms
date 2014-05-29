## Names: Marissa Croop and Joseph Black
## numberWords.py

def main():
    inFile = input("Enter input file: ")
    outFile = input("Enter output file: ")
    infile = open(inFile, "r")
    outfile = open(outFile, "w")
    inContents = infile.read()
    lineSplit = inContents.split()

    for i in range(len(lineSplit)):
        outLine = (str(i+ 1) + ". " + lineSplit[i])
        print(outLine)
        outfile.write(outLine + "\n")
        
    print("Data written.")
    infile.close()
    outfile.close()
                   
main()
