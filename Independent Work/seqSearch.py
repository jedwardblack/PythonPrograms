
def seqSearch(seq, subSeq):

    m = len(subSeq)
    n = len(seq)
    notFound = "\nSubsequence not found."
    found = "\nSubsequence found at position "
    if m > n:
        return notFound
    for i in range(n-m+1):
        j = 0
        while (seq[i+j] == subSeq[j]):
            j += 1
            if j == m:
                return found+str(i)+"."
    return notFound
    
def main():

    seq = input("Please enter a text sequence: ")
    search = input("Please enter another sequence: ")

    answer = seqSearch(seq, search)

    print(answer)
    

    

main()

    
