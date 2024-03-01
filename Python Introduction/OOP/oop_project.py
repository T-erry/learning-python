from bank_acccounts import *

Terry = BankAccount(10000, "Terry")
Wanjiru = BankAccount(2000, "Wanjiru")

Terry.getBalance()
Wanjiru.getBalance()

Wanjiru.deposit(5000)


Terry.withdrawal(5000)

Wanjiru.transfer(2000, Terry)

jim = InterestRewardsAcct(1000, "Jim")

jim.getBalance()

jim.deposit(100)

jim.transfer(100, Terry)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(200)

# Blaze.transfer(100, Wanjiru)
Blaze.transfer(1000, Wanjiru)


