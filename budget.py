import math

class Category:
  def __init__(self, type):
    self.type = type
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description = "") -> None:
    f = float("{:.2f}".format(amount))
    self.balance += f
    self.ledger.append({
      "amount": amount,
      "description": description
    })
  
  def withdraw(self, amount, description = "") -> bool:
    if not self.check_funds(amount): return False
    f = float("{:.2f}".format(amount))
    self.balance -= f
    self.ledger.append({
      "amount": amount * -1,
      "description": description
    })
    return True

  def get_balance(self) -> float:
    return self.balance

  def check_funds(self, amount) -> bool:
    return amount <= self.balance

  def get_type(self) -> str:
    return self.type

  def transfer(self, amount, budget) -> bool:
    if not self.check_funds(amount): return False
    self.withdraw(amount, f"Transfer to {budget.get_type()}")
    budget.deposit(amount, f"Transfer from {self.get_type()}")
    return True


  def __str__(self) -> str:
    typeLength = len(self.get_type())
    starL, starR = ["*", "*"]
    if typeLength % 2 == 0:
      x = int((30 - typeLength) / 2)
      starL *= x
      starR *= x
    else:
      x = int(math.floor((30 - typeLength) / 2))
      starL *= x
      starR *= x
      starR += "*"
    output = f"{starL}{self.type}{starR}\n"
    for transaction in self.ledger:
      amountStr = float(transaction["amount"])
      amountStr = format(amountStr, ".2f")
      descL, amL = ([len(transaction["description"][:23]), len(amountStr)])
      space = " " * (30 - (descL + amL))
      output += f"{transaction['description'][:23]}{space}{amountStr}\n"
    output += f"Total: {format(self.balance, '.2f')}" 
    return output  

def create_spend_chart(categories):
  return "WIP"