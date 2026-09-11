class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_opened = False

    def check_account_open(self):
        if not self.is_opened:
            raise ValueError("account not open")

    def check_negative_amount(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")

    def get_balance(self):

        self.check_account_open()

        return self.balance

    def open(self):

        if self.is_opened:
            raise ValueError("account already open")

        self.is_opened = True
        self.balance = 0

    def deposit(self, amount):

        self.check_account_open()
        self.check_negative_amount(amount)

        self.balance += amount

    def withdraw(self, amount):

        self.check_account_open()
        self.check_negative_amount(amount)

        if amount > self.balance:
            raise ValueError("amount must be less than balance")

        self.balance -= amount

    def close(self):

        self.check_account_open()

        self.is_opened = False
