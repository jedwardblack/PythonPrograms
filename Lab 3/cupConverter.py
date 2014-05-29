# Author: RoxAnn H. Stalvey
# Illustrates getting numeric input through graphics window

from graphics import *

def main():
    win = GraphWin("Cup Converter", 300, 200)

    boxDesc = Text(Point(100, 50), "How many cups do you have: ")
    boxDesc.draw(win)
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)
    output = Text(Point(150, 150), "")
    output.draw(win)
    button = Text(Point(150, 100), "Click to calculate.")
    button.draw(win)
    win.getMouse()
    value = eval(inp.getText())
    
    ounces = value*8*29.57
    output.setText(str(ounces))
    button.setText("Click to close")
    win.getMouse()
    win.close()

main()
