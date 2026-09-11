class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = False
        self.closed = False

    def check_account_closed(self):
        if self.closed and not self.opened:
            raise ValueError("account not open")

    def check_account_opened(self):
        if not self.opened:
            raise ValueError("account not open")

    def check_negative_amount(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")

    def get_balance(self):

        self.check_account_closed()

        return self.balance

    def open(self):
        # self.check_account_closed()

        if self.opened:
            raise ValueError("account already open")

        self.opened = True
        self.balance = 0

    def deposit(self, amount):

        self.check_account_closed()
        self.check_account_opened()

        self.check_negative_amount(amount)

        if self.opened and not self.closed:
            self.balance += amount

    def withdraw(self, amount):

        self.check_account_closed()

        if amount > self.balance:
            raise ValueError("amount must be less than balance")

        self.check_negative_amount(amount)

        self.balance -= amount

    def close(self):

        self.check_account_opened()

        self.closed = True
        self.opened = False
