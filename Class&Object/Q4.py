class Acount:
    def  __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def debit(self,debit):
        return self.balance+=self.balance+self.debit
    
    def credit(self,credit):
        return self.balance-=self.balance-self.debit

C_amount=int(input("Credit:"))
D_amount=int(input("Debit:"))
        
H1=Acount("Someshwar",10000)
H1.debit(C_amount)
H1.credit(D_amount)        