"""
find the max profit we can get from the stock prices
[5,9,19,2,,1,17]
"""

def max_profit(prices_list):
    smallest = prices_list[0]
    largest = max(prices_list)
    if smallest  == largest:
        max_profit(prices_list[1:])
    diff = largest - smallest
    print(f"smallest: {smallest}, largest: {largest}, diff: {diff}")
    print(f"prices_list.index(largest)-----------{prices_list.index(largest)}")
    current_largest_index = prices_list.index(largest)
    for each_index in range(1, current_largest_index):
        if prices_list[each_index] < smallest:
            diff = largest - prices_list[each_index]
    if prices_list.index(largest) == len(prices_list) - 1:
        return diff
    max_profit(prices_list[current_largest_index+1:])
    return diff
        


print(max_profit([18,15,6,4,5]))