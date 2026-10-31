class Student:
    def __init__(self,name:str,age:int,marks:list[int])->None:
        self.name=name
        self.age=age
        self.marks=marks
        
    def result(self):
        sum=0
        for i in self.marks:
            sum+=i
            
        return sum/3    
        
class marks(Student):
    pass

class result(marks):
     pass
     
s1=result("Someshwar",18,[18,19,20])
print(s1.result())