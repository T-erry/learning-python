class BalanceException(Exception):
    pass
    
class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName

        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f} ")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance =${self.balance:2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f} ")

    def withdrawal(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdrawal complete!")
            self.getBalance()
        except BalanceException as  error :
            print(f'\nWithdwal Interrupted: {error}')



    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. ')
            self.viableTransaction(amount)
            self.withdrawal(amount)
            account.deposit(amount)
            print('\n Transfer complete!\n\n**********')

        except BalanceException as error:
            print(f'\nTransfer Interrupted: {error}')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.5)
        print("\nDeposit Completee")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5


    def withdrawal(self, amount):
        try:
           self.viableTransaction(amount + self.fee )
           self.balance = self.balance - (amount + self.fee)
           print("\nWithdrawal complete")
           self.getBalance()
        except BalanceException as error:
           print(f'\nWithdrawal interrupt   ed: {error}')
           






