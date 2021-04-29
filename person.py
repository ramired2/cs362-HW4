class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

def getInfo():
    firAsk = "Please enter a first name: "
    firName = input(firAsk)

    lastAsk = "Please enter a last name: "
    lastName = input(lastAsk)
    
    per = Person(firName, lastName)
    return per


# print (per.first, per.last)