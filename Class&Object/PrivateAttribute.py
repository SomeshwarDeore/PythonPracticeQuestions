class Student:
    def __init__(self,name):
        self.__name=name
        
    def info(self):
        return self.__name    
        
s1=Student(input("Enter your name :"))
print(s1.info())