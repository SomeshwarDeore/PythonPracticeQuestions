class Student:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
        
    def info(self):
        print(self.name)
        print(self.age)
        
    def result(self):
        print("Pass" if self.marks>=35 else "Fail")
      
S1=Student("Someshwar",120,18)  
S1.info()
S1.result()              