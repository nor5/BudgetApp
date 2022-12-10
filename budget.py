import math
class Category:

  def __init__(self, name):
    # Instance variable
    self.name = name
    self.ledger = []
    self.categorie_spent = 0
  def deposit(self, amount, description=''):

    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.categorie_spent += amount
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for a in self.ledger:
      balance = balance + a["amount"]
    return balance
##

  def transfer(self, amount, budget2):
    discription1 = "Transfer to " + budget2.name
    discription2 = "Transfer from " + self.name
    if self.check_funds(amount):
      self.withdraw(amount, discription1)
      self.categorie_spent += amount
      budget2.deposit(amount, discription2)
      return True
    else:
      return False




  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  #printing object Category
  def __str__(self):
    line = ""

    title = (self.name).center(30, "*") + "\n"
    #title = ((30 - len(self.name) ) // 2) * "*"+self.name + ((30 - len(self.name) ) // 2) * "*"+"\n"
    for i in self.ledger:

      #line += str(i['description'][:23]).ljust(23) + for_num.rjust(7) + '\n'

      line += (i["description"][:23]).ljust(23) + " " + ("{0:.2f}".format(
        i["amount"])[-7:]).rjust(7) + "\n"

    total = "Total " + str("{:.2f}".format(self.get_balance()))

    return title + line + total


def create_spend_chart(categories):
   total_spent = 0
   for categorie in categories:
      total_spent += categorie.categorie_spent
      print("total spent" +str(total_spent))
      
   for categorie in categories:
      
      percentage = math.floor(categorie.categorie_spent/total_spent*10)*10
      print("%"+str(percentage) )

   return "byebye"
