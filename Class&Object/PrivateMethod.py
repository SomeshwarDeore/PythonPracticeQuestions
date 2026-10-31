class Student():
    def __init__(self:Student,name:str,age:int)->None:
        self.name=name
        self.age=age
        
    def __hello(self):
        print("Hello") 
           
    def info(self)->None:
        self.__hello() 
        print(self.name,self.age,sep=" ")             
        
s1=Student("someshwar",18)
s1.info()      