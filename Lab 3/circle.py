from graphics import *
from math import *

def main():

    win = GraphWin("Circle", 400, 400)
    textBox = Text(Point(200, 390), "Click center and point on circle.")
    textBox.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    xOne = p1.getX()
    xTwo = p2.getX()
    yOne = p1.getY()
    yTwo = p2.getY()

    radius = sqrt(((xTwo-xOne)**2)+((yTwo-yOne)**2))
    shape = Circle(p1, radius)
    shape.draw(win)
    ansBox = Text(Point(200, 50), "Radius:"+str(radius))
    ansBox.draw(win)
    

    win.getMouse()
    win.close()

main()

