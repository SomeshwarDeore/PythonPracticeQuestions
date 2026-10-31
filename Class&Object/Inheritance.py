class car:
    @staticmethod
    def start():
        print("car oi started..")
        
    @staticmethod
    def brk():
        print("car is stop")
        
class BMW(car):
    def __init__(self,price):
        self.price=price
        
c1=BMW(10000)
print(c1.price)
c1.start()                         