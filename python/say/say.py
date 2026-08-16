def handle_ones(number):
    match (number):
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case _:
            return ""


def handle_tens_special_numbers(number):
    match (number):
        case 0:
            return "ten"
        case 1:
            return "eleven"
        case 2:
            return "twelve"
        case 3:
            return "thirteen"
        case 5:
            return "fifteen"
        case 8:
            return "eighteen"
        case _:
            return f"{handle_ones(number)}teen"


def handle_tens(number):
    remainder = number % 10
    divisor = number // 10

    tens = {
        1: handle_tens_special_numbers(remainder),
        2: "twenty" if remainder == 0 else f"twenty-{handle_ones(remainder)}",
        3: "thirty" if remainder == 0 else f"thirty-{handle_ones(remainder)}",
        4: "forty" if remainder == 0 else f"forty-{handle_ones(remainder)}",
        5: "fifty" if remainder == 0 else f"fifty-{handle_ones(remainder)}",
        6: (
            f"{handle_ones(divisor)}ty"
            if remainder == 0
            else f"{handle_ones(divisor)}ty-{handle_ones(remainder)}"
        ),
        7: (
            f"{handle_ones(divisor)}ty"
            if remainder == 0
            else f"{handle_ones(divisor)}ty-{handle_ones(remainder)}"
        ),
        8: "eighty" if remainder == 0 else f"eighty-{handle_ones(remainder)}",
        9: (
            f"{handle_ones(divisor)}ty"
            if remainder == 0
            else f"{handle_ones(divisor)}ty-{handle_ones(remainder)}"
        ),
    }

    return tens[divisor]


def handle_hundreds(number):
    if number == 0:
        return ""
    if number % 100 == 0:
        return f"{handle_ones(number // 100)} hundred"
    if number % 10 == number:
        return f"{handle_ones(number)}"
    return f"{handle_ones(number // 100)} hundred {handle_tens(number % 100)}"


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    number_str = str(number)
    separated_number = [
        number_str[max(0, index - 3) : index] for index in range(len(number_str), 0, -3)
    ]

    result = ""
    match (len(separated_number[-1])):
        case 1:
            result += handle_ones(int(separated_number[-1]))
        case 2:
            result += handle_tens(int(separated_number[-1]))
        case 3:
            result += handle_hundreds(int(separated_number[-1]))

    match (len(separated_number)):
        case 2:
            result += f" thousand {handle_hundreds(int(separated_number[-2]))}"

        case 3:
            thousand_part = (
                handle_hundreds(int(separated_number[-2])) + " thousand"
                if handle_hundreds(int(separated_number[-2]))
                else ""
            )

            hundred_number = handle_hundreds(int(separated_number[-3]))
            result += f" million {thousand_part} {hundred_number}"

        case 4:
            million_part = (
                handle_hundreds(int(separated_number[-2])) + " million"
                if handle_hundreds(int(separated_number[-2]))
                else ""
            )
            thousand_part = (
                handle_hundreds(int(separated_number[-3])) + " thousand"
                if handle_hundreds(int(separated_number[-3]))
                else ""
            )
            hundred_part = handle_hundreds(int(separated_number[-4]))

            result += f" billion {million_part} {thousand_part} {hundred_part}"

    return result.strip()
