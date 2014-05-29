from graphics import *

def main():

    width = 400
    height = 400
    win = GraphWin("Draw Rectangle", width, height)
    textBox = Text(Point(width/2, height-10), "Click upper left and lower right corners.")
    textBox.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p1, p2)
    shape.draw(win)
    shapeWidth = (p2.getX())-(p1.getX())
    shapeHeight = (p2.getY())-(p1.getY())
    area = shapeWidth*shapeHeight
    perimeter = 2*(shapeHeight+shapeWidth)
    answerBox = Text(Point(width/2, height-350), "Area:"+str(area)+"\nPerimeter:"+str(perimeter))
    answerBox.draw(win)
    win.getMouse()
    win.close()
    

main()
