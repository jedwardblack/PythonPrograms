
class Point:

    def __init__(self):
        self.xValue = 0
        self.yValue = 0

    def setX(self, value):
        self.xValue = value

    def setY(self, value):
        self.yValue = value

    def getX(self):
        return self.xValue

    def getY(self):
        return self.yValue

    def __str__(self):
        return str("("+str(self.xValue)+", "+str(self.yValue)+")")        
