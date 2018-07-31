class Dog(object):
    def sound(self):
        print(" I am a puppy ")

class Bear(object):
    def sound(self):
        print(" I am a Bear")

def makesound(animaltype):
    animaltype.sound()

dogObj = Dog()
bearObj = Bear()

makesound(bearObj)
 
