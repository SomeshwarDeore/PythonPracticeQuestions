class Account:

    def _init_(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Money deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Money withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)


# Object
account1 = Account("Someshwar", 12345, 5000)

account1.display()

account1.deposit(2000)
account1.withdraw(1000)

account1.display()