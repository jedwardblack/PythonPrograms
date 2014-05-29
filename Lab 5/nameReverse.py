## Name: Joseph Black & Victoria Newton
## Assignement: nameReverse.py

def main ():

    name = input("Name: ")
    splitName = name.split()
    renameLast = splitName[0]
    renameFirst = splitName[1]
    newName = renameFirst+", "+renameLast
    print(newName)

main()
