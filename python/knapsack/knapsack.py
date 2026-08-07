"""Module for solving the knapsack problem using Dynamic programming approach.
"""
def maximum_value(maximum_weight, items):
    """Function to calculate the maximum value of items that
    can be placed in a knapsack with a given maximum weight.

    Args:
        maximum_weight (int): The maximum weight the knapsack can hold.
        items (list): A list of dictionaries, each containing 'weight' and 'value' keys.

    Returns:
        int: The maximum value that can be achieved without exceeding the maximum weight.
    """

    number_of_items = len(items)

    dp_matrix = [[float("inf")] * (number_of_items+1) for _ in range(maximum_weight+1)]


    # initialize first column
    for row_index, _ in enumerate(dp_matrix):
        dp_matrix[row_index][0] = 0

    for row in range(1, len(dp_matrix)):
        for col in range(1, len(dp_matrix[0])):

            # initialize first row
            dp_matrix[0][col] = 0

            item = items[col - 1]

            if item["weight"] <= row:
                take = item["value"] + dp_matrix[row - item["weight"]][col - 1]

                skip = dp_matrix[row][col - 1]

                dp_matrix[row][col] = max(take, skip)
            else:
                dp_matrix[row][col] = dp_matrix[row][col - 1]
                
    return dp_matrix[maximum_weight][number_of_items]
