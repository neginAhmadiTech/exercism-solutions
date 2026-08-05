"""Module for finding the fewest number of coins needed to make change for a given amount.
"""
def find_fewest_coins(coins, target):
    """Find the fewest number of coins needed to make up the target amount.

    Args:
        coins (list): A list of coin denominations.
        target (int): The target amount to make change for.

    Returns:
        list: The list of coins that make up the target amount with the fewest number of coins.
    """

    if target < 0:
        raise ValueError("target can't be negative")

    memory = {}

    def find(amount):
        # Impossible path
        if amount < 0:
            return float("inf"), []

        # Base case
        if amount == 0:
            return 0, []

        # Already solved
        if amount in memory:
            return memory[amount]

        best_count = float("inf")
        best_list = []

        for coin in sorted(coins, reverse=True):
            count, coin_list = find(amount - coin)

            candidate = count + 1

            if candidate < best_count:
                best_count = candidate
                best_list = coin_list + [coin]

        memory[amount] = (best_count, best_list)
        return memory[amount]

    count, result = find(target)

    if count == float("inf"):
        raise ValueError("can't make target with given coins")

    return result
