class Category: 
  
  def __init__(self, category, amount):
    
    self.category = category
    self.amount = amount

  #methods
  def deposit(self, amount):
    self.amount += amount
    return ('You have deposited ${} in {} account.'. format(amount, self.category))

  def budgetBalance (self):
    return ("For {} account, this is the current balance: ${}".format(self.category, self.amount))

  def checkBalance(self, amount):
    #This should return a boolean, it checks if balance is less than new amount
      return (self.amount < amount)
        
  def withdraw (self, amount):
    #reverse of deposit
    self.amount -= amount
    return ('You have withdrawn ${} from {} account.'. format(amount, self.category))
    pass
 
  def transfer (self, amount):
    #trasfer between two catagories
    #self.difference = self.amount - amount
    #self.newAmount = self.amount + amount
    #checkbalance returns boolean so use to see if amount tranferring is more/less than current balance
    if (self.checkBalance(self.amount)):
      self.amount -= amount
      #deposit = self.category + amount
    
    #withdaw = self.amount - amount
    # deposit = category of trnafer.amount + amount 
    
    #return ("You have moved ${} from {} acount and moved it to {} account.". format(amount, self.checkBalance, self.category ))
    return amount


foodCategory = Category('food', 500)
clothingCategory = Category('clothing', 100)
carCategory = Category ('car', 250)
miscCategory = Category("misc.", 700)


print(foodCategory.deposit(50))
print (miscCategory.budgetBalance())
print(carCategory.withdraw(50))
print(carCategory.checkBalance(50))
print (clothingCategory.deposit(miscCategory.transfer(45)))
print (miscCategory.budgetBalance())