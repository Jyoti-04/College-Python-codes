#BANKING PROJECT

class Account:
    def __init__(self):
        self.balance = 0
        print("your account is created")
    def deposit(self):
        amount = int(input('enter the amount to deposit:'))
        self.balance += amount
        print(f'your new balance = %d' %self.balance)
    def withdraw(self):
        amount = int(input('enter the amount to withdraw:'))
        if(amount>self.balance):
            print("insufficient balance!")
        else:
            self.balance -= amount
            print(f'your remaining balance =%d' %self.balance)
    def enquiry(self):
        print('your balance = %d' %self.balance)

account = Account()
account.deposit()
account.withdraw()
account.enquiry()
