## Name: Joseph Black & Victoria Newton
## Assignement: initials.py

def main():

    classSize=eval(input("Students in Class: "))

    for i in range(classSize):

        firstNam=input("Enter the first name of student"+str(i+1)+": ")
        lastNam=input("Enter "+firstNam + "'s last name: ")
        firstInt=firstNam[0]
        lastInt=lastNam[0]
        print(firstNam+"'s initaials are "+firstInt+lastInt+".")

main ()
