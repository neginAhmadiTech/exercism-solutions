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


    min_coins_count = [float('inf')] * (target + 1)
    min_coins_list = [[]] * (target + 1)
    min_coins_count[0] = 0  # Base case: 0 coins are needed to make the amount 0
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                candidate = min_coins_count[amount - coin] + 1

                if candidate < min_coins_count[amount]:
                    min_coins_count[amount] = candidate
                    min_coins_list[amount] = min_coins_list[amount - coin] + [coin]


    if min_coins_count[target] == float('inf'):
        raise ValueError("can't make target with given coins")


    min_coins_list[target].reverse()
    return min_coins_list[target]
