class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def sanitize_number(self):
        return self.card_num.replace(" ", "")

    def double_digit(self, digit):
        doubled = digit * 2
        return doubled if doubled < 10 else doubled - 9

    def valid(self):
        card_num = self.sanitize_number()

        if len(card_num) < 2:
            return False

        if not card_num.isdigit():
            return False

        card_num_list = [int(digit) for digit in card_num]
        card_num_list.reverse()

        for index, digit in enumerate(card_num_list):
            if index % 2 == 1:
                card_num_list[index] = self.double_digit(digit)

        sum_digits = sum(card_num_list)

        return sum_digits % 10 == 0
