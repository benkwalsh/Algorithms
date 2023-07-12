import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


cache = {}
def max_value(items, capacity):
    """ calculates the maximum capacity a knapsack can hold dependent on their weights 
        and values.
    """
    n = len(items)

    if (n, capacity) in cache:
        return cache[(n, capacity)]
    elif n ==0 or capacity == 0:
        return 0 
    elif items[-1].weight > capacity:
        return max_value(items[:-1], capacity)
    else:
        cache[(n, capacity)] = max(max_value(items[:-1], capacity),
                                   items[-1].value + 
                                   max_value(items[:-1], capacity - items[-1].weight))
        
    return cache[(n, capacity)]

# test case:
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]
print(max_value(items, 10))
# projected output:
# 170


