def first_rule(number, candidates):
    return number == sum(candidates)


def second_rule(first_number, second_number, third_number):
    return first_number**2 + second_number**2 == third_number**2


def triplets_with_sum(number):
    result = []

    for first_number in range(1, number + 1):
        for second_number in range(first_number + 1, number + 1):

            for third_number in range(second_number + 1, number + 1):

                if first_rule(
                    number, [first_number, second_number, third_number]
                ) and second_rule(first_number, second_number, third_number):

                    result.append([first_number, second_number, third_number])

    return result
