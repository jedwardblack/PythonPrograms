class Money:

    def __init__(self):

        self.dollars = 0
        self.cents = 0

    def getDollars(self):
        return self.dollars

    def getCents(self):
        return self.cents

    def setDollars(self, value):
        if value>0:
            self.dollars = value

    def setCents(self, value):
        if value>0:
            self.cents = value%100
            dollars = value//100
            self.dollars += dollars

    def compareTo(self, m):
        a = self.dollars*100
        b = self.cents
        valueSelf = a+b
        c = m.getDollars()*100
        d = m.getCents()
        valueM = c+d
        if valueSelf < valueM:
            ans = valueSelf - valueM
        elif valueSelf == valueM:
            ans = 0
        elif valueSelf > valueM:
            ans = valueSelf - valueM
        return ans

    def increment(self, m):
        self.dollars += m.getDollars()
        self.setCents(self.cents + m.getCents())
        

    def __str__(self):
        if len(str(self.cents)) == 1:
            answer = str("$"+str(self.dollars)+".0"+str(self.cents))
        else:
            answer = str("$"+str(self.dollars)+"."+str(self.cents))
        return answer
