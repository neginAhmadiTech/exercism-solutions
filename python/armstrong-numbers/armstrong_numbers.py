def is_armstrong_number(number):

    str_number = str(number)
    number_length = len(str_number)
    sum_of_digits = 0

    for digit in str_number:
        sum_of_digits += int(digit) ** number_length
    
    return sum_of_digits == number

