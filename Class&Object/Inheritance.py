class car:
    @staticmethod
    def start():
        print("car is started..")
        
    @staticmethod
    def brk():
        print("car is stop")
        
class BMW(car):#inherit car class
    def __init__(self,price):
        self.price=price
        
c1=BMW(10000)
print(c1.price)
c1.start()                       