import random

class Banking:
  def __init__(self):
    print("Welcome to our banking system.")
    self.name = input("Enter your name: ")
    while True:
      try:
        self.amount = int(input("Enter your initial balance: "))
        if self.amount <= 0: print("Amount should be positive. Please try again.")
        else: break
      except ValueError: print("Please enter a valid integer amount.")
    self.account_no = random.randint(10 ** 7, 10 ** 10 - 1)
    self.history = []

  def account_info(self):
    print(f"Name: {self.name}")
    print(f"Account Number: {self.account_no}")
    print(f"Remaining Balance: {self.amount}")

  def transaction_history(self):
    if not self.history:
      print("No transactions yet.")
      return
    for txn_type, amount in self.history:
      if txn_type == "deposit": print(f"Deposited {amount}")
      else: print(f"Withdrawing {amount}")

  def withdraw_money(self):
    while True:
      try:
        amount = int(input(f"Enter amount to withdraw (1 to {self.amount}): "))
        if amount < 1 or amount > self.amount: print("Invalid Amount. Please try again.")
        else:
          self.amount -= amount
          self.history.append(("withdraw", amount))
          print("Successfully withdrawn.")
          break
      except ValueError: print("Please enter a valid integer amount.")

  def deposit_money(self):
    while True:
      try:
        amount = int(input("Enter amount to deposit (Positive Number): "))
        if amount < 1: print("Amount should be positive. Please try again.")
        else:
          self.amount += amount
          self.history.append(("deposit", amount))
          print("Deposited successfully.")
          break
      except ValueError: print("Please enter a valid integer amount.")

def main():
  bank = Banking() # Open bank account
  while True:
    print("\n0. Exit")
    print("1. Check user information")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Show Transaction History")

    try:
      choice = int(input("Enter your choice (between 0 to 4): "))
      if choice == 0:
        print("\nThanks for using our banking management system.")
        break
      elif choice == 1: bank.account_info()
      elif choice == 2: bank.deposit_money()
      elif choice == 3: bank.withdraw_money()
      elif choice == 4: bank.transaction_history()
      else: print("Invalid choice. Try again!")
    except ValueError: print("Please enter a valid integer choice.")

if __name__ == "__main__":
  main()