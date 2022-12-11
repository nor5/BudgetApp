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
    max_name = 0
    

    title = (self.name).center(30, "*") + "\n"
    #title = ((30 - len(self.name) ) // 2) * "*"+self.name + ((30 - len(self.name) ) // 2) * "*"+"\n"
    for i in self.ledger:

      #line += str(i['description'][:23]).ljust(23) + for_num.rjust(7) + '\n'

      line += (i["description"][:23]).ljust(23) + ("{0:.2f}".format(
        i["amount"])[-7:]).rjust(7) + "\n"

    total = "Total: " + str("{:.2f}".format(self.get_balance()))

    return title + line + total


def create_spend_chart(categories):
   total_spent = 0
   max_percentage = 0
   categories_percentage = []
   line = ""
   line3 = ""
   max_name = 0
   alphabet = 0
   for categorie in categories:
      total_spent += categorie.categorie_spent
   
      if max_name <= len(categorie.name):
           max_name = len(categorie.name)
   print("max name"+str(max_name))
   print("total spent" +str(total_spent))
   for x in range(100, -10 , -10):  
     line += str(x).rjust(3) + "|"
     for categorie in categories:
        if categories.index(categorie) < 5:
            percentage = math.floor(categorie.categorie_spent/total_spent*10)*10
           
            
            i = categories.index(categorie)
           
            if percentage >= x:
               
                 if i == 0:
                  line +=("o").rjust(2) 
                 else:
                   line +=("o").rjust(3) 
          
     line += " \n"  
   for alphabet in range (0,max_name) :  
     for  index_categorie in range (0, len(categories)):
           
           
           if len(categories[index_categorie].name) > alphabet :
                 if index_categorie == 0:
                      line3 += categories[index_categorie].name[alphabet].rjust(6)
                  
                # elif index_categorie !=0 and len(categories[index_categorie].name) > len(categories[index_categorie-1].name):
           
                 else:
                      line3 += categories[index_categorie].name[alphabet].rjust(3)
           elif len(categories[index_categorie].name) <= alphabet and len(categories[index_categorie].name) < max_name:
             
             if index_categorie ==0:
                      line3 += " ".rjust(6)
                  
                # elif index_categorie !=0 and len(categories[index_categorie].name) > len(categories[index_categorie-1].name):
           
             else:
                      line3 += " ".rjust(3)
     line3 += "\n"
   line2 = ("-").rjust(5)+"-"*(3*len(categories))+"\n"
   return line + line2 + line3


 
