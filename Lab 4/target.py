## Name: Joseph Black
## File: target.pu

from graphics import*
def main():

    winWidth = 600
    winHeight = 600
    winCenter = Point((winWidth/2), (winHeight/2))
    win = GraphWin("Target", winWidth, winHeight)
    entryBox = Entry(Point(winWidth/2,winHeight-15), 30)
    entryBox.setText("Radius? Max. 60 ")
    entryBox.draw(win)
    win.getMouse()
    rad = eval(entryBox.getText())
    cir5 = Circle(winCenter, rad*5)
    cir5.draw(win)
    cir4 = Circle(winCenter, rad*4)
    cir4.draw(win)
    cir4.setFill("black")
    cir3 = Circle(winCenter, rad*3)
    cir3.draw(win)
    cir3.setFill("blue")
    cir2 = Circle(winCenter, rad*2)
    cir2.draw(win)
    cir2.setFill("red")
    cir1 = Circle(winCenter, rad*1)
    cir1.draw(win)
    cir1.setFill("yellow")
    entryBox.setText("Click to close.")

    win.getMouse()
    win.close()

main()
