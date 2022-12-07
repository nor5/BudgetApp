class Category:
  def __init__(self, name):
        # Instance variable
        self.name = name
        self.ledger = []
  def deposit (self, amount , description):
       
        self.ledger.append({"amount": amount, "description": description})
  
  
  
  

  

  def withdraw (self, amount , description):
    if self.check_funds(amount):
       self.ledger.append({"amount": -amount, "description": description})
       return True
    else:
      return False


  def get_balance (self):
    balance = 0
    for a in self.ledger:
      balance = balance + a["amount"]
    return balance
##    
  def transfer (self, amount, budget2):
    discription1 = "Transfer to "+ budget2.name
    discription2 = "Transfer from "+ self.name
    if self.check_funds(amount):
      self.withdraw(amount , discription1 )
      budget2.deposit(amount , discription2 )
      return True
    else:
      return False
    
  
##
  def check_funds (self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

    
##
##
##
##
##def create_spend_chart(categories)
food = Category("food")
clothing = Category("clothing")
food.deposit(34 ,"groceries")
clothing.deposit(100 ,"groceries")
o = food.withdraw (2 ,"groceries")
food.transfer(123, clothing )
print(food.get_balance())
print(o)
print(food.ledger)
print(food.name)
print(clothing.ledger)
