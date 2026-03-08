#create class to rep a bank acc - attributes - acc no., balance and methods- deposit, withdraw, check balance

class bankacc :
    def __init__(self, accnumber , initial_balance=0):
        self.accnumber = accnumber
        self.balance = initial_balance

    def checkbalance(self):
        print(f"Current Balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print (f"Deposited amount: {amount}")
            print (f"Updated Balance : {self.balance}")

        else :
            print ("Deposit value must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print (f"Amount withdrawn : {amount}")  
                print (f"Updated balance : {self.balance}")
            else :
                print ("Insufficient balance.")
        else :
            print ("Amount must be positive.")

        
account= bankacc(1234 , 1000)

while True :
    print ("\n 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Exit")
    choice = int(input("Enter your choice:  "))
    
    if choice == 1 :
        account.checkbalance()
    elif choice == 2:
        amount = int(input("Enter amount to deposit:    "))
        account.deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw:   "))
        account.withdraw(amount)

    elif choice == 4:
        break
    else : 
        print ("Invalid, Please try again.")