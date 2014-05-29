## Name: Joseph Black & Victoria Newton
## Assignement: wordAverage.py

def main():

    sent = input("Enter a sentence: ")

    spltSent = sent.split()
    spltLen = len(spltSent)
    newSent = sent.replace(" ","")
    newSent = newSent.replace(".","")
    charLen = len(newSent)

    avg = charLen/spltLen
    rndAvg = str(round(avg, 3))
    

    output = rndAvg.center(10)

    print(output)
