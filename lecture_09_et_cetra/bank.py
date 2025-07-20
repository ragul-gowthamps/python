# balance = 0
# def main():
    
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:",balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main() 


class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        
    @property
    def get_balance(self):
        return self._balance
    
def main():
    account = BankAccount()
    print("Balance:", account.get_balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.get_balance)

if __name__ == "__main__":
    main()