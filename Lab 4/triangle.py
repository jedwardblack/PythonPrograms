## Name: Joseph Black
## File: triangle.py

from graphics import*
from math import*

def main():

    winWidth = 600
    winHeight = 600
    win = GraphWin("Triangle", winWidth, winHeight)

    instr = Text(Point(winWidth/2,winHeight-20), "Click the window 3 times")
    instr.draw(win)

    pointOne = win.getMouse()
    pointTwo = win.getMouse()
    sideA = Line(pointOne, pointTwo)
    sideA.draw(win)

    pointThree = win.getMouse()
    sideB = Line(pointTwo, pointThree)
    sideC = Line(pointThree, pointOne)
    sideB.draw(win)
    sideC.draw(win)

    xOne = pointOne.getX()
    yOne = pointOne.getY()

    xTwo = pointTwo.getX()
    yTwo = pointTwo.getY()

    xThree = pointThree.getX()
    yThree = pointThree.getY()

    dXA = xTwo - xOne
    dYA = yTwo - yOne
    lengthA = sqrt((dXA**2)+(dYA**2))

    dXB = xThree - xTwo
    dYB = yThree - yTwo
    lengthB = sqrt((dXB**2)+(dYB**2))

    dXC = xOne - xThree
    dYC = yOne - yThree
    lengthC = sqrt((dXC**2)+(dYC**2))

    perim = lengthA+lengthB+lengthC
    s = perim/2
    area = sqrt(s*(s-lengthA)*(s-lengthB)*(s-lengthC))
    
    ans1 = Text(Point(winWidth/2,winHeight-575), "Perimeter: "+str(perim))
    ans2 = Text(Point(winWidth/2,winHeight-550), "Area: "+str(area))
    ans1.draw(win)
    ans2.draw(win)
    

    instr.setText("Click again to close.")
    win.getMouse()
    win.close()
