## Names: Marissa Croop and Joseph Black
## pigLatin.py

def main():

    sent = input("Enter a sentence: ")

    splitSent = sent.split()

    newSent = ""

    for i in range(len(splitSent)):

        wordI = splitSent[i]
        chZero = str(wordI[0])
        chRem = str(wordI[1:])
        newWord = chRem+chZero+"ay"
        newSent += newWord+" "

    print(newSent.lower())

main()
        
                 
