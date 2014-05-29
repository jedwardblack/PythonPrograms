## Discussion #3, Graphics chapter of Zelle text
## Moves a circle based on user clicks
## Comments added: RHS

from graphics import *

def main():
    #Creates a graphical window
    win = GraphWin("Lab 3", 400, 400)
    width = win.getWidth()
    height = win.getHeight()

    #number of times user can move circle
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move circle")
    instructions.draw(win)

    #builds a square
    shape = Rectangle(Point(50,50),Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #circle
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of circle

        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx, dy)
        shape.draw(win)
        

    instructions.setText("Click again to quit")
    win.getMouse()
    win.close()

main()
