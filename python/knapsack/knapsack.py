"""Module for solving the knapsack problem using a greedy algorithm approach.
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

    if maximum_weight == 0 or len(items) == 0:
        return 0
    
    sorted_items = sorted(items, key=lambda item: item['value'])
    sorted_items.reverse()
        
    result = 0
    current_weight = 0
    while current_weight <= maximum_weight:
        
        last_item = {}
        for item in sorted_items:
            if current_weight + item['weight'] > maximum_weight:
                last_item = item
                break
            
            current_weight += item['weight']
            result += item['value']
            
        if current_weight + last_item['weight'] > maximum_weight:
            break        
    
    return result