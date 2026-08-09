"""Module for generating combinations of numbers that sum up to a target value,
with a specified size and excluding certain numbers.
"""

def combinations(target, size, exclude):
    """Function to find all possible combinations of numbers that sum up to a target value,
    with a specified size and excluding certain numbers.

    Args:
        target (int): The sum that each combination should add up to.
        size (int): The number of elements in each combination.
        exclude (list): The list of numbers to exclude from the combinations.

    Returns:
        list: The list of all possible combinations of numbers that sum up to the target,
        with the given size and excluding the specified numbers.
    """

    result = []
    
    def solve(size, candidate, start, current_sum):

        # base case
        if size == 0:
            if current_sum == target:
                solution = candidate.copy()
                result.append(solution)
            return

        for number in range(start, 10):
            if number in exclude:
                continue

            candidate.append(number)
            new_sum = current_sum + number

            if new_sum > target:
                candidate.pop()
                continue

            solve(size - 1, candidate, number+1, new_sum)
            candidate.pop()
        
        return result

    result = solve(size, [], 1, 0)
               
    return result

combinations(7, 3, [])