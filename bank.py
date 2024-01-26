class Bank:
    bank_name="MyBank"
    total_balance=0
    account_count=0
    intrest_rate=0.5

def init(self,account_holder,initial_balance):
    self.account_holder=account_holder
    self.balance=initial_balance
    Bank.total_balance+=initial_balance
    Bank.account_count+=1

def deposit(self,amount):
    self.balance+=amount
    Bank.total_balance+=amount
def withdraw(self,amount):
    if amount<=self.balance:
        self.balance-=amount
        Bank.total_balance=amount
    else:
        print('Insufficient funds')
def set_intrest_rates(cls,new_rate):
    cls.intrest_rate=new_rate
def get_bank_info(cls):
  return f"{cls.bank_name}:Total Accounts-{cls.account_count},Total Balance-{cls.total_balance}"
  account1=Bank("Prashanth250",1000)
  account2=Bank("Jassu",2000)
  account3=Bank("Devil",1500)
  account4=Bank("Tom",3000)
  account5=Bank("Ashu",5000)

  account1.deposit(250)
  account2.withdraw(250)
  account3.deposit(1000)
 
  Bank.set_intrest_rate(0.03)
print(Bank  ())