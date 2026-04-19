class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("To'lov miqdori manfiy bo'lishi yoki 0 ga teng bo'lishi mumkin emas.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        elif amount <= 0:
            print("To'lov miqdori manfiy bo'lishi yoki 0 ga teng bo'lishi mumkin emas.")
        else:
            print("Balansdan ortiqcha pul yechib bo'lmaydi.")

    def get_balance(self):
        return self.balance
```

Kodni ishlatish uchun misol:
```python
account = BankAccount(1000)
print(account.get_balance())  # 1000

account.deposit(500)
print(account.get_balance())  # 1500

account.withdraw(200)
print(account.get_balance())  # 1300

account.withdraw(1500)
print(account.get_balance())  # 1300

account.withdraw(0)
print(account.get_balance())  # 1300

account.withdraw(-100)
print(account.get_balance())  # 1300
