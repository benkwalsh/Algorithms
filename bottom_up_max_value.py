class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""

    n = len(items)+1
    table = [(capacity+1) * [0] for _ in range(n)]

    for i in range(1,n):
        for j in range(capacity+1):
            if items[i-1].weight > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j],
                                  (items[i-1].value + table[i-1][j-items[i-1].weight]))
    
    # Retrieve the items contributing to the maximum value
    item_list = []
    i = n - 1
    j = capacity
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            item_list.append(items[i - 1])
            j -= items[i - 1].weight
        i -= 1

    return max(table[n - 1]), item_list    


# Test case:
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(maximum)
# Check the returned item list with a hidden function
check_item_list(items, selected_items, maximum)
# Projected output
# 170

