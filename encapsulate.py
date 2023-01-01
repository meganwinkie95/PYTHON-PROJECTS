#creating a protected class

class Protected:
    def __init__(self):
        self.__privateVar = 13

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
#printing bothe the protected and the private class
obj = Protected()
obj.getPrivate()
obj.setPrivate(32)
obj.getPrivate()

