#creating a protected class
class Protected:
    def __init__(self):
        self._protectedVar = 9
obj = Protected()
obj._protectedVar = 16
print(obj._protectedVar)








class Protected:
    def __init__(self):
        self.__privateVar = 13

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
#printing both the protected and the private class
obj = Protected()
obj.getPrivate()
obj.setPrivate(32)
obj.getPrivate()

