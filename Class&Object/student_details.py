class Student:
    def __init__(self,name:str,roll_no:int,marks:dict):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def Total(self):
        sum=0
        value=self.marks.values()
        for i in value:
            sum+=i
        
        return sum
class Marks(Student):
    def __init__(self,name:str,roll_no:int,marks):
        super().__init__(name,roll_no,marks)
s1=Marks("someshwar",40,{"Math":20,"OE":16})                
print(s1.Total())