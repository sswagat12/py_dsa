def selection_sort(arr):
    length = len(arr)
    for each_swipe in range(length-1):
        min_index = each_swipe
        for each_index in range(each_swipe, length):
            if arr[each_index] < arr[min_index]:
                min_index = each_index
        arr[each_swipe], arr[min_index] = arr[min_index], arr[each_swipe]
    return arr






unsorted_arr = [24,78,54,23,67,1,9,3]
sorted_arr = selection_sort(unsorted_arr)
print(sorted_arr)

"""In selection sort, we find the lowest element, swap it to left most, 2nd lowest ans swap and continue until len -1"""