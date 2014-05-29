# Author: RoxAnn H. Stalvey
# Illustrates getting numeric input through graphics window

from graphics import *

def main():
    win = GraphWin("Find the square", 300, 200)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input a number: ")
    boxDesc.draw(win)

    #create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)

    #Create a Text object for outputing the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary it just makes for a nice point for the user
    #  to click.  As long as you click in the window, the code reacts the same
    #  way.
    button = Text(Point(150, 100), "Click")
    button.draw(win)
    border = Rectangle(Point(115, 80), Point(185, 120))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    value = eval(inp.getText())

    #Calculate square of number
    square = value ** 2

    # Display output and change button
    output.setText(str(value) + "^2 = " + str(square))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
