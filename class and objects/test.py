class Dog:
    def __init__(self, name):
        __name__ = name
    
    def name(self):
        return __name__
    
dogObj = Dog("Timmy")
print(dogObj.name())