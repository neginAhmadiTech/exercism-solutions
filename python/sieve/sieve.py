def primes(limit):
    result = []

    if limit == 0:
        return []

    numbers = set(range(2, limit + 1))

    while numbers:
        number, *numbers = sorted(numbers)
        result.append(number)
        multiplier_list = [
            multiplier for multiplier in numbers if multiplier % number == 0
        ]

        numbers = set(numbers) - set(multiplier_list)

    return result
