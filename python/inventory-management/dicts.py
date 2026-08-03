"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    result = {}
    for item in items:
        result.setdefault(item, items.count(item))
    return result

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    items_dict = create_inventory(items)
    
    for item in items_dict:
        previous_value = inventory.get(item)

        if previous_value is None:
            inventory.setdefault(item, items.count(item))
        else:
            inventory.update({item: items.count(item) + previous_value})
    
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    items_dict = create_inventory(items)
    
    for item in items_dict:
        previous_value = inventory.get(item)
        
        if previous_value is not None:
            subtraction = max(previous_value - items.count(item), 0)
            inventory.update({item: subtraction})
    
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item) is not None:
        inventory.pop(item)
    
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    return [item for item in inventory.items() if item[1] > 0]
