class Animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

dog1=Animal("Sheru",3,"white")

def info(dog1):
    print(dog1.name)
    print(dog1.age)
    print(dog1.color)
info(dog1)    