class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.area_code = number[0:3]
        self.sanitize()
        self.validation()

    def sanitize(self):

        self.number = "".join(
            [letter for letter in self.number if letter not in "+()-. "]
        )

    def check_length(self):

        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")

    def check_eleven_start(self):
        if len(self.number) == 11 and not self.number.startswith("1"):
            raise ValueError("11 digits must start with 1")

    def check_area_code(self):

        if self.number.startswith("0"):
            raise ValueError("area code cannot start with zero")

        if self.number.startswith("1"):
            raise ValueError("area code cannot start with one")

    def check_exchange_code(self):
        exchange_code = self.number[3]

        if exchange_code == "0":
            raise ValueError("exchange code cannot start with zero")

        if exchange_code == "1":
            raise ValueError("exchange code cannot start with one")

    def check_punctuation(self):
        for letter in self.number:
            if not letter.isalpha() and not letter.isdigit():
                raise ValueError("punctuations not permitted")

    def check_letters(self):
        for letter in self.number:
            if letter.isalpha():
                raise ValueError("letters not permitted")

    def validation(self):

        self.check_length()
        self.check_eleven_start()
        if len(self.number) == 11:
            self.number = self.number[1:]
        self.check_exchange_code()
        self.check_area_code()
        self.check_punctuation()
        self.check_letters()

    def pretty(self):
        area_code = self.number[0:3]
        exchange_code = self.number[3:6]
        subscriber_code = self.number[6:]

        return f"({area_code})-{exchange_code}-{subscriber_code}"
