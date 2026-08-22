def primes(limit):
    result = []

    numbers = list(range(2, limit + 1))

    while numbers:

        number, *numbers = numbers

        result.append(number)

        multiplier_list = (
            list(range(number * number, max(numbers) + 1, number)) if numbers else []
        )

        numbers = [item for item in numbers if item not in multiplier_list]

    return result
