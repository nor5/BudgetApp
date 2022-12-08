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
  #printing object Category
  def __str__(self):
    line1 = ""
   
    title = ((30 - len(self.name) ) // 2) * "*"+self.name + ((30 - len(self.name) ) // 2) * "*"
    for i in self.ledger:
     # amountFormating = "{:.2f}".format(i["amount"])
      line1 = line1 + i["description"][:23] +" "+ str("{:.2f}".format(i["amount"]))[-7:]+"\n"
      
    total = "Total "+str( "{:.2f}".format(self.get_balance()))
    

    
    return line1 +total
    
    
##
##
##
##
##def create_spend_chart(categories)
food = Category("foood")
clothing = Category("clothing")
food.deposit(1000 ,"initiale deposit")
clothing.deposit(100 ,"groceries")
food.withdraw (52.45643,"groceries")
o = food.withdraw (24,"restaurant and more food")
food.transfer(123, clothing )
print(food.get_balance())
print(o)
print(food.ledger)
print(food.name)
print(clothing.ledger)
print("object food")
print (food)
