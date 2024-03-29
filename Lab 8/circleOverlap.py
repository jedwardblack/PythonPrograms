##Assignment: circleOverlap.py
##Name: Joseph Black

from graphics import *
from math import sqrt

def main():
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-30), "")
    instruct.draw(win)

    #Get center point and x/y for Circle1
    instruct.setText("Draw Circle #1: Click the centerpoint for the circle...")
    center = win.getMouse()
    center.draw(win)
    cX = center.getX()
    cY = center.getY()

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle....")
    border = win.getMouse()
    bX = border.getX()
    bY = border.getY()

    #Calculate radius using Euclidean distance
    radius = sqrt((cX-bX) ** 2 + (cY-bY) ** 2)
    circle = Circle(center, radius)
    circle.draw(win)

    #Get center point and x/y for Circle2
    instruct.setText("Draw Circle #2: Click the centerpoint for the circle...")
    center2 = win.getMouse()
    center2.draw(win)
    c2X = center2.getX()
    c2Y = center2.getY()

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle....")
    border2 = win.getMouse()
    b2X = border2.getX()
    b2Y = border2.getY()

    #Calculate radius using Euclidean distance
    radius2 = sqrt((c2X-b2X) ** 2 + (c2Y-b2Y) ** 2)
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    centerToCenter = sqrt((cX-c2X)**2 + (cY-c2Y)**2)

    if centerToCenter <= radius+radius2:
        instruct.setText("These circles overlap.\nClick anywhere to close.")
    else:
        instruct.setText("These circles do not overlap.\nClick anywhere to close.")

    win.getMouse()
    win.close()
    
main()
