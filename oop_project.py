from bank_accounts import *

Travis = BankAccount(1000, "Travis")
Bonnie = BankAccount(2000, "Bonnie")

Travis.getBalance()
Bonnie.getBalance()

Bonnie.deposit(500)

Travis.withdraw(10000)
Travis.withdraw(10)

Travis.transfer(10000, Bonnie)
Travis.transfer(100, Bonnie)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Travis)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000, Travis)

