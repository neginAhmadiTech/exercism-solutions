BASE_NUMBERS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def roman(number):
    base_numbers_list = list(BASE_NUMBERS.keys())
    roman_number = ""

    for base_number in base_numbers_list:
        while base_number <= number:
            number -= base_number
            roman_number += BASE_NUMBERS[base_number]

    return roman_number
