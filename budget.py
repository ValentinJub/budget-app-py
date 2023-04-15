class Category:
  type = ""
  ledger = []
  balance = 0
  def __init__(self, type):
    self.type = type

  def deposit(self, amount, description = ""):
    self.ledger.append({
      "amount": amount,
      "description": description
    })
    self.balance += amount
  
  def withdraw(self, amount, description):
    if self.balance < amount:
      return False
    self.ledger.append({
      "amount": amount * -1,
      "description": description
    })
    self.balance -= amount
    return True

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    return amount < self.balance


# def create_spend_chart(categories):