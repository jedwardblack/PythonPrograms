from Point import Point
from math import *

class Circle:

    def __init__(self, xValue, yValue, radius):

        self.center = Point()
        self.center.setX(xValue)
        self.center.setY(yValue)
        if radius>0:
            self.radius = radius
        else: self.radius = 1

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def setCenter(self, xValue, yValue):
        self.center.setX(xValue)
        self.center.setY(yValue)

    def setRadius(self, r):
        if r>0:
            self.radius = r

    def area(self):
        area = pi*self.radius**2
        return area
        

    def __str__(self):
        return str("Circle:\n\tCenter: "+str(self.center)+"\n\tRadius: "
                   +str(self.radius)+"\n\tArea: "+str(self.area()))
        

        
