class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def sanitize_number(self):
        self.card_num = self.card_num.replace(" ", "")

    def is_all_digit(self):
        for char in self.card_num:
            if not char.isnumeric():
                return False

        return True

    def double_digit(self, digit):
        doubled = digit * 2
        return doubled if doubled < 10 else doubled - 9

    def sum_numbers(self, card_num_list):
        return sum(card_num_list)

    def valid(self):
        self.sanitize_number()

        if not self.is_all_digit():
            return False

        if len(self.card_num) <= 1:
            return False

        card_num_list = [int(digit) for digit in self.card_num]
        card_num_list.reverse()

        for index, digit in enumerate(card_num_list):
            if index % 2 == 1:
                card_num_list[index] = self.double_digit(digit)

        sum_digits = self.sum_numbers(card_num_list)

        return sum_digits % 10 == 0
