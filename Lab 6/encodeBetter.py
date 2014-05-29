## Names: Marissa Croop & Joseph Black
## Assignment: encodeBetter.py

def main():
    originalMsg = input("Enter a message: ")
    key = eval(input("Enter key value: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    newWord = ""
    for i in range(len(originalMsg)):
        ch = originalMsg[i]
        chValue = alphabet.find(ch)
        newChValue = (chValue+key)%26
        newCh = alphabet[newChValue]
        newWord += newCh
    print(newWord)
