import math
import re

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
  
  def get_withdrawals(self) -> float:
    amount = 0
    for c in self.ledger:
      if c["amount"]< 0:
        amount += c["amount"] * -1
    return amount


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
  withdrawals = []
  total = 0
  for cat in categories:
    w = cat.get_withdrawals()
    withdrawals.append({
      "type": cat.get_type(),
      "amount": w,
    })
    total += w
    
  percentageLines = []
  x = 0
  y = 0
  for w in withdrawals: 
    l = len(withdrawals)
    w["percentage"] = math.floor((w["amount"] * 100) / total)
    i = 11
    inc = 0
    p = math.floor((w["percentage"] / 10) + 1)
    while i:
      if x == 0: percentageLines.append("")
      if i <= p: percentageLines[inc] += " o "
      else: percentageLines[inc] += "   "
      if y + 1 == l: percentageLines[inc] += " "
      i -= 1
      inc += 1
    x += 1
    y += 1
      
  output = "Percentage spent by category\n"
  i = 11
  x = 0
  while i:
    space = ""
    if i < 11 and i > 1: space = " "
    if i == 1: space = "  " 
    output += f"{space}{(i - 1) * 10}|{percentageLines[x]}\n"
    i -= 1
    x += 1
  output += "    " +  "-" * (3 * len(categories) + 1) + "\n"
  #loop 10 for % 1 for ---- and largest type len 

  typeLines = []
  x = 0
  y = 0
  for w in withdrawals:
    y = len(w["type"])
    if y > x: 
      x = y
  y = 0
  for w in withdrawals:
    l = len(withdrawals)
    t = w["type"]
    maxL = len(t)
    inc = 0
    loop = x
    while loop:   
      if y == 0: typeLines.append("    ")
      if inc < maxL: typeLines[inc] += f" {t[inc]} "
      else: typeLines[inc] += "   "
      #trailing space
      if y + 1 == l: typeLines[inc] += " "
      inc += 1
      loop -= 1
    y += 1
  
  y = 0
  for line in typeLines:
    if y + 1 == x: output += f"{line}"
    else: output += f"{line}\n"
    y += 1

  # output = output.rstrip()
  # output += " "  
    
    
  return output