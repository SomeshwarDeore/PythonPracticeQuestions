class List:
    def __init__(self,list,target):
        self.list=list
        self.target=target

    def show(self):
        for i in range(0,len(self.list)):
            for j in range(i+1,len(self.list)):
                if self.list[i]+self.list[j]==self.target :
                    return [i,j]  
L1=List([1,2,3,4],7)
print(f"target found at :{L1.show()}")
                  