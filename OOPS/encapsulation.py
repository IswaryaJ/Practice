class car(object):
    def __init__(self):
        self.a = 123
        self._b = 456
        self.__c = 789
obj = car()

print(obj.a)
print(obj._b)
print(obj.__c)

