def largest_product(series, size):

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if size < 0:
        raise ValueError("span must not be negative")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    max_product = 0
    for index in range(0, len(series) - size + 1):
        window = [int(digit) for digit in series[index : index + size]]

        product = 1
        for digit in window:
            product *= digit

        max_product = max(max_product, product)

    return max_product
