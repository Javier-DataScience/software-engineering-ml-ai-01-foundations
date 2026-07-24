class BankAccount:
    """A simple bank account."""

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount}")

    def get_balance(self):
        return self._balance


def main():
    account = BankAccount("Alvaro", 1000)

    print(f"Initial balance: ${account.get_balance()}")

    account.deposit(500)
    print(f"Balance: ${account.get_balance()}")

    account.withdraw(300)
    print(f"Balance: ${account.get_balance()}")

    account.withdraw(5000)
    print(f"Balance: ${account.get_balance()}")


if __name__ == "__main__":
    main()