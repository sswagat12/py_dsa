def bubble_sort(ip_list):
    length = len(ip_list)
    for each_check in range(length): #checking bubble sort for each swipe
        for index in range(length-1-each_check): #bubble sorting until the iteration
            if ip_list[index] > ip_list[index+1]:
                ip_list[index], ip_list[index+1] = ip_list[index+1], ip_list[index]
    return ip_list

# in each swipe, the largest element goes to the end of the list, hence we check len-each_swipe to only check for the required number

unsorted_list = [1,23,45,65,22,4,8]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)