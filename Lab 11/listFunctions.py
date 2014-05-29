# listFunctions.py

def main():
    L = ["apple", "pear", "banana", "plum", "cherry", "apple"]
    print ("The list:", L)

    print("\nAppending lime to the end of the list.")
    L.append("lime")
    print ("The list:", L)

    print ("\nInserting lemon at position 2")
    L.insert(2, "lemon")
    print ("The list:", L)

    print ("\nThere are", L.count("apple"), "occurrences of apple.")

    print ("\nThe position of the first occurrence of apple is", end = " ")
    print (L.index("apple"))

    print ("\nRemoving the first occurrence of apple.")
    L.remove("apple")
    print ("The list:", L)

    print ("\nRemoving AND returning the element at position 4.")
    element = L.pop(4)
    print ("The list:", L)
    print ("The element that was popped was:", element)

    print ("\nSorting the list.")
    L.sort()
    print ("The list:", L)

    print ("\nReversing the list.")
    L.reverse()
    print ("The list:", L)

main()
