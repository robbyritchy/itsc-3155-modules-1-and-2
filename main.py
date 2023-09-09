from BankAccount import BankAccount

account = BankAccount("Mark Walhberg", 2500.00)   

account.deposit(300.00)
account.withdraw(100.00) 

print(account.get_balance()) 
