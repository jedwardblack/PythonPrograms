## Names: Marissa Croop & Joseph Black
## Assignment: encode.py

def main():
    originalMsg = input("Enter a message: ")
    key = eval(input("Enter key value: "))
    newWord = ""
    for i in range(len(originalMsg)):
        ch = originalMsg[i]
        newCh = chr(ord(ch) + key)
        newWord += newCh
    print(newWord)


main()
        
                   
               
