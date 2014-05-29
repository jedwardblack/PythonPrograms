##Assignment: starter.py
##Name: Joseph Black


def main():

    weight = eval(input("Please enter the wrestler's weight: "))
    numWins = eval(input("Please enter this wrestler's number of wins: "))

    if (weight >= 150 and weight < 160) and (numWins >= 5):
        print("This wrestler should start.")

    elif (weight > 199) or (numWins > 20):
        print("This wrestler should start.")

    else:
        print("This wrestler should not start.")

main()
