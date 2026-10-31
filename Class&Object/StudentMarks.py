class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def avr(self):
        average=0
        for i in self.marks:
            average+=i
            
        return average/6
s1=Student("someshwar",[18,18,19,20,17,16])       
print(s1.avr()) 